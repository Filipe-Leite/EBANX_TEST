from fastapi import FastAPI, status,HTTPException
from fastapi.responses import Response,PlainTextResponse
from app.repositories import account_repository
from app.models import Event
from app.services import AccountService

app = FastAPI()

# Reset state before starting tests

@app.post("/reset", status_code=status.HTTP_200_OK)
async def reset_state():
    account_repository.reset()
    return Response(content="OK", media_type="text/plain")

# Get balance for existing account
# or
# Get balance for existing account

@app.get("/balance", response_class=PlainTextResponse)
async def get_balance(account_id: str):
    balance = account_repository.get_balance(account_id)
    
    if balance is not None:
        return str(balance) 
    
    return PlainTextResponse(content="0", status_code=status.HTTP_404_NOT_FOUND)


# Create account with initial balance
# or
# Deposit into existing account
# and
# Withdraw from existing account
# or
# Withdraw from non-existing account
# and
# Transfer from existing account
# or
# Transfer from non-existing account

@app.post("/event")
async def handle_event(event: Event):
    try:
        if event.type == "deposit":
            return AccountService.deposit(event.destination, event.amount)
    except ValueError:
        raise HTTPException(status_code=404, detail="0")