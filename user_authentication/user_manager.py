# user_manager.py
import json
import hashlib
import os

USERS_FILE = "users.json"

class UserManager:
    def __init__(self):
        if not os.path.exists(USERS_FILE):
            with open(USERS_FILE, "w") as f:
                json.dump({"users": {}}, f, indent=4)
        self.users = self._load_users()

    def _load_users(self):
        with open(USERS_FILE, "r") as f:
            return json.load(f)

    def _save_users(self):
        with open(USERS_FILE, "w") as f:
            json.dump(self.users, f, indent=4)

    def _hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def register_user(self, username: str, password: str) -> bool:
        """Register a new user. Returns False if username exists."""
        if username in self.users["users"]:
            return False

        self.users["users"][username] = {
            "password": self._hash_password(password),
            "sessions_completed": 0
        }
        self._save_users()
        return True

    def login_user(self, username: str, password: str) -> bool:
        """Validate login. Returns True if successful."""
        if username not in self.users["users"]:
            return False

        hashed_pw = self._hash_password(password)
        return self.users["users"][username]["password"] == hashed_pw

    def increment_session(self, username: str):
        """Update session count after a game session finishes."""
        if username in self.users["users"]:
            self.users["users"][username]["sessions_completed"] += 1
            self._save_users()

    def get_session_count(self, username: str) -> int:
        """Get number of sessions completed by a user."""
        if username in self.users["users"]:
            return self.users["users"][username]["sessions_completed"]
        return 0
