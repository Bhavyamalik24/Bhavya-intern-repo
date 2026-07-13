# Introduction to SQL for Data Analysis

## What I Did

Created a simulated Focus Bear database using SQLite with two tables:
- `users` — 8 users with membership type, signup date, and country
- `sessions` — 10 sessions with focus minutes, habits completed, and
  feature used

Practised the following SQL concepts:

### SELECT — Retrieve all data
```sql
SELECT * FROM users;
```

### WHERE — Filter rows
```sql
SELECT name, membership, country
FROM users
WHERE membership = 'premium';
```

### ORDER BY — Sort results
```sql
SELECT session_id, user_id, focus_minutes
FROM sessions
ORDER BY focus_minutes DESC;
```

### GROUP BY — Aggregate data
```sql
SELECT u.membership,
       COUNT(s.session_id) as total_sessions,
       AVG(s.focus_minutes) as avg_focus_minutes
FROM sessions s
JOIN users u ON s.user_id = u.user_id
GROUP BY u.membership;
```

### HAVING — Filter aggregated results
```sql
SELECT user_id,
       AVG(focus_minutes) as avg_focus,
       COUNT(session_id) as total_sessions
FROM sessions
GROUP BY user_id
HAVING AVG(focus_minutes) > 70
ORDER BY avg_focus DESC;
```

### JOIN — Combine tables
```sql
SELECT u.name, u.membership, u.country,
       s.focus_minutes, s.habits_completed,
       s.feature_used, s.session_date
FROM users u
JOIN sessions s ON u.user_id = s.user_id
ORDER BY s.focus_minutes DESC;
```

### Key Findings
- Premium users average significantly more focus minutes than free users
- Users with above-average focus minutes tend to also complete more habits
- Focus mode is the most used feature among high-engagement users

---

## Reflection

### How does SQL help in data analysis?
SQL is the most direct way to query structured data stored in a database.
Instead of loading an entire table into Python and filtering it there,
SQL lets you retrieve exactly the rows and columns you need — which is
faster, uses less memory, and keeps the data processing close to where
the data lives. For a product like Focus Bear with thousands of users
and millions of session records, SQL is essential for efficient data
retrieval before any Python analysis begins.

### What is the difference between WHERE and GROUP BY?
`WHERE` filters individual rows before any aggregation happens — it
decides which rows are included in the result set:
```sql
WHERE membership = 'premium'  -- only include premium users
```

`GROUP BY` collapses multiple rows into summary groups and is used with
aggregate functions like `AVG`, `COUNT`, `SUM`, and `MAX`:
```sql
GROUP BY membership  -- calculate stats for each membership type
```

`HAVING` is like `WHERE` but for aggregated results — it filters groups
after the aggregation has been calculated:
```sql
HAVING AVG(focus_minutes) > 70  -- only show groups where average > 70
```

The key distinction: `WHERE` filters rows, `GROUP BY` summarises them,
and `HAVING` filters the summaries.

### How would you retrieve and analyse user activity data in Focus Bear?
Focus Bear's PostgreSQL database likely has tables for users, sessions,
habits, and feature events. Example queries that would be useful:

```sql
-- Daily active users over the last 30 days
SELECT session_date, COUNT(DISTINCT user_id) as daily_active_users
FROM sessions
WHERE session_date >= CURRENT_DATE - INTERVAL '30 days'
GROUP BY session_date
ORDER BY session_date;

-- Average focus minutes by membership type
SELECT u.membership,
       AVG(s.focus_minutes) as avg_focus,
       COUNT(DISTINCT u.user_id) as total_users
FROM users u
JOIN sessions s ON u.user_id = s.user_id
GROUP BY u.membership;

-- Most used features
SELECT feature_used, COUNT(*) as usage_count
FROM sessions
GROUP BY feature_used
ORDER BY usage_count DESC;
```

These queries would give the product team immediate visibility into
engagement, retention, and feature adoption without needing to write
any Python code first.

### Why is SQL important even if you primarily use Python for analytics?
Python and SQL serve different roles in the analytics workflow:

- **SQL** retrieves and pre-processes data from the database efficiently
  — filtering, joining, and aggregating millions of rows directly in
  the database engine, which is much faster than loading everything
  into Python first
- **Python** takes the results of SQL queries and performs more complex
  analysis, visualization, machine learning, and reporting that SQL
  alone cannot do

In practice, a data analyst uses both — SQL to get the right data out
of the database, and Python to analyse and visualize it. Knowing only
Python means you depend on someone else to extract the data for you,
which slows down your workflow. SQL is also the universal language of
databases — every major data platform (PostgreSQL, MySQL, BigQuery,
Snowflake, Redshift) uses SQL, making it one of the most transferable
skills in the data analytics field.
