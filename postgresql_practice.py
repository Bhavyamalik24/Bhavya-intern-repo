import sqlite3
import pandas as pd

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

    CREATE TABLE habits (
        habit_id INTEGER PRIMARY KEY,
        user_id INTEGER,
        habit_name TEXT,
        completed INTEGER,
        habit_date TEXT
    );

    INSERT INTO users VALUES
    (1, 'Alice', 'premium', '2024-01-01', 'Australia'),
    (2, 'Bob', 'free', '2024-01-05', 'USA'),
    (3, 'Carol', 'premium', '2024-01-03', 'Australia'),
    (4, 'Dave', 'free', '2024-01-10', 'UK'),
    (5, 'Eve', 'premium', '2024-01-02', 'Australia');

    INSERT INTO sessions VALUES
    (1, 1, 90, 5, '2024-01-15', 'focus_mode'),
    (2, 2, 20, 1, '2024-01-15', 'habits'),
    (3, 3, 85, 4, '2024-01-15', 'focus_mode'),
    (4, 4, 15, 0, '2024-01-15', 'habits'),
    (5, 5, 120, 6, '2024-01-15', 'focus_mode'),
    (6, 1, 80, 4, '2024-01-14', 'focus_mode'),
    (7, 3, 75, 3, '2024-01-14', 'breaks'),
    (8, 2, 30, 2, '2024-01-14', 'habits');

    INSERT INTO habits VALUES
    (1, 1, 'Morning Meditation', 1, '2024-01-15'),
    (2, 1, 'Exercise', 1, '2024-01-15'),
    (3, 2, 'Morning Meditation', 0, '2024-01-15'),
    (4, 3, 'Exercise', 1, '2024-01-15'),
    (5, 3, 'Reading', 1, '2024-01-15'),
    (6, 4, 'Morning Meditation', 0, '2024-01-15'),
    (7, 5, 'Exercise', 1, '2024-01-15'),
    (8, 5, 'Morning Meditation', 1, '2024-01-15');
""")

# ---- JOIN ----
print("=== JOIN: Full User Session Report ===")
df = pd.read_sql("""
    SELECT u.name, u.membership, u.country,
           s.focus_minutes, s.habits_completed,
           s.feature_used, s.session_date
    FROM users u
    JOIN sessions s ON u.user_id = s.user_id
    ORDER BY s.focus_minutes DESC
""", conn)
print(df)

# ---- CASE STATEMENT ----
print("\n=== CASE: User Engagement Level ===")
df = pd.read_sql("""
    SELECT u.name, u.membership,
           AVG(s.focus_minutes) as avg_focus,
           CASE
               WHEN AVG(s.focus_minutes) >= 80 THEN 'High Engagement'
               WHEN AVG(s.focus_minutes) >= 40 THEN 'Medium Engagement'
               ELSE 'Low Engagement'
           END as engagement_level
    FROM users u
    JOIN sessions s ON u.user_id = s.user_id
    GROUP BY u.user_id, u.name, u.membership
    ORDER BY avg_focus DESC
""", conn)
print(df)

# ---- WINDOW FUNCTION (SQLite supports basic ones) ----
print("\n=== WINDOW FUNCTION: Running Total of Focus Minutes ===")
df = pd.read_sql("""
    SELECT user_id, session_date, focus_minutes,
           SUM(focus_minutes) OVER (
               PARTITION BY user_id
               ORDER BY session_date
           ) as running_total_focus
    FROM sessions
    ORDER BY user_id, session_date
""", conn)
print(df)

# ---- MULTIPLE JOIN ----
print("\n=== MULTI-JOIN: Users + Sessions + Habits ===")
df = pd.read_sql("""
    SELECT u.name, u.membership,
           s.focus_minutes,
           h.habit_name,
           CASE WHEN h.completed = 1 THEN 'Yes' ELSE 'No' END as completed
    FROM users u
    JOIN sessions s ON u.user_id = s.user_id
    JOIN habits h ON u.user_id = h.user_id
    WHERE s.session_date = '2024-01-15'
    ORDER BY u.name
""", conn)
print(df)

# ---- EXPLAIN ANALYZE equivalent ----
print("\n=== QUERY PLAN (SQLite EXPLAIN) ===")
cursor.execute("""
    EXPLAIN QUERY PLAN
    SELECT u.name, AVG(s.focus_minutes)
    FROM users u
    JOIN sessions s ON u.user_id = s.user_id
    GROUP BY u.user_id
""")
for row in cursor.fetchall():
    print(row)

conn.close()
print("\nPostgreSQL practice complete!")