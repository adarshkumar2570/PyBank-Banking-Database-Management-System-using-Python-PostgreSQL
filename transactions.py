import psycopg2
#imports the psycopg2 library, which is used to connect to a PostgreSQL database and execute SQL commands.

import random
# imports the random library, which is used to generate random numbers, such as transaction IDs in this case.

conn = psycopg2.connect(dbname='pybank',user='postgres',password='your_postgresql_password',host='localhost',port='5432')
cursor = conn.cursor()
print("Connected to the database successfully")
#this function establishes a connection to the PostgreSQL database named 'pybank' using the provided credentials and prints a success message.

bank_acc = int(input("Enter the bank account number: "))
pin = int(input("Enter the pin: "))
# Prompts the user to enter their bank account number and PIN, which are stored in the variables 'bank_acc' and 'pin' respectively.

query = '''SELECT bank_account FROM bank_accounts WHERE bank_account = %s AND pin = %s;'''
cursor.execute(query, (bank_acc, pin))

user = cursor.fetchone()

if user:
    print("Login successful")
# Login authentication: Executes a SQL query to check if the provided bank account number and PIN match any record in the 'bank_accounts' table.
# If a match is found, it prints "Login successful".
  
    print("What transaction would you like to perform?")
    print("1. Deposit" ,"\n2. Withdraw", "\n3. Check Balance")
    
    choice = input("Enter your choice: ")
# The user is presented with a menu of transaction options (Deposit, Withdraw, Check Balance) and prompted to enter their choice, which is stored in the variable 'choice'.

    if choice == '1':
        amount = float(input("Enter amount to deposit: "))

        deposit_query = '''UPDATE bank_accounts SET account_balance = account_balance + %s WHERE bank_account = %s;'''
        cursor.execute(deposit_query, (amount, bank_acc))

        conn.commit()
        conn.close()

        print("Deposit successful")
        print(f"Transaction ID: {random.randint(100000, 999999)}")
# If the user chooses to deposit, they are prompted to enter the amount to deposit. A SQL query is executed to update the account balance by adding the deposited amount, and a success message is printed.

    elif choice == '2':
        amount = float(input("Enter amount to withdraw: "))

        query = '''SELECT account_balance FROM bank_accounts WHERE bank_account = %s;'''
        cursor.execute(query, (bank_acc,))

        balance = cursor.fetchone()[0]

        if amount > balance :
            print("Insufficient balance")

        else:
            withdraw_query = '''UPDATE bank_accounts SET account_balance = account_balance - %s WHERE bank_account = %s;'''
            cursor.execute(withdraw_query, (amount, bank_acc))

            conn.commit()
            conn.close()
            print("Withdrawal successful")
            print(f"Transaction ID: {random.randint(100000, 999999)}")
# If the user chooses to withdraw, they are prompted to enter the amount to withdraw. The current account balance is retrieved from the database, and if the withdrawal amount exceeds the balance, an "Insufficient balance" message is printed. Otherwise, a SQL query is executed to update the account balance by subtracting the withdrawn amount, and a success message is printed.

    elif choice == '3':
        balance_query = '''SELECT account_balance FROM bank_accounts WHERE bank_account = %s;'''
        cursor.execute(balance_query, (bank_acc,))

        balance = cursor.fetchone()[0]

        conn.commit()
        conn.close()

        print(f"Your account balance is: {balance}")
        print(f"Transaction ID: {random.randint(100000, 999999)}")

    else:
        print("Invalid choice")
# If the user chooses to check their balance, a SQL query is executed to retrieve the current account balance, which is then printed. 
# If the user enters an invalid choice, an "Invalid choice" message is printed.

else:
    print("Invalid bank account number or PIN")
# If the login authentication fails (i.e., no matching record is found for the provided bank account number and PIN), an "Invalid bank account number or PIN" message is printed.

