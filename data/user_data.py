from dataclasses import dataclass


@dataclass
class User:
    email: str
    password: str

registered_user = User(email="test1234@test.ru", password="qwerty123")
fake_user = User(email="test123test.ru", password="qwerty123")