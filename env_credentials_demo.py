import os
from dotenv import load_dotenv
import sqlite3
import pandas as pd

# Load environment variables from .env file
load_dotenv()

# Read credentials from environment variables
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_port = os.getenv("DB_PORT")

print("=== Credentials loaded from .env ===")
print(f"Host: {db_host}")
print(f"Database: {db_name}")
print(f"User: {db_user}")
print(f"Password: {'*' * len(db_password)}")
print(f"Port: {db_port}")

# In real Focus Bear work this would be:
# import psycopg
# conn = psycopg.connect(
#     host=db_host,
#     dbname=db_name,
#     user=db_user,
#     password=db_password,
#     port=db_port
# )

# For demo, use SQLite
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.executescript("""
    CREATE TABLE users (
        user_id INTEGER PRIMARY KEY,
        name TEXT,
        membership TEXT
    );
    INSERT INTO users VALUES
    (1, 'Alice', 'premium'),
    (2, 'Bob', 'free'),
    (3, 'Carol', 'premium');
""")

print("\n=== Query result using secure connection ===")
df = pd.read_sql("SELECT * FROM users", conn)
print(df)

conn.close()
print("\nCredentials loaded and used securely!")