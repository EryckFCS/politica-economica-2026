# LPE - Laboratorio de Política Económica 2026

El nodo organiza la documentación académica, la evidencia reproducible y el acceso al motor RAG central bajo la doctrina Level 5.

## Arquitectura documental

- [Índice documental](docs/README.md)
- [Bóveda de evidencia](docs/vaults/u1-aa-01-policy-formulation/index.qmd)
- [Bóveda de escritura](docs/writing/index.qmd)
- [Bóveda de gestión](docs/management/index.qmd)
- [Bóveda de lecturas](docs/readings/index.qmd)
- [Bóveda de sílabo](docs/syllabus/index.qmd)

## Soporte técnico

- [main.py](main.py): resumen del estado del nodo.
- [src/core/config.py](src/core/config.py): descubrimiento de raíz y carga opcional de `config/params.yaml`.
- [src/core/brain.py](src/core/brain.py): wrapper sobre `ecs_quantitative.memory.agent_memory.AgentMemory`.
- [scripts/sync_brain.py](scripts/sync_brain.py): ingestión de PDFs desde `docs/readings/unit-00-foundations/assets/` hacia la colección `economic_policy`.

## Mantenimiento y validación

```bash
uv sync
uv run python main.py
uv run pytest tests/test_vault_architecture.py tests/test_main.py
```

Para reindexar la bibliografía local:

```bash
uv run python scripts/sync_brain.py
```

Para un smoke manual de RAG, fuera de CI:

```bash
uv run python scratch/test_pe_rag.py
```

La carpeta `writing/` en la raíz del repositorio se conserva solo como transición histórica.
