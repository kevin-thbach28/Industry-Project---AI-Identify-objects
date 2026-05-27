import json
import os
import hashlib
from enum import Enum 

FILE_NAME = "user_information.json"


# create new file if not exists
if not os.path.exists(FILE_NAME):

    with open(FILE_NAME, "w") as file:
        json.dump({}, file)


class Role(Enum):
    ADMIN = "admin"
    ENGINEER = "engineer"
    TEACHER = "teacher"
    STUDENT = "student"


class User:
    def __init__(self, username: str, password: str, role: Role, is_active: bool = True):
        if not username or not password:
            raise ValueError("Username and password cannot be empty!")

        if not self.valid_password(password):
            raise ValueError("Password must be between 8 and 16 characters long!")

        self.username = username
        self.password = password
        self.is_active = is_active
        self.role = role

    # -------------------------
    # validate password
    # -------------------------
    @staticmethod
    def valid_password(password: str) -> bool:

        return 8 <= len(password) <= 16

    # -------------------------
    # hash password
    # -------------------------
    @staticmethod
    def hash_password(password: str):

        return hashlib.sha256(
            password.encode()
        ).hexdigest()


    # -------------------------
    # register
    # -------------------------
    def register(self):

        with open(FILE_NAME, 'r') as file:
            content = file.read()
            if content:
                users = json.loads(content)
            else:
                users = {}

        # check username
        if self.username in users:
            raise ValueError(
                f"Username {self.username} already exists!"
            )

        # add user
        users[self.username] = {
            "password": self.hash_password(self.password),
        }

        # save file
        with open(FILE_NAME, 'w') as file:
            json.dump(users, file, indent=4)

        return f"User {self.username} registered successfully!"


    # -------------------------
    # login
    # -------------------------
    def login(self):
        with open(FILE_NAME, "r") as file:
            content = file.read()
            if not content:
                users = {}
                self.register()
            else:
                users = json.loads(content)

        # username check
        if self.username not in users:
            raise ValueError(
                f"Username {self.username} does not exist!"
            )

        hashed_password = self.hash_password(self.password)

        # password check
        if users[self.username]["password"] != hashed_password:
            raise ValueError(
                f"Incorrect password for user {self.username}!"
            )

        return f"Login successful! Welcome {self.username}!"
    
        