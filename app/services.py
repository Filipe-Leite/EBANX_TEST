from .repositories import account_repository
from .models import AccountResponse

class AccountService:
    @staticmethod
    def deposit(destination: str, amount: int) -> AccountResponse:
        balance = account_repository.deposit(destination, amount)
        return AccountResponse(id=destination, balance=balance)
