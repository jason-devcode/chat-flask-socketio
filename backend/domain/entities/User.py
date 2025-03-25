from dataclasses import dataclass
from datetime import date


@dataclass
class User:
    id: str
    username: str
    password: str
    birth: date
    roles_bitmask: int  # store user roles in bitmask value
