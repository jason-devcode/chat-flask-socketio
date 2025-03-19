from abc import ABC

from backend.domain.entities.User import User


class UserRepository(ABC):
    def __init__(self):
        pass

    def create(self, user_data: User) -> bool | None:
        raise Exception("Create user method is not implemented")

    def get_by_id(self, uuid: str) -> User | None:
        raise Exception("get user by id is not implemented")

    def delete_by_id(self, uuid: str) -> bool | None:
        raise Exception("Delete user method is not implemented")

    def update(self, uuid: str, user_data: User) -> bool | None:
        raise Exception("Update user method is not implemented")
