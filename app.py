from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from typing import List, Optional

class Bank(BaseModel):
    name: str
    address: str
    email: EmailStr
    account_number: int
    balance: float
    is_active: bool
    type_of_account: str

class BankUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    email: Optional[EmailStr] = None
    account_number: Optional[int] = None
    balance: Optional[float] = None
    is_active: Optional[bool] = None
    type_of_account: Optional[str] = None

app = FastAPI()

banks = [
    Bank(
        name="john doe",
        address="123 Example Street",
        email="johndoe@example.com",
        account_number=123456789,
        balance=1000.0,
        is_active=True,
        type_of_account="savings"
    ),
    Bank(
        name="mark smith",
        address="456 Example Avenue",
        email="marksmith@example.com",
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
def update_bank_partial(account_number: int, bank: BankUpdate):
    for b in banks:
        if b.account_number == account_number:
            if bank.name is not None:
                b.name = bank.name
            if bank.address is not None:
                b.address = bank.address
            if bank.email is not None:
                b.email = bank.email
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