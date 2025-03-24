from domain.repositories.user import UserRepository


class CreateUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(username: str, password: str, birth: str): ...
