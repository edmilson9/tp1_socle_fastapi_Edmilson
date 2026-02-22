from abc import abstractmethod

class users_factory_protocol:
    
    @abstractmethod
    def create_users(self, chemin: str):
        pass