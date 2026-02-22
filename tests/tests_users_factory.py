import pytest
from app.factories.users_factory import users_factory
from app.core.settings import Settings

def test_should_raise_ValueError_if_key_not_in_file(monkeypatch):
    #Arrange
    monkeypatch.setenv("USERS_JSON_PATH", "data/users_test.json")
    u = users_factory()
    settings = Settings()
    chemin = settings.users_json_path

    #Act / Assert
    with pytest.raises(ValueError):
        utilisateur = u.create_users(chemin)


def test_should_create_users_given_right_key():
    #Arrange
    u = users_factory()
    settings = Settings()
    chemin = settings.users_json_path
    #Act
    utilisateur = u.create_users(chemin)
    
    #Assert
    assert isinstance(utilisateur, list)
    assert len(utilisateur) == 1000
    assert utilisateur[0].login == "user0001"


def test_should_not_create_users_given_wrong_data_format(monkeypatch): 
    #Arrange
    monkeypatch.setenv("USERS_JSON_PATH", "data/u_test.json")
    u = users_factory()
    settings = Settings()
    chemin = settings.users_json_path
    
    # Act / Assert
    with pytest.raises(ValueError):
        utilisateur = u.create_users(chemin)

