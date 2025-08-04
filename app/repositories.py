from typing import Dict

class AccountRepository:
    def __init__(self):
        self._accounts: Dict[str, int] = {}

    def reset(self):
        self._accounts = {}


account_repository = AccountRepository()