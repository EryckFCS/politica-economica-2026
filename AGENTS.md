# AGENTS.md - High-Fidelity Federated Node: Economic Policy

> This repository is a Level 5 Pure Node in the Federated Architecture v8.1.5.
> It operates under the Constitution centralized in:
> `/home/erick-fcs/Capital_Workstation/capital-workstation-libs/.github/copilot-instructions.md`

## 1. Node Identity and Governance

| Field | Value |
| --- | --- |
| **Node** | Economic Policy (7mo Ciclo) |
| **Status** | Active - Federation v8.1.5 Intervention Phase |
| **Teacher** | Econ. Maria Gabriela Moreno Hurtado |
| **Central Library** | `ecs_quantitative` (capital-workstation-libs) |
| **Intelligence Level** | 5 - Intelligent Ecosystem with Controlled Autonomy |
| **Gatekeeper** | `tests/system/test_architecture.py` |
| **RAG** | `global_knowledge` (Federated Vector Store) |
| **Bibliography Vault** | `docs/writing/` |

## 2. Advanced Intelligence Capabilities (v2.0)

This node is an autonomous inference unit designed for:

1. Policy Analysis Audit: real-time evaluation of economic policies against the UNL (2026) academic framework.
2. Federated Knowledge Consumption: deep integration with `ecs_quantitative` for quantitative policy evaluation.
3. Atomic Evidence Mapping: absolute traceability between theoretical readings, workshop evidence, and Quarto deliveries.
4. Quarto Delivery Layer: separates the narrative layer from code and keeps presentation in `docs/writing/`.

## 3. Operational Protocols (Active Directives)

### 3.1. Guardian Protocol

- Invariant: every structural change must preserve the architecture gatekeeper and the data contracts.
- Action: before closing any task, run `uv run pytest tests/system/test_architecture.py`.
- Failure: if the test fails, the repository is unstable and the root cause must be fixed before any further change.

### 3.2. Research Protocol

- Detection: identify whether the task is Theory (Readings) or Application (Evidence).
- Location: analytical work lives in `docs/vaults/`; narratives and deliveries live in `docs/writing/`; governance lives in `docs/management/`; readings live in `docs/readings/`; the official syllabus lives in `docs/syllabus/`.
- Registration: every analysis must leave reproducible logs in its local `logs/` folder or in the corresponding vault.

## 4. Vault Architecture (Atomic Level 5)

### 4.1. Analytical Structure

```text
.
├── docs/
│   ├── vaults/            # Workshops, activities, and reports by unit (uX-[cat]-[seq]-slug)
│   │   ├── writing/             # Canonical narrative and delivery layer
│   ├── management/          # Planning, architecture, and risks
│   ├── readings/            # Theoretical readings and references
│   └── syllabus/            # Institutional and academic syllabus
├── src/                     # Core logic, tasks, and orchestration
├── scripts/                 # Support scripts and maintenance helpers
└── tests/                   # Gatekeepers and regression checks
```

### 4.2. Documentary Structure

- `docs/vaults/`: vaults with `index.qmd` and supporting assets.
- `docs/writing/`: canonical narrative, bibliography, and delivery layer.
- `docs/management/`: planning, architecture, and risks.
- `docs/readings/`: reading vault for foundational and thematic material.
- `docs/syllabus/`: syllabus and institutional documents.


## 5. Resilience Strategy

1. Zero Floating Doctrine: no analytical scripts should float in the root; operational logic stays in `src/` or the vaults.
2. Path Integrity: resolve paths with `pathlib` and project configuration, not hardcoded routes.
3. Data Lineage: curation and normalization must preserve traceability in logs and catalog files.
4. Quarto Hygiene: writing outputs must not mix with core logic or raw data.

## 6. Environment and Maintenance

```bash
uv sync
uv run pytest tests/test_vault_architecture.py tests/test_main.py
uv run python main.py
uv run python scripts/sync_brain.py
quarto render docs/vaults/u1-aa-01-policy-formulation/index.qmd --to pdf
```

## Golden Rule

> If something built here is useful for other courses, propose it for the central library.
# AGENTS.md Update: Centralized Lake Protocol (v8.1.5)

Este repositorio utiliza el **Data Lake Centralizado** de Capital Workstation para gestionar archivos pesados (Datasets y Bibliografía).

## 1. Protocolo de Recursos
- **Ubicación Física**: Los archivos reales residen en `~/.capital/lake/`.
- **Punteros Locales**: El archivo `config/resources.json` define qué recursos requiere este nodo.
- **Resolución**: Al inicializar el entorno o clonar por primera vez, se debe ejecutar la resolución de recursos para crear los enlaces simbólicos (Symlinks).

```bash
uv run python -c "from src.core.config import settings; settings.resolve_resources()"
```

## 2. Invariante de Git
- **Prohibido**: No se deben subir archivos `.xlsx`, `.dta`, `.pdf` o `.csv` pesados al repositorio.
- **Acción**: Si necesitas un nuevo archivo pesado, regístralo en el Lake y añade el puntero en `config/resources.json`.

---
*Actualización aplicada automáticamente durante la migración a Arquitectura v8.1.5.*

## Architecture v8.1.5 (Final Validation)
- Status: ✅ Synchronized and Lake-Linked.
- Date: 2026-05-01
- Operation: Massive Data Lake Centralization and RAG intelligence decoupling.

