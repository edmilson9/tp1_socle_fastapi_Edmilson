import json
from app.models.user_model import UserModel
from app.factories.users_factory_protocol import users_factory_protocol

class users_factory(users_factory_protocol):

    def create_users(self, chemin: str):
        with open(chemin) as r:
            users = json.load(r) 
        
        if 'users' not in users:
            raise ValueError("No users found")

        res = []
        for u in users["users"]: 
            user = UserModel(**u)
            res.append(user)
        return res
    
