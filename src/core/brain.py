from __future__ import annotations

from typing import Any

from ecs_quantitative.memory.agent_memory import AgentMemory


class PEBrain:
    """Consumidor del Motor RAG Central para Política Económica."""

    def __init__(self, collection: str = "politica_economica", memory: Any | None = None) -> None:
        self.collection = collection
        self.connection_error: str | None = None

        if memory is not None:
            self.memory = memory
            return

        try:
            self.memory = AgentMemory(collection_name=self.collection)
        except Exception as exc:
            self.memory = None
            self.connection_error = str(exc)

    def recall_theory(self, query: str, top_n: int = 5) -> list[dict[str, Any]]:
        """Recupera fundamentación teórica de los libros indexados."""
        if self.memory is None:
            return []

        return self.memory.recall(query=query, n_results=top_n, collection=self.collection)

    @property
    def is_available(self) -> bool:
        return self.memory is not None


brain = PEBrain()
