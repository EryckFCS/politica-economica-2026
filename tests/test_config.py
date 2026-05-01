from __future__ import annotations

from src.core.config import PEConfig


def _reset_peconfig() -> None:
    PEConfig._instance = None


def test_peconfig_discovers_root_and_config_path(tmp_path, monkeypatch):
    project_root = tmp_path / "economic_policy"
    nested_dir = project_root / "docs" / "evidence"
    nested_dir.mkdir(parents=True)
    (project_root / "pyproject.toml").write_text(
        "[project]\nname = 'politica-economica'\n", encoding="utf-8"
    )

    monkeypatch.chdir(nested_dir)
    _reset_peconfig()

    config = PEConfig()

    assert config.root_path == project_root
    assert config.config_path == project_root / "config" / "params.yaml"
    assert config.has_config is False
    assert config.params == {}


def test_peconfig_reload_reads_yaml_when_present(tmp_path, monkeypatch):
    project_root = tmp_path / "economic_policy"
    project_root.mkdir()
    (project_root / "pyproject.toml").write_text(
        "[project]\nname = 'politica-economica'\n", encoding="utf-8"
    )

    config_dir = project_root / "config"
    config_dir.mkdir()
    (config_dir / "params.yaml").write_text(
        "collection: economic_policy\nrefresh:\n  enabled: true\n",
        encoding="utf-8",
    )

    monkeypatch.chdir(project_root)
    _reset_peconfig()

    config = PEConfig()

    assert config.params == {"collection": "economic_policy", "refresh": {"enabled": True}}
    assert config.reload() == config.params
    assert config.has_config is True


def test_peconfig_ignores_reinitialization(tmp_path, monkeypatch):
    project_root = tmp_path / "economic_policy"
    project_root.mkdir()
    (project_root / "pyproject.toml").write_text(
        "[project]\nname = 'politica-economica'\n", encoding="utf-8"
    )

    monkeypatch.chdir(project_root)
    _reset_peconfig()

    first_config = PEConfig()
    monkeypatch.chdir(tmp_path)
    second_config = PEConfig()

    assert second_config is first_config
    assert second_config.root_path == project_root


def test_peconfig_returns_empty_params_for_non_mapping_yaml(tmp_path, monkeypatch):
    project_root = tmp_path / "economic_policy"
    project_root.mkdir()
    (project_root / "pyproject.toml").write_text(
        "[project]\nname = 'politica-economica'\n", encoding="utf-8"
    )

    config_dir = project_root / "config"
    config_dir.mkdir()
    (config_dir / "params.yaml").write_text("- uno\n- dos\n", encoding="utf-8")

    monkeypatch.chdir(project_root)
    _reset_peconfig()

    config = PEConfig()

    assert config.params == {}


def test_peconfig_recovers_from_invalid_yaml(tmp_path, monkeypatch):
    project_root = tmp_path / "economic_policy"
    project_root.mkdir()
    (project_root / "pyproject.toml").write_text(
        "[project]\nname = 'politica-economica'\n", encoding="utf-8"
    )

    config_dir = project_root / "config"
    config_dir.mkdir()
    (config_dir / "params.yaml").write_text("collection: [sin cerrar\n", encoding="utf-8")

    monkeypatch.chdir(project_root)
    _reset_peconfig()

    config = PEConfig()

    assert config.params == {}


def test_peconfig_falls_back_to_current_directory_when_no_markers(tmp_path, monkeypatch):
    current_dir = tmp_path / "isolated" / "workspace"
    current_dir.mkdir(parents=True)

    monkeypatch.chdir(current_dir)
    _reset_peconfig()

    config = PEConfig()

    assert config.root_path == current_dir
    assert config.config_path == current_dir / "config" / "params.yaml"
