from pydantic import BaseModel

class EventRequest(BaseModel):
    type: str
    amount: int | None = None
    origin: str| None = None
    destination: str | None = None

class AccountResponse(BaseModel):
    id: str
    balance: int

class WithdrawResponse(BaseModel):
    origin: AccountResponse

class DepositResponse(BaseModel):
    destination: AccountResponse

class TransferResponse(BaseModel):
    origin: AccountResponse | None = None
    destination: AccountResponse | None = None