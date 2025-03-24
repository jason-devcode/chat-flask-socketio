from abc import ABC

from domain.entities.User import User


class UserRepository(ABC):
    def __init__(self):
        pass

    def create(self, user: User) -> bool | None:
        raise Exception("Create user method is not implemented")

    def get_by_id(self, id: str) -> User | None:
        raise Exception("get user by id is not implemented")

    def delete_by_id(self, id: str) -> bool | None:
        raise Exception("Delete user method is not implemented")

    def update(self, id: str, user: User) -> bool | None:
        raise Exception("Update user method is not implemented")
