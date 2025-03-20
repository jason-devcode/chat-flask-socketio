from dataclasses import dataclass
from datetime import date


class Conversation(dataclass):
    id: str
    name: str
    created_at: date
    participants: list[int]
