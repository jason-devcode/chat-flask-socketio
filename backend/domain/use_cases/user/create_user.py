from backend.domain.repositories.repository import CommonCRUDRepository


class CreateUserUseCase:
    def __init__(self, user_repository: CommonCRUDRepository):
        self.user_repository = user_repository

    def execute( username: str, password: str, birth: str ):
        ...