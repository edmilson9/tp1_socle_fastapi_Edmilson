from abc import abstractmethod
from app.models.user_model import UserModel
from app.models.user_model_create import UserModelCreate

class IUsersService:
    @abstractmethod
    def list_users() -> list[UserModel]:
        pass

    @abstractmethod
    def get_user_by_id(user_id : int) -> UserModel | None : 
        pass

    @abstractmethod
    def create_user(payload: UserModelCreate) -> UserModel:
        pass