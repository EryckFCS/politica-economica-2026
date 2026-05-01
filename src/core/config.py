from __future__ import annotations

from pathlib import Path
from typing import Any, ClassVar

import yaml


class PEConfig:
    """Configuración canonizada del nodo Economic Policy.

    Resuelve la raíz del proyecto, expone la ruta de configuración local y
    mantiene compatibilidad con el contrato histórico del nodo.
    """

    _instance: ClassVar[PEConfig | None] = None
    project_name: str = "Economic Policy"
    rag_collection: str = "economic_policy"

    def __new__(cls) -> PEConfig:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self) -> None:
        if getattr(self, "_initialized", False):
            return

        self.root_path = self._discover_root()
        self.config_path = self.root_path / "config" / "params.yaml"
        self.params: dict[str, Any] = {}
        self.has_config = False
        self.reload()
        self._initialized = True

    def _discover_root(self) -> Path:
        current = Path.cwd().resolve()
        for candidate in (current, *current.parents):
            if (candidate / "pyproject.toml").is_file():
                return candidate
        return current

    def _load_params(self) -> dict[str, Any]:
        if not self.config_path.is_file():
            return {}

        try:
            loaded = yaml.safe_load(self.config_path.read_text(encoding="utf-8"))
        except yaml.YAMLError:
            return {}

        if isinstance(loaded, dict):
            return loaded
        return {}

    def reload(self) -> dict[str, Any]:
        self.params = self._load_params()
        self.has_config = self.config_path.is_file() and bool(self.params)
        return self.params


NodeSettings = PEConfig
settings = PEConfig()
