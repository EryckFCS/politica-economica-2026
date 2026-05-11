from __future__ import annotations

from typing import Any

from ecs_quantitative.core.memory import AgentMemory

from .config import settings


class PEBrain:
    """Wrapper local del cerebro del nodo Economic Policy."""

    def __init__(self, memory: Any | None = None, config: Any | None = None) -> None:
        self.config = config if config is not None else settings
        self.collection = getattr(self.config, "rag_collection", "economic_policy")
        self.connection_error: str | None = None

        if memory is not None:
            self.memory = memory
            self.is_available = True
            return

        try:
            self.memory = AgentMemory(collection_name=self.collection)
            self.is_available = True
        except Exception as exc:
            self.memory = None
            self.connection_error = str(exc)
            self.is_available = False

    def recall_theory(self, query: str, top_n: int = 5) -> list[dict[str, Any]]:
        if self.memory is None:
            return []

        try:
            return self.memory.recall(query=query, n_results=top_n, collection=self.collection)
        except Exception as exc:
            self.connection_error = str(exc)
            self.is_available = False
            return []


NodeBrain = PEBrain
brain = PEBrain(config=settings)
