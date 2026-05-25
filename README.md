# 🏦 PyBank – Banking Database Management System

PyBank is a beginner-level backend banking application developed using **Python** and **PostgreSQL**.  
The project simulates ATM-like banking operations such as login authentication, deposit, withdrawal, and balance inquiry with real-time database updates.

---

# 📌 Features

## pybank.py
- Connects Python to PostgreSQL
- Creates the `bank_accounts` table
- Inserts sample account holder records
- Retrieves and displays all account holder information

## transactions.py
- User login authentication using:
  - Bank Account Number
  - PIN
- Deposit money
- Withdraw money
- Check account balance
- Real-time database updates
- Generates random transaction IDs

---

# 🛠 Tech Stack

- Python
- PostgreSQL
- SQL
- psycopg2
- VS Code
- Virtual Environment (venv)

---

# 🗂 Project Structure

```bash
Banking/
│
├── pybank.py
├── transactions.py
└── README.md
````

---

# 🗄 Database Schema

## Table: `bank_accounts`

| Column Name         | Data Type |
| ------------------- | --------- |
| bank_account        | INTEGER   |
| account_holder_name | TEXT      |
| pin                 | INTEGER   |
| account_balance     | FLOAT     |

---

# ⚙️ Functionalities

## 🔐 Authentication

Users log in using:

* Bank Account Number
* PIN

---

## 💰 Deposit

* Updates account balance in PostgreSQL database

```sql
UPDATE bank_accounts
SET account_balance = account_balance + amount
WHERE bank_account = account_number;
```

---

## 💸 Withdraw

* Checks available balance
* Prevents overdraft transactions
* Updates balance in real time

```sql
UPDATE bank_accounts
SET account_balance = account_balance - amount
WHERE bank_account = account_number;
```

---

## 📊 Check Balance

Retrieves current balance from database using SQL SELECT query.

---

# ▶️ How to Run the Project

## 1️⃣ Clone Repository

```bash
git clone <your-repository-link>
```

---

## 2️⃣ Navigate to Project Folder

```bash
cd Banking
```

---

## 3️⃣ Create Virtual Environment

```bash
python -m venv env
```

---

## 4️⃣ Activate Virtual Environment

### Windows

```bash
env\Scripts\activate
```

### Mac/Linux

```bash
source env/bin/activate
```

---

## 5️⃣ Install psycopg2

```bash
pip install psycopg2
```

---

## 6️⃣ Run Database Setup Script

```bash
python pybank.py
```

This will:

* Create the table
* Insert sample users
* Display records

---

## 7️⃣ Run ATM Transaction System

```bash
python transactions.py
```

---

# 🖥 Sample Transactions

```text
Enter the bank account number: 12456
Enter the pin: 1234

Login successful

1. Deposit
2. Withdraw
3. Check Balance
```

---

# 📚 Concepts Used

* Python Functions
* PostgreSQL Integration
* SQL Queries
* CRUD Operations
* Authentication Logic
* Database Transactions
* Backend Development
* Financial Data Handling

---

# 📷 Project Environment

* IDE: VS Code
* Database: PostgreSQL
* Python Environment: Virtual Environment (venv)

---

# 👨‍💻 Author

Adarsh Kumar

---

```
```
