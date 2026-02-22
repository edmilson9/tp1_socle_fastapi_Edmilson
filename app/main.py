import fastapi, pydantic, json
from factories.users_factory import users_factory
from models.user_model import UserModel

chemin_fichier = "data/users.json"

u = users_factory()
a = u.create_users(chemin_fichier)
print(a[1])