# Using PostgreSQL for Analytics

## What I Did

Practised PostgreSQL analytics concepts using SQLite with three related
tables — users, sessions, and habits — covering JOIN operations, CASE
statements, window functions, and query planning.

### JOIN — Combining Multiple Tables
```sql
SELECT u.name, u.membership, u.country,
       s.focus_minutes, s.habits_completed,
       s.feature_used, s.session_date
FROM users u
JOIN sessions s ON u.user_id = s.user_id
ORDER BY s.focus_minutes DESC;
```
Combines user profile data with session data in one result set, giving
a complete picture of each user's activity without needing separate queries.

### CASE — Conditional Data Transformation
```sql
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
ORDER BY avg_focus DESC;
```
Creates a new calculated column based on conditions — categorising users
into engagement levels based on their average focus minutes.

### Window Function — Running Total
```sql
SELECT user_id, session_date, focus_minutes,
       SUM(focus_minutes) OVER (
           PARTITION BY user_id
           ORDER BY session_date
       ) as running_total_focus
FROM sessions
ORDER BY user_id, session_date;
```
Calculates a running total of focus minutes for each user across their
sessions — without collapsing rows like GROUP BY would. Each row keeps
its individual data while also showing the cumulative total.

### Multi-Table JOIN
```sql
SELECT u.name, u.membership,
       s.focus_minutes,
       h.habit_name,
       CASE WHEN h.completed = 1 THEN 'Yes' ELSE 'No' END as completed
FROM users u
JOIN sessions s ON u.user_id = s.user_id
JOIN habits h ON u.user_id = h.user_id
WHERE s.session_date = '2024-01-15'
ORDER BY u.name;
```
Joins three tables simultaneously to show each user's session data
alongside their individual habit completion status for the same date.

### EXPLAIN ANALYZE — Query Planning
```sql
EXPLAIN QUERY PLAN
SELECT u.name, AVG(s.focus_minutes)
FROM users u
JOIN sessions s ON u.user_id = s.user_id
GROUP BY u.user_id;
```
Shows how the database engine plans to execute the query — which tables
it scans, whether it uses indexes, and the order of operations. In
PostgreSQL, `EXPLAIN ANALYZE` goes further by actually running the query
and showing real execution times for each step.

---

## Reflection

### What makes PostgreSQL a good choice for data analytics?
PostgreSQL is one of the most feature-rich open-source databases
available, making it particularly well suited for analytics:

- **Advanced SQL support:** PostgreSQL supports window functions, CTEs
  (Common Table Expressions), recursive queries, and complex joins that
  simpler databases like SQLite don't fully support
- **JSON support:** PostgreSQL can store and query JSON data natively,
  making it flexible for semi-structured data like user event logs or
  app configuration data
- **Indexing options:** PostgreSQL supports multiple index types (B-tree,
  Hash, GIN, GiST) that can dramatically speed up analytical queries
  on large datasets
- **Reliability and scale:** PostgreSQL handles large datasets reliably
  with ACID compliance, making it trustworthy for production data
- **Integration:** PostgreSQL integrates directly with Python (via
  psycopg2 or SQLAlchemy), Pandas, and visualization tools, fitting
  naturally into the analytics workflow

For Focus Bear specifically, PostgreSQL stores all user activity data
and its analytics features allow the team to run complex queries across
users, sessions, habits, and events without moving data to a separate
analytics platform.

### How do JOIN operations help in analysing relational data?
Relational databases store data in separate tables to avoid duplication
— user information lives in one table, session data in another, habit
data in a third. JOIN operations bring these tables together into a
single result set by matching rows on a common key (like user_id).

Without JOINs, you would need to run multiple separate queries and
manually combine the results in Python. With JOINs, you can retrieve
a complete, combined view of user activity in a single query — for
example, showing each user's name, membership type, session duration,
and habit completion status all at once. This is essential for analytics
because insights almost always require data from multiple tables.

### What are window functions and how can they be used for user trend analysis?
Window functions perform calculations across a set of rows related to
the current row, without collapsing those rows into a single summary
like GROUP BY does. The `OVER` clause defines the "window" of rows to
include in each calculation.

Common window functions for user trend analysis:
- `SUM() OVER (PARTITION BY user_id ORDER BY date)` — running total of
  focus minutes per user, showing cumulative progress over time
- `ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY focus_minutes DESC)`
  — ranks each user's sessions from longest to shortest
- `LAG(focus_minutes) OVER (ORDER BY session_date)` — compares each
  session to the previous one, useful for detecting improvement or decline
- `AVG(focus_minutes) OVER (PARTITION BY membership)` — shows each
  user's focus minutes alongside the average for their membership tier

For Focus Bear, window functions would be ideal for tracking whether
individual users are improving their focus over time, or comparing
each user's performance to the average for their cohort.

### Why is query optimization important and how does EXPLAIN ANALYZE help?
As Focus Bear grows, its database will contain millions of session
records and event logs. A poorly written query that scans every row
in a table (a "full table scan") might run in milliseconds on 1,000
rows but take minutes on 10 million rows. Query optimization ensures
that analytical queries remain fast as the data scales.

`EXPLAIN ANALYZE` in PostgreSQL shows:
- **The query plan:** Which tables are scanned, in what order, and
  whether indexes are used
- **Estimated vs actual rows:** Whether the database's estimates match
  reality (large differences suggest outdated statistics)
- **Execution time per step:** Which part of the query is the bottleneck
- **Index usage:** Whether the query is using available indexes or
  doing expensive sequential scans

For example, if a query filtering sessions by `user_id` is doing a
sequential scan instead of using an index, adding an index on `user_id`
could reduce query time from seconds to milliseconds. `EXPLAIN ANALYZE`
makes these bottlenecks visible so they can be fixed before they become
production problems.
