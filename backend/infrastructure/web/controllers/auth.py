from common.utils.logger import Logger
from domain.use_cases.auth.signup import SignUpUseCase


class AuthenticationController:
    def __init__(self, logger: Logger, signup_use_case: SignUpUseCase):
        self.logger = logger
        self.signup_use_case = signup_use_case

    def signup(self, username: str, password: str, confirm_password: str, birth: str):
        try:
            data, success = self.signup_use_case.execute(
                username, password, confirm_password, birth
            )
            return {**data, "success": success}, 200 if success else 400
        except Exception as unknown_error:
            return {"message": "User cannot sign up!", "success": False}, 400
