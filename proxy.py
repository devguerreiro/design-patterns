import time
from typing import Any, Dict


class Database:
    def find_user(self, user_id: int) -> Dict[str, Any]:
        time.sleep(1)
        return {"id": user_id, "cached": False}


class DatabaseProxy:
    def __init__(self) -> None:
        self.database = Database()
        self.cache: Dict[int, Any] = {}

    def find_user(self, user_id: int) -> Dict[str, Any]:
        if user_id in self.cache:
            return {**self.cache[user_id], "cached": True}
        user = self.database.find_user(user_id)
        self.cache[user_id] = user
        return user


proxy = DatabaseProxy()

assert proxy.find_user(1) == {"id": 1, "cached": False}
assert proxy.find_user(1) == {"id": 1, "cached": True}

assert proxy.find_user(2) == {"id": 2, "cached": False}
