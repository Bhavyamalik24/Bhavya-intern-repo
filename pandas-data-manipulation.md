# Data Manipulation with Pandas

## What I Did

Loaded a simulated Focus Bear user dataset (20 users, 7 columns) from a
CSV file and practised filtering, sorting, grouping, cleaning, and
pivoting data using Pandas.

### Dataset
`focus_bear_users.csv` contains:
- user_id, name, membership (free/premium)
- days_active, habits_completed, focus_minutes
- last_login

The dataset intentionally contained 3 missing values across
habits_completed, focus_minutes, and last_login columns.

---

### Key Operations Performed

**Loading data:**
```python
df = pd.read_csv("focus_bear_users.csv")
```

**Filtering:**
```python
premium_users = df[df["membership"] == "premium"]
high_performers = df[df["habits_completed"] > 10]
```

**Sorting:**
```python
top_focus = df.sort_values("focus_minutes", ascending=False).head(5)
```

**Groupby aggregation:**
```python
grouped = df.groupby("membership")[["days_active", "habits_completed",
         "focus_minutes"]].mean().round(2)
```

**Handling missing data:**
```python
df["habits_completed"] = df["habits_completed"].fillna(0)
df["focus_minutes"] = df["focus_minutes"].fillna(avg_focus)
df = df.dropna(subset=["last_login"])
```

**Pivot table:**
```python
pivot = df.pivot_table(values="focus_minutes",
        index="membership", aggfunc=["mean", "min", "max"])
```

---

### Key Findings
- Premium users average significantly more focus minutes and habits
  completed than free users
- Top 5 users by focus minutes were all premium members
- After cleaning, no missing values remained in the dataset

---

## Reflection

### What are the advantages of using Pandas for data manipulation?
Pandas makes working with tabular data fast, readable, and powerful.
Instead of writing loops to filter or aggregate data manually, Pandas
provides methods like `groupby`, `sort_values`, and `pivot_table` that
perform complex operations in a single line. It also handles large
datasets efficiently and integrates directly with visualization libraries
like Matplotlib and Seaborn, making it the core tool for the entire
data analytics workflow — from raw data to insight to chart.

### How do you filter and aggregate data in Pandas?
Filtering uses boolean indexing — you pass a condition inside square
brackets and Pandas returns only the rows where the condition is True:
```python
df[df["membership"] == "premium"]
```

Aggregation uses `groupby` to split the data into groups, then applies
a function like `mean`, `sum`, or `count` to each group:
```python
df.groupby("membership")["focus_minutes"].mean()
```

Pivot tables extend this further by allowing multiple aggregation
functions and restructuring the output into a more readable format.

### What techniques help handle missing or incorrect data?
- `df.isnull().sum()` — identifies which columns have missing values
  and how many
- `fillna(value)` — replaces missing values with a specified value,
  such as 0 for habits_completed or the column average for focus_minutes
- `dropna(subset=["column"])` — removes rows where a specific column
  is missing, used for last_login since a missing date makes the row
  unreliable for time-based analysis
- `replace(old, new)` — replaces specific incorrect values with
  correct ones, useful for fixing typos or inconsistent categories

The choice between fillna and dropna depends on the context — filling
is better when you can make a reasonable assumption about the missing
value, while dropping is better when the missing data makes the entire
row unreliable.

### How would Pandas be useful for analysing Focus Bear's user activity data?
Focus Bear's database likely contains tables for users, sessions, habits,
and feature interactions. Pandas would be useful for:

- **Retention analysis:** Filter users by signup date, group by cohort,
  and calculate what percentage remain active after 7, 14, and 30 days
- **Feature usage:** Group session data by feature and aggregate usage
  counts to identify which features drive the most engagement
- **Habit completion rates:** Calculate the average completion rate per
  habit type and identify which habits users abandon most often
- **User segmentation:** Filter and compare free vs premium users across
  key metrics like focus minutes, habit streaks, and session frequency
- **Data cleaning:** Real user data always has missing values, duplicates,
  and inconsistencies — Pandas fillna, dropna, and replace methods would
  be essential before any analysis or visualization is produced

In the context of my internship, these are exactly the kinds of analyses
I would be expected to run on real Focus Bear data to surface actionable
insights for the product team.
