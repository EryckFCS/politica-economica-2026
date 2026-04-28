from __future__ import annotations

import asyncio
from pathlib import Path
from typing import Any

from ecs_quantitative.ingestion.processors.pdf import PDFProcessor
from ecs_quantitative.memory.agent_memory import AgentMemory


PROJECT_ROOT = Path(__file__).resolve().parents[1]
COLLECTION_NAME = "politica_economica"
MIN_CHUNK_LENGTH = 100


def discover_books(bibliography_dir: Path) -> list[Path]:
    """Return the local bibliography PDFs in a stable order."""
    return sorted(bibliography_dir.glob("*.pdf"))


def chunk_text(text: str, min_length: int = MIN_CHUNK_LENGTH) -> list[str]:
    """Split extracted text into the chunks stored in the central memory."""
    return [chunk.strip() for chunk in text.split("\n\n") if len(chunk.strip()) > min_length]


def clear_previous_entries(memory: AgentMemory, collection_name: str, book_id: str) -> None:
    try:
        collection = memory.client.get_collection(name=collection_name)
        collection.delete(where={"book_id": book_id})
    except Exception:
        return


def build_chunk_metadata(book_path: Path, book_id: str) -> dict[str, str]:
    return {
        "source_name": book_path.name,
        "book_id": book_id,
        "project": "economic_policy",
        "type": "theoretical_framework",
    }


def resolve_books_dir(project_root: Path) -> Path:
    candidates = (
        project_root / "docs/readings/unit-00-foundations/assets",
        project_root / "bibliography",
    )

    for candidate in candidates:
        if candidate.is_dir():
            return candidate

    return candidates[0]


async def ingest_bibliography(
    project_root: Path = PROJECT_ROOT,
    collection_name: str = COLLECTION_NAME,
    memory: Any | None = None,
    processor: Any | None = None,
) -> dict[str, int]:
    print("🧠 Sincronizador de Conocimiento PE v7.4.0")
    print("=" * 60)

    books_dir = resolve_books_dir(project_root)
    books = discover_books(books_dir)
    summary = {"books_found": len(books), "books_indexed": 0, "chunks_indexed": 0}

    if not books:
        print(f"⚠️ No se encontraron libros en '{books_dir}'.")
        return summary

    print(f"📡 Libros detectados para indexación: {len(books)}")

    memory = memory if memory is not None else AgentMemory(collection_name=collection_name)
    processor = processor if processor is not None else PDFProcessor(ocr_enabled=False)

    for book_path in books:
        book_id = book_path.stem[:20]
        print(f"\n📖 Procesando: {book_path.name}...")

        clear_previous_entries(memory, collection_name, book_id)

        text, _ = await processor.extract_text(str(book_path))
        chunks = chunk_text(text)
        print(f"   -> Fragmentando conocimiento: {len(chunks)} unidades.")

        print(f"   -> Alimentando Cerebro Central (Colección: {collection_name})...")
        for idx, chunk in enumerate(chunks):
            memory.store(
                content=chunk,
                metadata=build_chunk_metadata(book_path, book_id),
                doc_id=f"pe_{book_id}_{idx}",
                collection=collection_name,
            )

        summary["books_indexed"] += 1
        summary["chunks_indexed"] += len(chunks)

    print("\n" + "=" * 60)
    print("✨ ÉXITO: Bibliografía integrada en la Memoria Federada.")
    return summary


def main() -> int:
    asyncio.run(ingest_bibliography())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
