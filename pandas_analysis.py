import pandas as pd

# ---- LOAD DATA ----
df = pd.read_csv("focus_bear_users.csv")
print("=== RAW DATA ===")
print(df)
print(f"\nShape: {df.shape}")
print(f"\nData types:\n{df.dtypes}")
print(f"\nMissing values:\n{df.isnull().sum()}")

# ---- FILTERING ----
print("\n=== PREMIUM USERS ONLY ===")
premium_users = df[df["membership"] == "premium"]
print(premium_users[["name", "days_active", "focus_minutes"]])

print("\n=== USERS WITH MORE THAN 10 HABITS COMPLETED ===")
high_performers = df[df["habits_completed"] > 10]
print(high_performers[["name", "membership", "habits_completed"]])

# ---- SORTING ----
print("\n=== TOP 5 USERS BY FOCUS MINUTES ===")
top_focus = df.sort_values("focus_minutes", ascending=False).head(5)
print(top_focus[["name", "membership", "focus_minutes"]])

# ---- GROUPBY ----
print("\n=== AVERAGE STATS BY MEMBERSHIP TYPE ===")
grouped = df.groupby("membership")[["days_active", "habits_completed", "focus_minutes"]].mean().round(2)
print(grouped)

# ---- HANDLING MISSING DATA ----
print("\n=== MISSING VALUES BEFORE CLEANING ===")
print(df.isnull().sum())

# Fill missing habits_completed with 0
df["habits_completed"] = df["habits_completed"].fillna(0)

# Fill missing focus_minutes with the average
avg_focus = df["focus_minutes"].mean()
df["focus_minutes"] = df["focus_minutes"].fillna(avg_focus)

# Drop rows where last_login is missing
df = df.dropna(subset=["last_login"])

print("\n=== MISSING VALUES AFTER CLEANING ===")
print(df.isnull().sum())

# ---- PIVOT TABLE ----
print("\n=== PIVOT TABLE: AVERAGE FOCUS MINUTES BY MEMBERSHIP ===")
pivot = df.pivot_table(
    values="focus_minutes",
    index="membership",
    aggfunc=["mean", "min", "max"]
).round(2)
print(pivot)

print("\nAnalysis complete!")