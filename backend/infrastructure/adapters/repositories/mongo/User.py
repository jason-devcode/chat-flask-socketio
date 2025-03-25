from os import getenv

from bson import ObjectId
from common.constants.env_keys import MONGO_DB_NAME_KEY, MONGO_URI_KEY
from common.utils.repository_register import register_repository
from domain.entities.User import User
from domain.ports.repositories.user import UserRepository
from pymongo import MongoClient


@register_repository("users", "mongo")  # Category: users, Database: MongoDB
class MongoUserRepository(UserRepository):
    """
    MongoDB implementation of the UserRepository interface.
    This class provides CRUD operations for User entities in a MongoDB database.
    """

    def __init__(self):
        """Initializes the MongoDB client and sets up the user collection."""
        self.client = MongoClient(getenv(MONGO_URI_KEY))
        self.db = self.client[getenv(MONGO_DB_NAME_KEY)]
        self.collection = self.db["users"]

    def create(self, user: User) -> bool | None:
        """
        Inserts a new user into the MongoDB collection.

        :param user: The User entity to be stored.
        :return: True if the operation was acknowledged, otherwise None.
        """
        user_data = user.to_dict()
        user_data.pop("id", None)  # Remove id field to avoid conflicts
        result = self.collection.insert_one(user_data)
        return result.acknowledged

    def get_by_id(self, id: str) -> User | None:
        """
        Retrieves a user by their unique ID.

        :param id: The user's MongoDB ObjectId as a string.
        :return: A User object if found, otherwise None.
        """
        user_data = self.collection.find_one({"_id": ObjectId(id)})
        if not user_data:
            return None
        user_data["id"] = str(user_data.pop("_id"))  # Convert `_id` to `id`
        return User.from_dict(user_data)

    def get_by_username(self, username: str) -> User | None:
        """
        Retrieves a user by their username.

        :param username: The unique username of the user.
        :return: A User object if found, otherwise None.
        """
        user_data = self.collection.find_one({"username": username})
        if not user_data:
            return None
        user_data["id"] = str(user_data.pop("_id"))  # Convert `_id` to `id`
        return User.from_dict(user_data)

    def delete_by_id(self, id: str) -> bool | None:
        """
        Deletes a user by their unique ID.

        :param id: The user's MongoDB ObjectId as a string.
        :return: True if the user was deleted, otherwise None.
        """
        result = self.collection.delete_one({"_id": ObjectId(id)})
        return result.deleted_count > 0

    def update(self, id: str, user: User) -> bool | None:
        """
        Updates an existing user's data.

        :param id: The user's MongoDB ObjectId as a string.
        :param user: A User object with updated information.
        :return: True if the user was updated, otherwise None.
        """
        user_data = user.to_dict()
        user_data.pop("id", None)  # Ensure `id` is not stored
        result = self.collection.update_one({"_id": ObjectId(id)}, {"$set": user_data})
        return result.modified_count > 0
