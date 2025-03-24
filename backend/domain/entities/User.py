from dataclasses import dataclass
from datetime import date

from common.constants.roles import Roles


class User(dataclass):
    id: str
    username: str
    password: str
    birth: date
    roles_bitmask: int  # store user roles in bitmask value
