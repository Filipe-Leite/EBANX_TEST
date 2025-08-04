from typing import Dict

class AccountRepository:
    def __init__(self):
        self._accounts: Dict[str, int] = {}

    def reset(self):
        self._accounts = {}

    def get_balance(self, account_id: str) -> int | None:
        return self._accounts.get(account_id)
    
    def deposit(self, account_id: str, amount: int):
        self._accounts[account_id] = self._accounts.get(account_id, 0) + amount
        return self._accounts[account_id]

account_repository = AccountRepository()