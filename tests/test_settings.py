import pytest
from app.core.settings import  Settings

def test_should_use_default_path_when_env_var_is_not_set(monkeypatch):
    monkeypatch.delenv("USERS_JSON_PATH", raising = False)
    settings = Settings()
    assert settings.users_json_path == "data/users/json"

def test_should_use_default_path_when_env_var_is_not_set(monkeypatch):
    monkeypatch.setenv("USERS_JSON_PATH", "custom/users/json")
    settings = Settings()
    assert settings.users_json_path == "custom/users/json"