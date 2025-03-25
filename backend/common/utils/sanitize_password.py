import re
from typing import Optional, Tuple

MIN_USER_PASSWORD_LENGTH = 6


class PasswordValidator:
    def __init__(self, next_validator=None):
        self.next_validator = next_validator

    def validate(
        self, password: str, confirm_password: str
    ) -> Tuple[Optional[dict], bool]:
        if self.next_validator:
            return self.next_validator.validate(password, confirm_password)
        return None, True


class TypeValidator(PasswordValidator):
    def validate(
        self, password: str, confirm_password: str
    ) -> Tuple[Optional[dict], bool]:
        if not (isinstance(password, str) and isinstance(confirm_password, str)):
            return {
                "message": "Both password and confirmation must be string values."
            }, False
        return super().validate(password, confirm_password)


class LengthValidator(PasswordValidator):
    def validate(
        self, password: str, confirm_password: str
    ) -> Tuple[Optional[dict], bool]:
        if len(password) < MIN_USER_PASSWORD_LENGTH:
            return {
                "message": f"Password must be at least {MIN_USER_PASSWORD_LENGTH} characters long."
            }, False
        return super().validate(password, confirm_password)


class MatchValidator(PasswordValidator):
    def validate(
        self, password: str, confirm_password: str
    ) -> Tuple[Optional[dict], bool]:
        if password != confirm_password:
            return {
                "message": "Passwords do not match. Please ensure both fields are identical."
            }, False
        return super().validate(password, confirm_password)


class UppercaseValidator(PasswordValidator):
    def validate(
        self, password: str, confirm_password: str
    ) -> Tuple[Optional[dict], bool]:
        if not re.search(r"[A-Z]", password):
            return {
                "message": "Password must contain at least one uppercase letter (A-Z)."
            }, False
        return super().validate(password, confirm_password)


class LowercaseValidator(PasswordValidator):
    def validate(
        self, password: str, confirm_password: str
    ) -> Tuple[Optional[dict], bool]:
        if not re.search(r"[a-z]", password):
            return {
                "message": "Password must contain at least one lowercase letter (a-z)."
            }, False
        return super().validate(password, confirm_password)


class DigitValidator(PasswordValidator):
    def validate(
        self, password: str, confirm_password: str
    ) -> Tuple[Optional[dict], bool]:
        if not re.search(r"\d", password):
            return {
                "message": "Password must include at least one numeric digit (0-9)."
            }, False
        return super().validate(password, confirm_password)


class SpecialCharacterValidator(PasswordValidator):
    def validate(
        self, password: str, confirm_password: str
    ) -> Tuple[Optional[dict], bool]:
        if not re.search(r"[!@#$%^&*()\[\]{};:'\"\\|,.<>?/`~]", password):
            return {
                "message": "Password must contain at least one special character."
            }, False
        return super().validate(password, confirm_password)


class SpaceValidator(PasswordValidator):
    def validate(
        self, password: str, confirm_password: str
    ) -> Tuple[Optional[dict], bool]:
        if " " in password:
            return {"message": "Password should not contain spaces."}, False
        return super().validate(password, confirm_password)


class CommonPasswordValidator(PasswordValidator):
    COMMON_PATTERNS = [
        "password",
        "123456",
        "qwerty",
        "abc123",
        "letmein",
        "welcome",
        "111111",
        "password1",
    ]

    def validate(
        self, password: str, confirm_password: str
    ) -> Tuple[Optional[dict], bool]:
        if any(pattern in password.lower() for pattern in self.COMMON_PATTERNS):
            return {
                "message": "Password is too common. Choose a more secure password."
            }, False
        return super().validate(password, confirm_password)


def sanitize_password(
    password: str, confirm_password: str
) -> Tuple[Optional[dict], bool]:
    validator_chain = TypeValidator(
        LengthValidator(
            MatchValidator(
                UppercaseValidator(
                    LowercaseValidator(
                        DigitValidator(
                            SpecialCharacterValidator(
                                SpaceValidator(CommonPasswordValidator())
                            )
                        )
                    )
                )
            )
        )
    )

    return validator_chain.validate(password, confirm_password)
