from dataclasses import asdict, dataclass
from datetime import date, datetime
from typing import Any, Dict


@dataclass
class User:
    id: str
    username: str
    password: str
    birth: date
    roles_bitmask: int  # Store user roles in bitmask value

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the User object into a dictionary for database storage.
        """
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "birth": self.birth.isoformat(),  # Store date as ISO string
            "roles_bitmask": self.roles_bitmask,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "User":
        """
        Creates a User object from a dictionary.
        """
        return cls(
            id=str(data["id"]),
            username=data["username"],
            password=data["password"],
            birth=datetime.fromisoformat(
                data["birth"]
            ).date(),  # Convert ISO string to date
            roles_bitmask=data["roles_bitmask"],
        )
