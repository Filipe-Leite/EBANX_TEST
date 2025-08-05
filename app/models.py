from pydantic import BaseModel

class Event(BaseModel):
    type: str
    amount: int
    origin: str | None = None
    destination: str | None = None

class AccountResponse(BaseModel):
    id: str
    balance: int

class WithdrawResponse(BaseModel):
    origin: AccountResponse

class DepositResponse(BaseModel):
    destination: AccountResponse

class TransferResponse(BaseModel):
    origin: AccountResponse
    destination: AccountResponse