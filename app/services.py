from .repositories import account_repository
from .models import TransferResponse,DepositResponse,WithdrawResponse

class AccountService:
    @staticmethod
    def deposit(destination: str, amount: int) -> DepositResponse:
        balance = account_repository.deposit(destination, amount)

        return DepositResponse(destination={"id": destination, 
                                            "balance":balance
                                            }
        )
    @staticmethod
    def withdraw(origin: str, amount: int) -> WithdrawResponse:
        try:
            balance = account_repository.withdraw(origin, amount)

            return WithdrawResponse(origin={"id": origin, 
                                            "balance": balance}
            )
        except ValueError:
            raise
    @staticmethod
    def transfer(origin: str, amount: int, destination: str) -> TransferResponse:
        try:
            balance = account_repository.transfer(origin, amount, destination)
            
            return TransferResponse(origin={"id": origin, 
                                            "balance": balance['origin']},
                                 destination={"id":destination,
                                                 "balance": balance['destination']}
            )
        except ValueError:
            raise 