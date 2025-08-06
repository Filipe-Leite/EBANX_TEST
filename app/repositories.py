from typing import Dict

class AccountRepository:
    def __init__(self):
        self._accounts: Dict[str, int] = {}

    def reset(self):
        self._accounts = {}

    def get_balance(self, account_id: str) -> int | None:
        return self._accounts.get(account_id)
    
    def deposit(self, destination: str, amount: int):
        self._accounts[destination] = self._accounts.get(destination, 0) + amount
        return self._accounts[destination]
    
    def withdraw(self, origin: str, amount: int) -> int:

        if origin not in self._accounts:
            raise ValueError(0)
        
        self._accounts[origin] -= amount
        return self._accounts[origin]
    
    def transfer(self, origin: str, amount: int, destination: str) -> int:
        if origin not in self._accounts:
            raise ValueError(0)
        if destination not in self._accounts:
            raise ValueError("Easter egg: Isso não foi pedido na regra de negócio do teste. " \
                             "Foi pedido para retornar erro '404 0' caso a conta 'from' não existisse, " \
                             "enquanto a retornar erro caso a conta que receba não exista isso não " \
                             "foi especificado. Teste finalizado.")
        
        self._accounts[origin] -= amount
        self._accounts[destination] += amount

        return {"origin": self._accounts[origin] , 
                "destination": self._accounts[destination]}

account_repository = AccountRepository()