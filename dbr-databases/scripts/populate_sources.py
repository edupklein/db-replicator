import mysql.connector
from faker import Faker
from tqdm import tqdm
import random

# MySQL Connection info
conn1 = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root1',
    database='db1'
)
conn2 = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root2',
    database='db2'
)
cursor1 = conn1.cursor()
cursor2 = conn2.cursor()

fake = Faker('en_US')

# Total quantity of records to be created
total_clients = 500_000
total_users = 500_000
batch_size = 5000

# ========================
# Inserting CLIENTS
# ========================
print("Inserting fake clients...")

for _ in tqdm(range(total_clients // batch_size)):
    data = []
    for _ in range(batch_size):
        name = fake.name()
        email = fake.email()
        phone = fake.phone_number()
        city = fake.city()
        state = fake.state_sigla()
        creation_date = fake.date_time_between(start_date='-2y', end_date='now')
        data.append((name, email, phone, city, state, creation_date))

    cursor1.executemany("""
        INSERT INTO clients (name, email, phone, city, state, creation_date)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, data)
    conn1.commit()

for _ in tqdm(range(total_clients // batch_size)):
    data = []
    for _ in range(batch_size):
        name = fake.name()
        email = fake.email()
        phone = fake.phone_number()
        city = fake.city()
        state = fake.state_sigla()
        creation_date = fake.date_time_between(start_date='-2y', end_date='now')
        data.append((name, email, phone, city, state, creation_date))

    cursor2.executemany("""
        INSERT INTO clients (name, email, phone, city, state, creation_date)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, data)
    conn2.commit()

# ========================
# Inserting USERS
# ========================
print("Inserting fake users...")

for _ in tqdm(range(total_users // batch_size)):
    data = []
    for _ in range(batch_size):
        username = fake.user_name()
        email = fake.email()
        password = fake.password(length=12)
        creation_date = fake.date_time_between(start_date='-2y', end_date='now')
        data.append((username, email, password, creation_date))

    cursor1.executemany("""
        INSERT INTO users (username, email, password, creation_date)
        VALUES (%s, %s, %s, %s)
    """, data)
    conn1.commit()

for _ in tqdm(range(total_users // batch_size)):
    data = []
    for _ in range(batch_size):
        username = fake.user_name()
        email = fake.email()
        password = fake.password(length=12)
        creation_date = fake.date_time_between(start_date='-2y', end_date='now')
        data.append((username, email, password, creation_date))

    cursor2.executemany("""
        INSERT INTO users (username, email, password, creation_date)
        VALUES (%s, %s, %s, %s)
    """, data)
    conn2.commit()

cursor1.close()
conn1.close()

cursor2.close()
conn2.close()

print("Insertion completed!")
