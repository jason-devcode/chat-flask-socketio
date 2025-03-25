from common.utils.logger import Logger
from common.utils.sanitize_password import sanitize_password
from domain.repositories.user import UserRepository


class SignUpUseCase:
    def __init__(self, logger: Logger, user_repository: UserRepository):
        self.user_repository = user_repository
        self.logger = logger

    def execute(self, username: str, password: str, confirm_password: str, birth: str):
        try:
            sanitize_message, is_valid = sanitize_password(password, confirm_password)

            if not is_valid:
                return sanitize_message, False

            result = {}
            return result
        except Exception as unknown_error:
            self.logger.error(str(unknown_error))
            return {"message": "Unknown error!"}, False
