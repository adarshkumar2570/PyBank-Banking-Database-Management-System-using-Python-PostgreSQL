import psycopg2
#imports the psycopg2 library, which is used to connect to a PostgreSQL database and execute SQL commands.

def connect():
    conn = psycopg2.connect(dbname='pybank',user='postgres',password='your_postgresql_password',host='localhost',port='5432')
    print("Connected to the database successfully")
#this function establishes a connection to the PostgreSQL database named 'pybank' using the provided credentials and prints a success message.
connect()

def create_table():
    conn = psycopg2.connect(dbname='pybank',user='postgres',password='your_postgresql_password',host='localhost',port='5432')

    cursor = conn.cursor()
    cursor.execute('''create table bank_accounts(bank_account int,account_holder_name text,pin int,account_balance float);''')
    print('Table created successfully')

    conn.commit()
    conn.close()
#this function creates a new table named 'bank_accounts' in the 'pybank' database with four columns: 'bank_account' (integer), 'account_holder_name' (text), 'pin' (integer), and 'account_balance' (float). 
# It then commits the changes to the database and closes the connection.
create_table()

def account_holder_a():
    conn = psycopg2.connect(dbname='pybank',user='postgres',password='your_postgresql_password',host='localhost',port='5432')

    cursor = conn.cursor()
    cursor.execute('''insert into bank_accounts(bank_account,account_holder_name,pin,account_balance) values (12456,'John Doe',1234,11500.0);''')
    print('Account holder A added successfully')

    conn.commit()
    conn.close()
#adds the data of account holder A into the table
account_holder_a()

def account_holder_b():
    conn = psycopg2.connect(dbname='pybank',user='postgres',password='your_postgresql_password',host='localhost',port='5432')

    cursor = conn.cursor()
    cursor.execute('''insert into bank_accounts(bank_account,account_holder_name,pin,account_balance) values (789101,'Joseph',7891,19999.99);''')
    print('Account holder B added successfully')

    conn.commit()
    conn.close()
#adds the data of account holder B into the table
account_holder_b()

def account_holder_c():
    conn = psycopg2.connect(dbname='pybank',user='postgres',password='your_postgresql_password',host='localhost',port='5432')

    cursor = conn.cursor()
    cursor.execute('''insert into bank_accounts(bank_account,account_holder_name,pin,account_balance) values (101112,'Adam',1011,8687.50);''')
    print('Account holder C added successfully')

    conn.commit()
    conn.close()
#adds the data of account holder C into the table
account_holder_c()

def account_holder_d():
    conn = psycopg2.connect(dbname='pybank',user='postgres',password='your_postgresql_password',host='localhost',port='5432')

    cursor = conn.cursor()
    cursor.execute('''insert into bank_accounts(bank_account,account_holder_name,pin,account_balance) values (121314,'Alex',1213,17650.57);''')
    print('Account holder D added successfully')

    conn.commit()
    conn.close()
#adds the data of account holder d into the table
account_holder_d()


def account_holder_e():
    conn = psycopg2.connect(dbname='pybank',user='postgres',password='your_postgresql_password',host='localhost',port='5432')

    cursor = conn.cursor()
    cursor.execute('''insert into bank_accounts(bank_account,account_holder_name,pin,account_balance) values (151617,'Emily',1516,25000.00);''')
    print('Account holder E added successfully')

    conn.commit()
    conn.close()
#adds the data of account holder E into the table
account_holder_e()

print("All account holders added successfully")

def account_holder_info():
    conn = psycopg2.connect(dbname='pybank',user='postgres',password='your_postgresql_password',host='localhost',port='5432')

    cursor = conn.cursor()
    cursor.execute('''select * from bank_accounts;''')
    show = cursor.fetchall()
    for i in show:
        print(i)    
        
    conn.commit()
    conn.close()
# retrieves the information of all account holders from the 'bank_accounts' table and prints it to the console. 
# It establishes a connection to the database, executes a SELECT query to fetch all records, and then iterates through the results to display each account holder's information. Finally, it commits any changes (if necessary) and closes the connection.
account_holder_info()
print("All account holders' information retrieved successfully")
