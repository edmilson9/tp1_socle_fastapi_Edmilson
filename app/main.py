from factories.users_factory import users_factory
from core.settings import Settings

settings = Settings()
chemin = settings.users_json_path()
u = users_factory()
a = u.create_users(chemin)
print(a[1])