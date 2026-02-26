from fastapi import APIRouter, Depends, HTTPException
from functools import lru_cache
from app.services.users_service import UsersService
from app.core.settings import Settings
from app.factories.users_factory import users_factory
from app.models.user_model_create import UserModelCreate


router = APIRouter()

@lru_cache
def get_users_service ():
    settings = Settings ()
    factory  = users_factory()
    return UsersService(factory, settings)

@router.get("/users")
def get_list_users(service: UsersService = Depends(get_users_service)):
    return service.list_users()


@router.get("/users/{user_id}")
def get_user_by_id( user_id : int, service: UsersService = Depends(get_users_service)):
    user =  service.get_user_by_id(user_id)
    if user == None:
        raise HTTPException(status_code=404, detail= f"User not found")
    return user

@router.post("/users")
def create_user( payload : UserModelCreate, service: UsersService = Depends(get_users_service)):
    return service.create_user(payload)