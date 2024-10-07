# Bank API

This is a FastAPI-based application that provides a simple banking system. It allows you to manage bank accounts and user accounts with various operations such as creating, updating, deleting, and querying accounts.

## Features

- **Bank Accounts**: Create, read, update, delete, deposit, and withdraw from bank accounts.
- **User Accounts**: Create and query user accounts.
- **CORS Middleware**: Enabled for cross-origin requests.

## Endpoints

### Bank Endpoints

- **Get all banks**
    - `GET /banks`
    - Response: List of all bank accounts.

- **Get bank by email**
    - `GET /banks/email/{email}`
    - Response: List of bank accounts matching the email.

- **Create a new bank**
    - `POST /banks`
    - Request Body: Bank object.
    - Response: Created bank account.

- **Update bank partially**
    - `PATCH /banks/{account_number}`
    - Request Body: BankUpdate object.
    - Response: Updated bank account.

- **Update bank balance**
    - `PATCH /banks/{account_number}/balance`
    - Query Parameter: `amount` (float).
    - Response: Updated bank account with new balance.

- **Replace bank**
    - `PUT /banks/{account_number}`
    - Request Body: Bank object.
    - Response: Replaced bank account.

- **Delete bank**
    - `DELETE /banks/{account_number}`
    - Response: Deleted bank account.

- **Deposit to bank account**
    - `PUT /banks/{account_number}/deposit`
    - Query Parameter: `amount` (float).
    - Response: Updated bank account with new balance after deposit.

- **Withdraw from bank account**
    - `PUT /banks/{account_number}/withdraw`
    - Query Parameter: `amount` (float).
    - Response: Updated bank account with new balance after withdrawal.

- **Get bank by account number**
    - `GET /banks/{account_number}`
    - Response: Bank account matching the account number.

### User Endpoints

- **Create a new user**
    - `POST /user`
    - Request Body: UserAccount object.
    - Response: Created user account.

- **Get all users**
    - `GET /users`
    - Response: List of all user accounts.

- **Get user by email**
    - `GET /users/email/{email}`
    - Response: User account matching the email.

## Models

### Bank

- `name`: str
- `address`: str
- `email`: EmailStr
- `account_number`: int
- `balance`: float
- `is_active`: bool
- `type_of_account`: str

### BankUpdate

- `name`: Optional[str]
- `address`: Optional[str]
- `email`: Optional[EmailStr]
- `account_number`: Optional[int]
- `balance`: Optional[float]
- `is_active`: Optional[bool]
- `type_of_account`: Optional[str]

### UserAccount

- `name`: str
- `email`: EmailStr
- `address`: str

## Setup

1. Clone the repository:
     ```bash
     git clone <repository-url>
     cd bank_api
     ```

2. Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```

3. Run the application:
     ```bash
     uvicorn app:app --reload
     ```

4. Access the API documentation at `http://127.0.0.1:8000/docs`.

## License

This project is licensed under the MIT License.