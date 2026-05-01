from __future__ import annotations

import src.core.brain as brain_module
from src.core.brain import PEBrain


class FakeMemory:
    def __init__(self) -> None:
        self.calls: list[dict[str, object]] = []

    def recall(self, *, query: str, n_results: int, collection: str):
        self.calls.append(
            {
                "query": query,
                "n_results": n_results,
                "collection": collection,
            }
        )
        return [{"content": "respuesta", "metadata": {"source_name": "demo"}}]


def test_pebrain_uses_injected_memory():
    fake_memory = FakeMemory()
    brain = PEBrain(memory=fake_memory)

    results = brain.recall_theory("política fiscal", top_n=3)

    assert results == [{"content": "respuesta", "metadata": {"source_name": "demo"}}]
    assert fake_memory.calls == [
        {"query": "política fiscal", "n_results": 3, "collection": "economic_policy"}
    ]
    assert brain.is_available is True
    assert brain.connection_error is None


def test_pebrain_handles_agentmemory_failure(monkeypatch):
    class RaisingAgentMemory:
        def __init__(self, *args, **kwargs) -> None:
            raise RuntimeError("vector store unavailable")

    monkeypatch.setattr(brain_module, "AgentMemory", RaisingAgentMemory)

    brain = brain_module.PEBrain()

    assert brain.memory is None
    assert brain.connection_error == "vector store unavailable"
    assert brain.recall_theory("anything") == []
    assert brain.is_available is False
