from __future__ import annotations

import runpy
from pathlib import Path

import pytest

from scripts import sync_brain


class FakeCollection:
    def __init__(self) -> None:
        self.deleted_filters: list[dict[str, str]] = []

    def delete(self, *, where):
        self.deleted_filters.append(where)


class FakeClient:
    def __init__(self, collection: FakeCollection) -> None:
        self.collection = collection
        self.requested_names: list[str] = []

    def get_collection(self, name: str):
        self.requested_names.append(name)
        return self.collection


class FakeMemory:
    def __init__(self) -> None:
        self.collection = FakeCollection()
        self.client = FakeClient(self.collection)
        self.calls: list[dict[str, object]] = []

    def store(self, **kwargs):
        self.calls.append(kwargs)


class FakeProcessor:
    def __init__(self, text: str) -> None:
        self.text = text
        self.calls: list[Path] = []

    async def extract_text(self, path: str):
        self.calls.append(Path(path))
        return self.text, {}


class FailingClient:
    def get_collection(self, name: str):
        raise RuntimeError(f"collection missing: {name}")


class FailingMemory:
    def __init__(self) -> None:
        self.client = FailingClient()


def test_discover_books_returns_sorted_pdfs(tmp_path):
    (tmp_path / "b.pdf").write_bytes(b"%PDF-1.4\n%%EOF\n")
    (tmp_path / "a.pdf").write_bytes(b"%PDF-1.4\n%%EOF\n")
    (tmp_path / "ignore.txt").write_text("x", encoding="utf-8")

    assert sync_brain.discover_books(tmp_path) == [tmp_path / "a.pdf", tmp_path / "b.pdf"]


def test_chunk_text_filters_short_fragments():
    text = "short\n\n" + ("x" * 101) + "\n\n" + ("y" * 120)

    assert sync_brain.chunk_text(text, min_length=100) == ["x" * 101, "y" * 120]


def test_clear_previous_entries_ignores_collection_errors():
    sync_brain.clear_previous_entries(FailingMemory(), sync_brain.COLLECTION_NAME, "sample")


@pytest.mark.asyncio
async def test_ingest_bibliography_returns_empty_summary_when_no_books(tmp_path):
    summary = await sync_brain.ingest_bibliography(
        project_root=tmp_path, memory=FakeMemory(), processor=FakeProcessor("")
    )

    assert summary == {"books_found": 0, "books_indexed": 0, "chunks_indexed": 0}


@pytest.mark.asyncio
async def test_ingest_bibliography_indexes_chunks_and_clears_previous_entries(tmp_path):
    bibliography_dir = tmp_path / "bibliography"
    bibliography_dir.mkdir()

    pdf_path = bibliography_dir / "Cuadrado-RouraJR-LibroPol.Economica4a.ed.2014.pdf"
    pdf_path.write_bytes(b"%PDF-1.4\n%%EOF\n")

    text = (
        "Instrumento fiscal orientado a la estabilización macroeconómica. " * 3
        + "\n\n"
        + "La política monetaria coordinada con la fiscalidad incide sobre el empleo y el exterior. "
        * 3
        + "\n\n"
        + "corto"
    )

    memory = FakeMemory()
    processor = FakeProcessor(text)

    summary = await sync_brain.ingest_bibliography(
        project_root=tmp_path,
        memory=memory,
        processor=processor,
    )

    book_id = pdf_path.stem[:20]

    assert summary == {"books_found": 1, "books_indexed": 1, "chunks_indexed": 2}
    assert processor.calls == [pdf_path]
    assert memory.client.requested_names == [sync_brain.COLLECTION_NAME]
    assert memory.collection.deleted_filters == [{"book_id": book_id}]
    assert len(memory.calls) == 2

    first_call = memory.calls[0]
    assert first_call["collection"] == sync_brain.COLLECTION_NAME
    assert first_call["doc_id"] == f"pe_{book_id}_0"
    assert first_call["metadata"]["project"] == "economic_policy"
    assert first_call["metadata"]["source_name"] == pdf_path.name
    assert first_call["metadata"]["book_id"] == book_id
    assert sync_brain.COLLECTION_NAME == "economic_policy"


def test_sync_brain_main_returns_zero_without_real_io(monkeypatch):
    calls: list[object] = []

    def fake_run(coro):
        calls.append(coro)
        coro.close()
        return {"books_found": 0, "books_indexed": 0, "chunks_indexed": 0}

    monkeypatch.setattr(sync_brain.asyncio, "run", fake_run)

    assert sync_brain.main() == 0
    assert len(calls) == 1


def test_sync_brain_entrypoint_exits_cleanly(monkeypatch):
    def fake_run(coro):
        coro.close()
        return 0

    monkeypatch.setattr(sync_brain.asyncio, "run", fake_run)

    with pytest.raises(SystemExit) as excinfo:
        runpy.run_path(sync_brain.__file__, run_name="__main__")

    assert excinfo.value.code == 0
