# Combining SQL + Pandas for Deeper Insights

## What I Did

Built a multi-insight analytics pipeline combining SQL queries and Pandas
transformations across three related tables (users, sessions, habits),
producing four insights and a four-chart analytics dashboard.

### Insight 1: User Engagement Summary
SQL query joins users and sessions, calculates total sessions, average
focus minutes, and total habits completed per user. Pandas then adds
a composite engagement score and categorises users into tiers:
- **Champion** (score >= 80): High engagement, consistent users
- **Active** (score >= 50): Regular users with room to grow
- **At Risk** (score < 50): Low engagement, potential churn risk

### Insight 2: Daily Focus Trend
SQL aggregates sessions by date, showing how average focus minutes and
total habits completed change day by day. Pandas converts the date
strings to datetime for proper time-series plotting.

### Insight 3: Habit Completion Rate
SQL calculates the completion rate for each habit type — showing which
habits users complete consistently and which they tend to skip.

### Insight 4: Engagement by Country
SQL groups users by country and calculates average focus minutes per
region — useful for understanding geographic differences in engagement.

### Analytics Dashboard
Generated a 4-chart dashboard saved as `analytics_dashboard.png`:
- User engagement scores (horizontal bar, colour-coded by tier)
- Daily average focus minutes trend (line chart)
- Habit completion rates by habit type (bar chart)
- Average focus minutes by country (bar chart)

---

## Reflection

### How can combining SQL and Pandas improve data analysis for Focus Bear?

SQL and Pandas serve complementary roles in the analytics workflow —
SQL is optimised for retrieving and aggregating large datasets directly
from the database, while Pandas is optimised for the complex
transformations, calculations, and visualizations that SQL alone cannot
easily perform. Together they form a complete analytics pipeline.

**What SQL handles best:**
- Joining multiple tables (users, sessions, habits) into one result set
- Filtering and aggregating millions of rows efficiently at the database level
- Grouping data by membership, country, date, or feature
- Calculating summary statistics like averages, counts, and sums

**What Pandas adds on top:**
- Calculated columns that combine multiple metrics into a composite score
  (like the engagement score that weights focus minutes, habits, and sessions)
- User segmentation into tiers (Champion, Active, At Risk) using apply()
  and lambda functions
- Datetime conversion and time-series analysis (extracting day of week,
  month, or quarter from date strings)
- Multi-chart dashboard generation with Matplotlib and Seaborn
- Data reshaping — pivoting, melting, and restructuring results into
  formats that SQL cannot produce

**Practical impact for Focus Bear:**

The engagement scoring system demonstrated in this analysis is a real
example of something Focus Bear could use in production. By combining:
- Average focus minutes from the sessions table (SQL)
- Total habits completed from the habits table (SQL JOIN)
- Session frequency from session counts (SQL aggregation)
- A weighted composite score (Pandas calculation)
- Tier classification (Pandas apply)

...the analytics pipeline produces an actionable user health score that
identifies at-risk users before they churn. This kind of insight is
impossible to generate in SQL alone but straightforward once data is
in a Pandas DataFrame.

Other concrete applications for Focus Bear:
- **Churn prediction:** Flag users whose engagement score has dropped
  more than 30% week-over-week as at-risk, triggering a re-engagement
  notification
- **Feature effectiveness:** Compare engagement scores before and after
  a user adopts a new feature to measure its impact
- **Geographic insights:** Identify countries with low average focus
  minutes as markets where the app's default habit recommendations may
  not resonate with local routines
- **Habit effectiveness:** Surface which habits have the highest
  completion rates and correlate them with longer focus sessions —
  informing which habits to recommend to new users during onboarding

The combination of SQL's data retrieval power and Pandas' transformation
flexibility means these insights can be generated automatically on a
schedule, giving the Focus Bear team a constantly updated view of user
health without any manual analysis work.
