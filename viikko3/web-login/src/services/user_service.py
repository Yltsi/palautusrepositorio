from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        # Check if username and password are provided
        if not username or not password:
            raise UserInputError("Username and password are required")

        # Check if username is at least 3 characters long and consists of letters a-z
        if len(username) < 3 or not username.islower() or not username.isalpha():
            raise UserInputError("Username must be at least 3 characters long and contain only lowercase letters a-z")

        # Check if username is already in use
        if self._user_repository.find_by_username(username):
            raise UserInputError("Username is already in use")

        # Check if password is at least 8 characters long
        if len(password) < 8:
            raise UserInputError("Password must be at least 8 characters long")

        # Check if password contains non-letter characters
        if password.isalpha():
            raise UserInputError("Password must contain at least one non-letter character")

        # Check if password and password confirmation match
        if password != password_confirmation:
            raise UserInputError("Password and password confirmation do not match")


user_service = UserService()