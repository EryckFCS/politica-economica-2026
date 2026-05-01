# Arquitectura - Política Económica 2026

## Propósito

Este repositorio organiza la evidencia, la escritura canónica y la gestión documental del nodo de Política Económica.

## Capas de trabajo

- `docs/vaults/`: evidencia reproducible. Unidad activa: `u1-aa-01-policy-formulation/`.
- `docs/writing/`: narrativa canónica y entregas.
- `docs/management/`: planificación, arquitectura y riesgos.
- `docs/readings/`: lecturas y bibliografía base.
- `docs/syllabus/`: marco institucional y académico.
- `main.py`: punto de entrada y resumen de estado.
- `src/core/`: configuración y cerebro RAG.
- `scripts/sync_brain.py`: sincronización bibliográfica.
- `tests/`: gatekeeper de bóvedas y pruebas de estado.
- `docs/writing/legacy/`: capa legacy de transición.

## Regla de uso

1. No duplicar la narrativa fuera de `docs/writing/`.
2. No mover la evidencia fuera de `docs/vaults/`.
3. Mantener sincronizados los metadatos bibliográficos con la escritura canónica.


## Intervención v8.1.5 (Endurecimiento)

El nodo ha sido endurecido y unificado en Python 3.12. Se eliminaron archivos flotantes y se centralizó la gestión del Data Lake vía `ecs_core`.