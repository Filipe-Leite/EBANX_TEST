from fastapi import FastAPI, status

app = FastAPI()

# Reset state before starting tests

@app.post("/reset")
async def reset_state():
    return

# Get balance for non-existing account

@app.get("/balance")
async def get_balance():
    return

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
async def create_account_or_deposit_account():
    return

# Get balance for existing account

@app.post("/balance")
async def create_account_or_deposit_account():
    return