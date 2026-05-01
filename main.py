from __future__ import annotations

from typing import Any


def build_status(config: Any | None = None, brain: Any | None = None) -> dict[str, Any]:
    if config is None:
        from src.core.config import settings as config

    if brain is None:
        from src.core.brain import brain as brain

    rag_collection = getattr(config, "rag_collection", "economic_policy")

    return {
        "project_root": str(config.root_path),
        "config_path": str(config.config_path),
        "config_exists": config.config_path.exists(),
        "rag_collection": rag_collection,
        "rag_available": getattr(brain, "memory", None) is not None,
    }


def main() -> int:
    status = build_status()
    print("Política Económica 2026")
    print(f"Root: {status['project_root']}")
    print(f"Config: {status['config_path']} ({'found' if status['config_exists'] else 'missing'})")
    print(f"RAG collection: {status['rag_collection']}")
    print(f"RAG disponible: {'sí' if status['rag_available'] else 'no'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
