import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

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
    (5, 'Eve', 'premium', '2024-01-02', 'Australia'),
    (6, 'Frank', 'free', '2024-01-08', 'USA'),
    (7, 'Grace', 'premium', '2024-01-04', 'Canada'),
    (8, 'Henry', 'free', '2024-01-12', 'UK');

    INSERT INTO sessions VALUES
    (1, 1, 90, 5, '2024-01-13', 'focus_mode'),
    (2, 2, 20, 1, '2024-01-13', 'habits'),
    (3, 3, 85, 4, '2024-01-13', 'focus_mode'),
    (4, 4, 15, 0, '2024-01-13', 'habits'),
    (5, 5, 120, 6, '2024-01-14', 'focus_mode'),
    (6, 6, 30, 2, '2024-01-14', 'breaks'),
    (7, 7, 95, 5, '2024-01-14', 'focus_mode'),
    (8, 8, 10, 0, '2024-01-14', 'habits'),
    (9, 1, 80, 4, '2024-01-15', 'focus_mode'),
    (10, 3, 75, 3, '2024-01-15', 'breaks'),
    (11, 5, 110, 5, '2024-01-15', 'focus_mode'),
    (12, 7, 100, 6, '2024-01-15', 'focus_mode');

    INSERT INTO habits VALUES
    (1, 1, 'Morning Meditation', 1, '2024-01-15'),
    (2, 1, 'Exercise', 1, '2024-01-15'),
    (3, 2, 'Morning Meditation', 0, '2024-01-15'),
    (4, 3, 'Exercise', 1, '2024-01-15'),
    (5, 3, 'Reading', 1, '2024-01-15'),
    (6, 4, 'Morning Meditation', 0, '2024-01-15'),
    (7, 5, 'Exercise', 1, '2024-01-15'),
    (8, 5, 'Morning Meditation', 1, '2024-01-15'),
    (9, 6, 'Reading', 0, '2024-01-15'),
    (10, 7, 'Exercise', 1, '2024-01-15'),
    (11, 7, 'Morning Meditation', 1, '2024-01-15'),
    (12, 8, 'Exercise', 0, '2024-01-15');
""")

# ---- INSIGHT 1: User engagement summary ----
print("=== Insight 1: User Engagement Summary ===")
df_engagement = pd.read_sql("""
    SELECT u.name, u.membership, u.country,
           COUNT(s.session_id) as total_sessions,
           AVG(s.focus_minutes) as avg_focus,
           SUM(s.habits_completed) as total_habits
    FROM users u
    JOIN sessions s ON u.user_id = s.user_id
    GROUP BY u.user_id, u.name, u.membership, u.country
    ORDER BY avg_focus DESC
""", conn)
print(df_engagement)

# ---- PANDAS: Add engagement score ----
df_engagement["engagement_score"] = (
    df_engagement["avg_focus"] * 0.6 +
    df_engagement["total_habits"] * 2 +
    df_engagement["total_sessions"] * 5
).round(2)
df_engagement["tier"] = df_engagement["engagement_score"].apply(
    lambda x: "Champion" if x >= 80 else "Active" if x >= 50 else "At Risk"
)
print("\n=== Pandas: Engagement Score & Tier ===")
print(df_engagement[["name", "membership", "engagement_score", "tier"]])

# ---- INSIGHT 2: Daily trend ----
print("\n=== Insight 2: Daily Focus Trend ===")
df_daily = pd.read_sql("""
    SELECT session_date,
           COUNT(session_id) as sessions,
           AVG(focus_minutes) as avg_focus,
           SUM(habits_completed) as total_habits
    FROM sessions
    GROUP BY session_date
    ORDER BY session_date
""", conn)
df_daily["session_date"] = pd.to_datetime(df_daily["session_date"])
print(df_daily)

# ---- INSIGHT 3: Habit completion rate ----
print("\n=== Insight 3: Habit Completion Rate ===")
df_habits = pd.read_sql("""
    SELECT habit_name,
           COUNT(*) as total,
           SUM(completed) as completed,
           ROUND(SUM(completed) * 100.0 / COUNT(*), 1) as completion_rate
    FROM habits
    GROUP BY habit_name
    ORDER BY completion_rate DESC
""", conn)
print(df_habits)

# ---- INSIGHT 4: Country analysis ----
print("\n=== Insight 4: Engagement by Country ===")
df_country = pd.read_sql("""
    SELECT u.country,
           COUNT(DISTINCT u.user_id) as total_users,
           AVG(s.focus_minutes) as avg_focus
    FROM users u
    JOIN sessions s ON u.user_id = s.user_id
    GROUP BY u.country
    ORDER BY avg_focus DESC
""", conn)
print(df_country)

# ---- VISUALIZATIONS ----
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Focus Bear Analytics Dashboard", fontsize=16)

# Chart 1: Engagement score by user
axes[0, 0].barh(
    df_engagement["name"],
    df_engagement["engagement_score"],
    color=df_engagement["tier"].map({
        "Champion": "#2ecc71",
        "Active": "#f39c12",
        "At Risk": "#e74c3c"
    })
)
axes[0, 0].set_title("User Engagement Scores")
axes[0, 0].set_xlabel("Score")

# Chart 2: Daily focus trend
axes[0, 1].plot(
    df_daily["session_date"],
    df_daily["avg_focus"],
    marker="o", color="blue", linewidth=2
)
axes[0, 1].set_title("Daily Average Focus Minutes")
axes[0, 1].set_xlabel("Date")
axes[0, 1].set_ylabel("Minutes")

# Chart 3: Habit completion rates
axes[1, 0].bar(
    df_habits["habit_name"],
    df_habits["completion_rate"],
    color=["#3498db", "#9b59b6", "#1abc9c"]
)
axes[1, 0].set_title("Habit Completion Rates (%)")
axes[1, 0].set_ylabel("Completion %")

# Chart 4: Average focus by country
axes[1, 1].bar(
    df_country["country"],
    df_country["avg_focus"],
    color="#e67e22"
)
axes[1, 1].set_title("Average Focus Minutes by Country")
axes[1, 1].set_ylabel("Minutes")

plt.tight_layout()
plt.savefig("analytics_dashboard.png")
plt.show()
print("\nDashboard saved as analytics_dashboard.png")

conn.close()
print("Analysis complete!")