from user import User
from abc import ABC


class Angel(User):
    def __init__(self, is_locked):
        self._is_locked = is_locked

    def get_warning_message(self):
        pass


class Rebel(User):
    def __init__(self, is_locked):
        self._is_locked = is_locked

class TroubleMaker(User):
    def __init__(self, is_locked):
        self._is_locked = is_locked
