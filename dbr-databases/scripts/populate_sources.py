import mysql.connector
from faker import Faker
from tqdm import tqdm
import random

# MySQL Connection info
conn1 = mysql.connector.connect(
    host='localhost',
    user='root',
    port=3307,
    password='root1',
    database='db1'
)
conn2 = mysql.connector.connect(
    host='localhost',
    user='root',
    port=3308,
    password='root2',
    database='db2'
)
cursor1 = conn1.cursor()
cursor2 = conn2.cursor()

fake = Faker('en_US')

# Total quantity of records to be created
total_client = 12_000_000
total_user = 12_000_000
batch_size = 5000

# ========================
# Inserting clients
# ========================
print("Inserting fake clients...")

for _ in tqdm(range(total_client // batch_size)):
    data = []
    for _ in range(batch_size):
        name = fake.name()
        email = fake.email()
        phone = fake.phone_number()[:20]
        city = fake.city()
        state = fake.state_abbr()
        creation_date = fake.date_time_between(start_date='-2y', end_date='now')
        data.append((name, email, phone, city, state, creation_date))

    cursor1.executemany("""
        INSERT INTO client (name, email, phone, city, state, creation_date)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, data)
    conn1.commit()

for _ in tqdm(range(total_client // batch_size)):
    data = []
    for _ in range(batch_size):
        name = fake.name()
        email = fake.email()
        phone = fake.phone_number()[:20]
        city = fake.city()
        state = fake.state_abbr()
        creation_date = fake.date_time_between(start_date='-2y', end_date='now')
        data.append((name, email, phone, city, state, creation_date))

    cursor2.executemany("""
        INSERT INTO client (name, email, phone, city, state, creation_date)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, data)
    conn2.commit()

# ========================
# Inserting users
# ========================
print("Inserting fake users...")

for _ in tqdm(range(total_user // batch_size)):
    data = []
    for _ in range(batch_size):
        username = fake.user_name()
        email = fake.email()
        password = fake.password(length=12)
        city = fake.city()
        state = fake.state_abbr()
        creation_date = fake.date_time_between(start_date='-2y', end_date='now')
        data.append((username, email, password, city, state, creation_date))

    cursor1.executemany("""
        INSERT INTO user (username, email, password, city, state, creation_date)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, data)
    conn1.commit()

for _ in tqdm(range(total_user // batch_size)):
    data = []
    for _ in range(batch_size):
        username = fake.user_name()
        email = fake.email()
        password = fake.password(length=12)
        city = fake.city()
        state = fake.state_abbr()
        creation_date = fake.date_time_between(start_date='-2y', end_date='now')
        data.append((username, email, password, city, state, creation_date))

    cursor2.executemany("""
        INSERT INTO user (username, email, password, city, state, creation_date)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, data)
    conn2.commit()

cursor1.close()
conn1.close()

cursor2.close()
conn2.close()

print("Insertion completed!")
