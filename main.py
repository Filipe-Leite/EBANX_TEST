from fastapi import FastAPI, status
from fastapi.responses import Response,PlainTextResponse
from app.repositories import account_repository
from app.models import EventRequest
from app.services import AccountService

app = FastAPI()

@app.post("/reset", status_code=status.HTTP_200_OK)
async def reset_state():
    account_repository.reset()
    return Response(content="OK", media_type="text/plain")

@app.get("/balance", response_class=PlainTextResponse)
async def get_balance(account_id: str):
    balance = account_repository.get_balance(account_id)
    
    if balance is not None:
        return str(balance) 
    
    return PlainTextResponse(content="0", status_code=status.HTTP_404_NOT_FOUND)

@app.post("/event", status_code=status.HTTP_200_OK)
async def handle_event(event: EventRequest):

    try:
        if event.type == "deposit":
            return AccountService.deposit(event.destination, event.amount)
        elif event.type == "withdraw":
            return AccountService.withdraw(event.origin, event.amount)
        elif event.type == "transfer":
            return AccountService.transfer(event.origin, event.amount, event.destination)
    except ValueError:
            return PlainTextResponse(
                content="0",
                status_code=status.HTTP_404_NOT_FOUND
            )