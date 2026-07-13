import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# ---- CONNECTION ----
# In real Focus Bear work this would be:
# import psycopg
# conn = psycopg.connect(
#     host="localhost",
#     dbname="focusbear",
#     user="analyst",
#     password="password",
#     port=5432
# )
# For now we use SQLite which uses identical patterns

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# Create and populate tables
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

# ---- QUERY INTO DATAFRAME ----
print("=== Step 1: Load data from database into DataFrame ===")
df = pd.read_sql("""
    SELECT u.name, u.membership, u.country,
           s.focus_minutes, s.habits_completed,
           s.feature_used, s.session_date
    FROM users u
    JOIN sessions s ON u.user_id = s.user_id
""", conn)
print(df)
print(f"\nShape: {df.shape}")
print(f"Data types:\n{df.dtypes}")

# ---- PANDAS TRANSFORMATIONS ----
print("\n=== Step 2: Data Transformations ===")

# Add engagement level column
df["engagement_level"] = df["focus_minutes"].apply(
    lambda x: "High" if x >= 80 else "Medium" if x >= 40 else "Low"
)

# Convert session_date to datetime
df["session_date"] = pd.to_datetime(df["session_date"])

# Add day of week
df["day_of_week"] = df["session_date"].dt.day_name()

print(df[["name", "focus_minutes", "engagement_level", "day_of_week"]])

# ---- AGGREGATION ----
print("\n=== Step 3: Aggregated Report ===")
report = df.groupby("membership").agg(
    total_sessions=("focus_minutes", "count"),
    avg_focus_minutes=("focus_minutes", "mean"),
    avg_habits=("habits_completed", "mean"),
    total_focus=("focus_minutes", "sum")
).round(2)
print(report)

# ---- AUTOMATED REPORT ----
print("\n=== Step 4: Automated Visualization Report ===")
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Chart 1: Average focus by membership
report["avg_focus_minutes"].plot(
    kind="bar", ax=axes[0],
    color=["green", "orange"],
    title="Avg Focus Minutes by Membership"
)
axes[0].set_xlabel("Membership")
axes[0].set_ylabel("Minutes")
axes[0].tick_params(axis='x', rotation=0)

# Chart 2: Engagement level distribution
df["engagement_level"].value_counts().plot(
    kind="pie", ax=axes[1],
    autopct="%1.1f%%",
    title="Engagement Level Distribution",
    colors=["#2ecc71", "#f39c12", "#e74c3c"]
)

plt.tight_layout()
plt.savefig("automated_report.png")
plt.show()
print("Report saved as automated_report.png")

conn.close()
print("\nIntegration complete!")