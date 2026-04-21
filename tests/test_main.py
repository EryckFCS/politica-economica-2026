from __future__ import annotations

import runpy
import sys
from types import ModuleType

import pytest

import main as main_module


def test_build_status_reports_config_and_brain_state(tmp_path):
    config_path = tmp_path / "config" / "params.yaml"
    config_path.parent.mkdir(parents=True)
    config_path.write_text("collection: politica_economica\n", encoding="utf-8")

    config = type("Config", (), {"root_path": tmp_path, "config_path": config_path})()
    brain = type("Brain", (), {"collection": "politica_economica", "memory": object()})()

    status = main_module.build_status(config=config, brain=brain)

    assert status["project_root"] == str(tmp_path)
    assert status["config_path"] == str(config_path)
    assert status["config_exists"] is True
    assert status["rag_collection"] == "politica_economica"
    assert status["rag_available"] is True


def test_build_status_uses_local_defaults(monkeypatch, tmp_path):
    config_module = ModuleType("src.core.config")
    config_module.settings = type(
        "Config",
        (),
        {
            "root_path": tmp_path,
            "config_path": tmp_path / "config" / "params.yaml",
        },
    )()

    brain_module = ModuleType("src.core.brain")
    brain_module.brain = type(
        "Brain",
        (),
        {
            "collection": "politica_economica",
            "memory": None,
        },
    )()

    monkeypatch.setitem(sys.modules, "src.core.config", config_module)
    monkeypatch.setitem(sys.modules, "src.core.brain", brain_module)

    status = main_module.build_status()

    assert status["project_root"] == str(tmp_path)
    assert status["config_exists"] is False
    assert status["rag_available"] is False


def test_main_prints_summary(capsys, monkeypatch):
    monkeypatch.setattr(
        main_module,
        "build_status",
        lambda config=None, brain=None: {
            "project_root": "/tmp/economic_policy",
            "config_path": "/tmp/economic_policy/config/params.yaml",
            "config_exists": False,
            "rag_collection": "politica_economica",
            "rag_available": True,
        },
    )

    exit_code = main_module.main()
    captured = capsys.readouterr()

    assert exit_code == 0
    assert "Política Económica 2026" in captured.out
    assert "RAG disponible: sí" in captured.out


def test_main_entrypoint_exits_cleanly(monkeypatch, tmp_path):
    config_module = ModuleType("src.core.config")
    config_module.settings = type(
        "Config",
        (),
        {
            "root_path": tmp_path,
            "config_path": tmp_path / "config" / "params.yaml",
        },
    )()

    brain_module = ModuleType("src.core.brain")
    brain_module.brain = type(
        "Brain",
        (),
        {
            "collection": "politica_economica",
            "memory": object(),
        },
    )()

    monkeypatch.setitem(sys.modules, "src.core.config", config_module)
    monkeypatch.setitem(sys.modules, "src.core.brain", brain_module)

    with pytest.raises(SystemExit) as excinfo:
        runpy.run_module("main", run_name="__main__")

    assert excinfo.value.code == 0