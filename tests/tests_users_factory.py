import pytest
from app.factories.users_factory import users_factory

def test_should_raise_ValueError_if_key_not_in_file():
    #Arrange
    u = users_factory()
    chemin_fichier = "data/users_test.json"

    #Act / Assert
    with pytest.raises(ValueError):
        utilisateur = u.create_users(chemin_fichier)


def test_should_create_users_given_right_key():
    #Arrange
    u = users_factory()
    chemin_fichier = "data/users.json"

    #Act
    utilisateur = u.create_users(chemin_fichier)
    
    #Assert
    assert isinstance(utilisateur, list)
    assert len(utilisateur) == 1000
    assert utilisateur[0].login == "user0001"


def test_should_not_create_users_given_wrong_data_format(): 
    #Arrange
    u = users_factory()
    chemin_fichier = "data/u_test.json"
    
    # Act / Assert
    with pytest.raises(ValueError):
        utilisateur = u.create_users(chemin_fichier)