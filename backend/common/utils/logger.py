from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def info(message: str):
        raise Exception("not implemented")

    @abstractmethod
    def warning(message: str):
        raise Exception("not implemented")

    @abstractmethod
    def error(message: str):
        raise Exception("not implemented")
