from .repositories import account_repository
from .models import *

class AccountService:
    @staticmethod
    def deposit(destination: str, amount: int) -> AccountResponse:
        balance = account_repository.deposit(destination, amount)
        return DepositResponse(destination={"id": destination, 
                                            "balance":balance
                                            }
                )
    @staticmethod
    def withdraw(origin: str, amount: int) -> AccountResponse:
        try:
            balance = account_repository.withdraw(origin, amount)
            return WithdrawResponse(
                                    origin={"id": origin, "balance": balance}
            )
        except ValueError:
            raise