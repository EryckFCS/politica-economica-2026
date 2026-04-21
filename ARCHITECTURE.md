# Arquitectura - Política Económica 2026

## Estado actual

Este repositorio funciona como nodo académico con soporte técnico mínimo. No existe un orquestador histórico tipo `M01-U1-LPE-Master_Build.py`; el flujo real hoy está en la documentación, la evidencia Quarto, el wrapper RAG y el script de sincronización bibliográfica.

## Capas de trabajo

### Documentación académica

- [docs/README.md](docs/README.md): índice canónico de lectura.
- [docs/syllabus/](docs/syllabus/): marco doctrinal de la materia.
- [docs/readings/](docs/readings/): lecturas y referencias.
- [docs/evidence/U1-Elaboracion-Politica-Economica/AA-01-Aplicacion-Marco-Conceptual/index.qmd](docs/evidence/U1-Elaboracion-Politica-Economica/AA-01-Aplicacion-Marco-Conceptual/index.qmd): evidencia principal disponible.

### Soporte técnico local

- [main.py](main.py): resumen del estado del nodo.
- [src/core/config.py](src/core/config.py): descubrimiento de raíz y carga opcional de parámetros.
- [src/core/brain.py](src/core/brain.py): wrapper del cerebro central.

### Mantenimiento del conocimiento

- [bibliography/](bibliography/): PDFs locales para indexación.
- [scripts/sync_brain.py](scripts/sync_brain.py): ingestión hacia la colección `politica_economica`.

### Verificación

- [tests/](tests/): suite formal de pytest.
- [scratch/test_pe_rag.py](scratch/test_pe_rag.py): smoke manual no integrado a CI.

## Regla de uso

1. Consultar [docs/README.md](docs/README.md) antes de escribir material nuevo.
2. Mantener la evidencia activa en `docs/evidence/` y no inventar carpetas de unidad que no existan.
3. Usar `tests/` para cobertura automática y dejar `scratch/` como verificación manual.
