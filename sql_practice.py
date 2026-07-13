import sqlite3
import pandas as pd

# Create an in-memory database
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# Create tables
cursor.executescript("""
    CREATE TABLE users (
        user_id INTEGER PRIMARY KEY,
        name TEXT,
        membership TEXT,
        signup_date TEXT,
        country TEXT
    );

    CREATE TABLE sessions (
        session_id INTEGER PRIMARY KEY,
        user_id INTEGER,
        focus_minutes INTEGER,
        habits_completed INTEGER,
        session_date TEXT,
        feature_used TEXT
    );

    INSERT INTO users VALUES
    (1, 'Alice', 'premium', '2024-01-01', 'Australia'),
    (2, 'Bob', 'free', '2024-01-05', 'USA'),
    (3, 'Carol', 'premium', '2024-01-03', 'Australia'),
    (4, 'Dave', 'free', '2024-01-10', 'UK'),
    (5, 'Eve', 'premium', '2024-01-02', 'Australia'),
    (6, 'Frank', 'free', '2024-01-08', 'USA'),
    (7, 'Grace', 'premium', '2024-01-04', 'Canada'),
    (8, 'Henry', 'free', '2024-01-12', 'UK');

    INSERT INTO sessions VALUES
    (1, 1, 90, 5, '2024-01-15', 'focus_mode'),
    (2, 2, 20, 1, '2024-01-15', 'habits'),
    (3, 3, 85, 4, '2024-01-15', 'focus_mode'),
    (4, 4, 15, 0, '2024-01-15', 'habits'),
    (5, 5, 120, 6, '2024-01-15', 'focus_mode'),
    (6, 6, 30, 2, '2024-01-15', 'breaks'),
    (7, 7, 95, 5, '2024-01-14', 'focus_mode'),
    (8, 8, 10, 0, '2024-01-14', 'habits'),
    (9, 1, 80, 4, '2024-01-14', 'focus_mode'),
    (10, 3, 75, 3, '2024-01-14', 'breaks');
""")

# ---- SELECT ----
print("=== ALL USERS ===")
df = pd.read_sql("SELECT * FROM users", conn)
print(df)

# ---- WHERE ----
print("\n=== PREMIUM USERS ONLY ===")
df = pd.read_sql("""
    SELECT name, membership, country
    FROM users
    WHERE membership = 'premium'
""", conn)
print(df)

# ---- ORDER BY ----
print("\n=== SESSIONS ORDERED BY FOCUS MINUTES ===")
df = pd.read_sql("""
    SELECT session_id, user_id, focus_minutes, habits_completed
    FROM sessions
    ORDER BY focus_minutes DESC
""", conn)
print(df)

# ---- WHERE + ORDER BY ----
print("\n=== SESSIONS WITH MORE THAN 60 FOCUS MINUTES ===")
df = pd.read_sql("""
    SELECT session_id, user_id, focus_minutes, feature_used
    FROM sessions
    WHERE focus_minutes > 60
    ORDER BY focus_minutes DESC
""", conn)
print(df)

# ---- GROUP BY ----
print("\n=== AVERAGE FOCUS MINUTES BY MEMBERSHIP ===")
df = pd.read_sql("""
    SELECT u.membership,
           COUNT(s.session_id) as total_sessions,
           AVG(s.focus_minutes) as avg_focus_minutes,
           AVG(s.habits_completed) as avg_habits
    FROM sessions s
    JOIN users u ON s.user_id = u.user_id
    GROUP BY u.membership
""", conn)
print(df)

# ---- HAVING ----
print("\n=== USERS WITH AVERAGE FOCUS MINUTES ABOVE 70 ===")
df = pd.read_sql("""
    SELECT user_id,
           AVG(focus_minutes) as avg_focus,
           COUNT(session_id) as total_sessions
    FROM sessions
    GROUP BY user_id
    HAVING AVG(focus_minutes) > 70
    ORDER BY avg_focus DESC
""", conn)
print(df)

# ---- JOIN ----
print("\n=== FULL USER SESSION REPORT ===")
df = pd.read_sql("""
    SELECT u.name, u.membership, u.country,
           s.focus_minutes, s.habits_completed,
           s.feature_used, s.session_date
    FROM users u
    JOIN sessions s ON u.user_id = s.user_id
    ORDER BY s.focus_minutes DESC
""", conn)
print(df)

conn.close()
print("\nSQL practice complete!")