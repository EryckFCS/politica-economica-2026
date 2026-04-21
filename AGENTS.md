# AGENTS.md — Nodo Federado: Economic Policy

> Este repositorio es un **Nodo Puro** de la Arquitectura Federada v7.4.0.  
> Opera bajo la Constitución centralizada en `capital-workstation-libs`.

---

## Constitución

```
/home/erick-fcs/Capital_Workstation/capital-workstation-libs/.github/copilot-instructions.md
```

---

## Identidad del Nodo

| Campo | Valor |
|:---|:---|
| **Nodo** | Economic Policy |
| **Materia** | 7mo Ciclo — Universidad |
| **Docente** | Econ. Maria Gabriela Moreno Hurtado |
| **Estudiante** | Erick Fabricio Condoy Seraquive |
| **Período** | Marzo - Agosto 2026 |
| **Librería Central** | `ecs_quantitative` (capital-workstation-libs) |
| **Tipo** | Nodo Puro — consumidor, no reimplementa lógica |
| **RAG** | `global_knowledge` en `~/.capital/brain/vector_store/` |

---

## Ley de Nodo Puro (Obligatoria)

1. **No reimplementar** lógica que ya exista en `ecs_quantitative`.
2. **Importar siempre** desde la librería central.
3. **RAG**: usar la base central, nunca crear stores locales.

---

## Entorno

```bash
uv sync
uv run python main.py  # o el orquestador correspondiente
```

---

## Regla de Oro

> Si algo sirve para otras materias, propónlo para la librería central.
