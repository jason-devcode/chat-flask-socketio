import inspect
from abc import ABC, abstractmethod


def get_caller_info():
    frame = inspect.stack()[2]
    return f"File: {frame.filename}, Line: {frame.lineno}"


class CommonCRUDRepository(ABC):
    @abstractmethod
    def create(self, **kwargs):
        """Abstract method for creating a record."""
        raise NotImplementedError(
            f"Abstract Repository: create method not implemented\n{get_caller_info()}"
        )

    @abstractmethod
    def delete(self, **kwargs):
        """Abstract method for deleting a record."""
        raise NotImplementedError(
            f"Abstract Repository: delete method not implemented\n{get_caller_info()}"
        )

    @abstractmethod
    def read(self, **kwargs):
        """Abstract method for reading a record."""
        raise NotImplementedError(
            f"Abstract Repository: read method not implemented\n{get_caller_info()}"
        )

    @abstractmethod
    def update(self, **kwargs):
        """Abstract method for updating a record."""
        raise NotImplementedError(
            f"Abstract Repository: update method not implemented\n{get_caller_info()}"
        )
