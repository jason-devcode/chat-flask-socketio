from dataclasses import dataclass
from datetime import date

from backend.common.constants.roles import Roles


class User(dataclass):
    id: str
    username: str
    password: str
    birth: date
    roles: Roles
