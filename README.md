# LPE - Laboratorio de Política Económica 2026

El laboratorio organiza la documentación académica del curso y un soporte técnico mínimo para mantener la evidencia, la bibliografía y el acceso al motor RAG central.

## Qué contiene el repositorio

- [Índice documental](docs/README.md): navegación por sílabo, lecturas y evidencia disponible.
- [Sílabo](docs/syllabus/): marco formal de la materia.
- [Lecturas](docs/readings/): bibliografía y material de apoyo.
- [Evidencia U1](docs/evidence/U1-Elaboracion-Politica-Economica/AA-01-Aplicacion-Marco-Conceptual/index.qmd): actividad práctica principal disponible hoy.
- [Enunciado de la tarea U1](docs/evidence/U1-Elaboracion-Politica-Economica/tarea_AA.md): consigna de la actividad.

## Soporte técnico

- [main.py](main.py): resumen de estado del nodo.
- [src/core/config.py](src/core/config.py): descubrimiento de raíz y carga opcional de `config/params.yaml`.
- [src/core/brain.py](src/core/brain.py): wrapper sobre `ecs_quantitative.memory.agent_memory.AgentMemory`.
- [scripts/sync_brain.py](scripts/sync_brain.py): ingestión de PDFs desde `bibliography/` hacia la colección `politica_economica`.

## Mantenimiento y validación

```bash
uv sync
uv run python main.py
uv run pytest
```

Para reindexar la bibliografía local:

```bash
uv run python scripts/sync_brain.py
```

Para un smoke manual de RAG, fuera de CI:

```bash
uv run python scratch/test_pe_rag.py
```

La carpeta `docs/evidence/` concentra el material de entrega actual. `docs/README.md` es el índice canónico de lectura.

## 📄 Arquitectura de Reporteo (Quarto)

La redacción de informes y evidencia académica sigue el **Estándar Nivel 5**:
- El archivo `_quarto.yml` reside en la **raíz del repositorio**.
- Todo el output generado (HTML/PDF intermedios, dependencias JS/CSS) se excluye del control de versiones mediante reglas globales (`**/*_files/`).
- La configuración garantiza un entorno limpio sin carpetas ad-hoc generadas por renderizado individual.
