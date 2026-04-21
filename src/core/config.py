from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


class PEConfig:
    """Configuración central del Nodo de Política Económica."""

    _instance: PEConfig | None = None

    def __new__(cls) -> PEConfig:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self) -> None:
        if getattr(self, "_initialized", False):
            return

        self.root_path = self._find_project_root()
        self.config_path = self.root_path / "config" / "params.yaml"
        self.params = self._load_params()
        self._initialized = True

    @staticmethod
    def _find_project_root() -> Path:
        current = Path.cwd().resolve()
        for candidate in (current, *current.parents):
            if (candidate / "pyproject.toml").is_file() or (candidate / ".git").exists():
                return candidate
        return current

    def _load_params(self) -> dict[str, Any]:
        if not self.config_path.is_file():
            return {}

        try:
            with self.config_path.open(encoding="utf-8") as handle:
                loaded = yaml.safe_load(handle) or {}
        except yaml.YAMLError:
            return {}

        return loaded if isinstance(loaded, dict) else {}

    def reload(self) -> dict[str, Any]:
        self.params = self._load_params()
        return self.params

    @property
    def has_config(self) -> bool:
        return self.config_path.is_file()


settings = PEConfig()
