# Connecting Python & Pandas to a SQL Database

## What I Did

Demonstrated how Python connects to a SQL database, queries data into
a Pandas DataFrame, performs transformations, and generates an automated
visual report — using SQLite as a stand-in for Focus Bear's PostgreSQL
database (the connection pattern is identical).

### Connection Pattern
```python
# SQLite (used for practice)
import sqlite3
conn = sqlite3.connect(":memory:")

# PostgreSQL (real Focus Bear usage with psycopg)
import psycopg
conn = psycopg.connect(
    host="localhost",
    dbname="focusbear",
    user="analyst",
    password="password",
    port=5432
)
```

### Query into DataFrame
```python
df = pd.read_sql("""
    SELECT u.name, u.membership, u.country,
           s.focus_minutes, s.habits_completed,
           s.feature_used, s.session_date
    FROM users u
    JOIN sessions s ON u.user_id = s.user_id
""", conn)
```

### Post-Query Transformations
```python
# Add engagement level column
df["engagement_level"] = df["focus_minutes"].apply(
    lambda x: "High" if x >= 80 else "Medium" if x >= 40 else "Low"
)

# Convert to datetime and extract day of week
df["session_date"] = pd.to_datetime(df["session_date"])
df["day_of_week"] = df["session_date"].dt.day_name()
```

### Automated Report
Generated a two-chart report showing average focus minutes by membership
type and engagement level distribution, saved as `automated_report.png`.

---

## Reflection

### Why is it useful to query databases directly from Python?
Querying databases directly from Python removes the need to manually
export data from a SQL client, save it as a CSV, and then load it into
Python for analysis. Instead, the entire workflow — connect, query,
transform, visualize, report — happens in a single script that can be
automated and scheduled to run without any human involvement.

For Focus Bear this means analytics reports can be generated
automatically on a schedule (daily, weekly, monthly) pulling fresh
data directly from the database every time. No manual exports, no
stale data, no human error in the transfer process. A single Python
script becomes a self-contained analytics pipeline.

### How does psycopg differ from psycopg2?
Both are Python libraries for connecting to PostgreSQL databases, but
they represent different generations of the same tool:

- **psycopg2** is the older, widely used library that has been the
  standard PostgreSQL adapter for Python for many years. It is
  synchronous — it waits for each query to complete before continuing.
- **psycopg (psycopg3)** is the newer version, rewritten from scratch
  with modern Python features. Key improvements include native support
  for async/await (non-blocking queries), better type handling, improved
  performance, and a cleaner API.

For Focus Bear's analytics work, psycopg2 is still commonly used and
well supported. psycopg3 is increasingly preferred for new projects,
particularly where async performance matters. The SQL queries themselves
are identical between the two — only the connection and cursor syntax
differs slightly.

### How can Pandas help with post-query data transformation?
SQL is excellent at retrieving and aggregating data but has limitations
for complex transformations. Once data is loaded into a Pandas DataFrame,
Python's full power becomes available:

- **Calculated columns:** Adding new columns based on conditions, like
  the engagement level column created using `apply()` and a lambda function
- **Date handling:** Converting string dates to datetime objects and
  extracting components like day of week, month, or quarter
- **Reshaping:** Pivoting, melting, and restructuring data into formats
  that SQL alone cannot easily produce
- **Visualization:** Passing DataFrame columns directly to Matplotlib
  or Seaborn for instant charts
- **Machine learning:** Feeding cleaned DataFrames directly into
  Scikit-learn models for predictive analytics

The typical workflow is: use SQL for what it's best at (filtering,
joining, aggregating large datasets efficiently), then hand the result
to Pandas for the transformations and analysis that benefit from
Python's flexibility.

### How could this integration be used to generate automated reports for Focus Bear?
A Python + Pandas + PostgreSQL pipeline could power several automated
reports for Focus Bear:

- **Daily engagement report:** Every morning, a script queries the
  previous day's session data, calculates average focus minutes and
  habit completion rates by membership tier, generates charts, and
  emails the report to the product team — all without any manual work
- **Weekly retention report:** Queries cohort data to show what
  percentage of users from each signup week are still active, with
  a line chart showing retention curves over time
- **Feature usage dashboard:** Aggregates session data by feature
  used, generates a bar chart of the most and least used features,
  and flags any features with declining usage week-over-week
- **User health score:** For each active user, calculates a composite
  score based on streak length, average focus minutes, and habit
  completion rate — stored back to the database for use in the app

These pipelines would run on a schedule using a task scheduler, turning
what would otherwise be manual weekly analysis into a fully automated,
always-current analytics system.
