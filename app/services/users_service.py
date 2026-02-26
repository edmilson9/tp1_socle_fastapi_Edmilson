from app.services.users_service_protocols import IUsersService
from app.models.user_model import UserModel
from app.models.user_model_create import UserModelCreate

class UsersService (IUsersService):
    users : list[UserModel]

    def __init__(self, factory, settings):
        self.users = factory.create_users(settings.users_json_path)

    def list_users(self) -> list[UserModel]:
        return self.users.copy()

    def get_user_by_id(self, user_id : int) -> UserModel | None : 
        for u in self.list_users():
            if u.id == user_id:
                return u
            
    def create_user(self, payload: UserModelCreate) -> UserModel:
        if len(self.users) == 0:
            new_id = 1
        else:
            new_id = max([u.id for u in self.users]) + 1
        new_user = UserModel(id=new_id, **payload.model_dump())
        self.users.append(new_user)
        return new_user