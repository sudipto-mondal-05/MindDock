from pathlib import Path

import app.core.config as config


def test_settings_resolve_storage_paths_from_project_root(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    config.get_settings.cache_clear()

    settings = config.get_settings()

    project_root = Path(__file__).resolve().parents[1]

    assert Path(settings.upload_dir).is_absolute()
    assert Path(settings.upload_dir) == (project_root / "storage" / "uploads").resolve()
    assert Path(settings.processed_dir) == (project_root / "storage" / "processed").resolve()
    assert Path(settings.export_dir) == (project_root / "storage" / "exports").resolve()
    assert Path(settings.temp_dir) == (project_root / "storage" / "temp").resolve()
