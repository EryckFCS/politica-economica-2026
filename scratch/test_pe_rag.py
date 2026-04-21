from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.core.brain import brain  # noqa: E402


def verify_rag() -> None:
    print("🔍 Probando Cerebro Federado (PE)...")
    query = "Cuadro 3.5 matriz de relaciones instrumentos y objetivos macroeconómicos"
    results = brain.recall_theory(query, top_n=2)

    if not results:
        print("❌ No se encontraron resultados. ¿Se completó la indexación?")
        return

    print(f"✅ Se encontraron {len(results)} fragmentos relevantes.")
    for i, res in enumerate(results):
        print(f"\n--- Fragmento {i + 1} (Fuente: {res['metadata'].get('source_name')}) ---")
        print(f"{res['content'][:500]}...")


def main() -> int:
    verify_rag()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
