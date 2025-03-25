from os import getenv
from typing import Any, Dict, Type

from common.constants.db_type_supported import DBTypeSupported
from common.constants.env_keys import DB_TYPE_ENV_KEY

# dictionary to store all repository categories and db types
_repository_registry: Dict[str, Dict[DBTypeSupported, Type[Any]]] = {}


def register_repository(category: str, db_type: DBTypeSupported):
    def wrapper(repository_class):
        if category not in _repository_registry:
            _repository_registry[category] = {}
        _repository_registry[category][db_type] = repository_class
        return repository_class

    return wrapper


def get_repository(category: str):
    # get db type (SQLite, MongoDB, etc) from environment variable.
    db_type: DBTypeSupported = DBTypeSupported(getenv(DB_TYPE_ENV_KEY))

    # get category in db (table name (SQL), document name (NoSQL), etc)
    category_registry = _repository_registry.get(category)

    if not category_registry:
        raise ValueError(f"Category {category} does'nt has support.")

    # now get concrete repository class by db type
    repository_class = category_registry.get(db_type)

    if not repository_class:
        raise ValueError(
            f"Repository class {category} in db type {db_type.value} not has support."
        )

    # return repository class instance
    return repository_class()
