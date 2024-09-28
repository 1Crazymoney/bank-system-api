from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

class Bank(BaseModel):
    name: str
    address: str
    account_number: int
    balance: float
    is_active: bool
    type_of_account: str

app = FastAPI()

# In-memory storage for banks
banks = [
    Bank(
        name="Bank of Example",
        address="123 Example Street",
        account_number=123456789,
        balance=1000.0,
        is_active=True,
        type_of_account="savings"
    ),
    Bank(
        name="Example National Bank",
        address="456 Example Avenue",
        account_number=987654321,
        balance=2500.5,
        is_active=True,
        type_of_account="joint"
    )
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/banks", response_model=List[Bank])
def get_banks():
    return banks

@app.post("/banks", response_model=Bank)
def create_bank(bank: Bank):
    banks.append(bank)
    return bank

@app.patch("/banks/{account_number}", response_model=Bank)
def update_bank_partial(account_number: int, bank: Bank):
    for b in banks:
        if b.account_number == account_number:
            if bank.name is not None:
                b.name = bank.name
            if bank.address is not None:
                b.address = bank.address
            if bank.balance is not None:
                b.balance = bank.balance
            if bank.is_active is not None:
                b.is_active = bank.is_active
            if bank.type_of_account is not None:
                b.type_of_account = bank.type_of_account
            return b
    raise HTTPException(status_code=404, detail="Bank not found")

@app.put("/banks/{account_number}", response_model=Bank)
def update_bank(account_number: int, bank: Bank):
    for i, b in enumerate(banks):
        if b.account_number == account_number:
            banks[i] = bank
            return bank
    raise HTTPException(status_code=404, detail="Bank not found")

@app.delete("/banks/{account_number}", response_model=Bank)
def delete_bank(account_number: int):
    for i, b in enumerate(banks):
        if b.account_number == account_number:
            return banks.pop(i)
    raise HTTPException(status_code=404, detail="Bank not found")

@app.put("/banks/{account_number}/deposit", response_model=Bank)
def deposit(account_number: int, amount: float = Query(...)):
    for b in banks:
        if b.account_number == account_number:
            b.balance += amount
            return b
    raise HTTPException(status_code=404, detail="Bank not found")

@app.put("/banks/{account_number}/withdraw", response_model=Bank)
def withdraw(account_number: int, amount: float = Query(...)):
    for b in banks:
        if b.account_number == account_number:
            if b.balance < amount:
                raise HTTPException(status_code=400, detail="Insufficient funds")
            b.balance -= amount
            return b
    raise HTTPException(status_code=404, detail="Bank not found")

@app.get("/banks/{account_number}", response_model=Bank)
def get_bank(account_number: int):
    for b in banks:
        if b.account_number == account_number:
            return b
    raise HTTPException(status_code=404, detail="Bank not found")