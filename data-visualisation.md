# Data Visualization with Matplotlib and Seaborn

## Charts Created

### 1. Line Chart - Daily Focus Minutes
Shows how focus minutes changed across 7 days. Line charts are ideal
for showing trends over time — you can immediately see whether focus
is improving, declining, or fluctuating.

### 2. Bar Chart - Focus Bear Feature Usage
Compares how many users use each Focus Bear feature. Bar charts are
ideal for comparing categories side by side — the height difference
between bars makes comparisons instant and obvious.

### 3. Scatter Plot - Sleep Hours vs Productivity
Shows the relationship between sleep hours and productivity scores.
Each dot represents one person. The upward trend from left to right
shows that more sleep generally correlates with higher productivity.

### 4. Seaborn Histogram - Distribution of Focus Minutes
Shows how 200 simulated focus sessions are distributed. Most sessions
cluster around 50 minutes (the centre of the bell curve). The KDE
line shows the smooth overall shape of the distribution, making it
easy to spot whether most users are hitting their focus goals or
falling short.

### 5. Seaborn Heatmap - Correlation Between Wellbeing Factors
Shows the correlation between Sleep, Focus, Exercise, and Mood using
colour intensity. Sleep and Focus have the strongest correlation (0.7),
meaning users who sleep more tend to focus more. The diagonal is always
1.0 because every variable perfectly correlates with itself.

---

## Reflection

### Why is data visualization important in analytics?
Raw numbers are hard to interpret at a glance. A table of 200 focus
session durations tells you nothing useful until you visualize it as
a histogram — then you immediately see where most users cluster, whether
there are outliers, and whether the distribution is balanced or skewed.
Visualization turns data into insight by making patterns, trends, and
anomalies visible without requiring the viewer to mentally process
hundreds of individual data points.

For a product like Focus Bear, visualization is essential for answering
questions like: Are users actually using the app consistently? Which
features drive the most engagement? Do users who complete morning
routines have better focus sessions? These questions cannot be answered
by staring at a database — they need charts.

### What types of charts are most useful for different types of data?

| Chart Type | Best Used For | Example |
|---|---|---|
| Line chart | Trends over time | Daily focus minutes across a week |
| Bar chart | Comparing categories | Feature usage across different features |
| Scatter plot | Relationship between two variables | Sleep vs productivity |
| Histogram | Distribution of a single variable | How focus minutes are spread |
| Heatmap | Correlations between multiple variables | Sleep, focus, exercise, mood |

### How do Seaborn's advanced visualizations compare to Matplotlib's basic charts?
Matplotlib gives you full control but requires more code to produce
polished results. A basic line chart needs explicit colour, marker,
grid, title, and label settings to look professional. Seaborn handles
much of this automatically — `sns.histplot()` with `kde=True` produces
a publication-quality distribution chart in two lines that would take
significantly more code to replicate in pure Matplotlib.

Seaborn also introduces chart types that Matplotlib doesn't have built
in — like heatmaps and distribution plots — which are particularly
useful for data analytics work. The tradeoff is that Seaborn is less
flexible for highly customised charts, where Matplotlib's lower-level
control becomes an advantage.

In practice, both are used together — Seaborn for quick, beautiful
charts and Matplotlib for fine-grained customisation.

### How could Focus Bear use visualizations to improve product decisions?
Focus Bear collects rich behavioural data — habit completion rates,
focus session durations, break frequency, streak lengths, and feature
usage. Visualizations could directly support product decisions in
several ways:

- **Line charts** of daily active users over time would show whether
  retention is improving or declining after a new feature release
- **Histograms** of focus session lengths would reveal whether users
  are actually completing their intended sessions or dropping off early
- **Heatmaps** of feature correlations would show which combinations
  of features (e.g. morning routine + focus blocks) are associated with
  the best user outcomes
- **Bar charts** of feature usage would highlight which features are
  underused and might need better onboarding or promotion
- **Scatter plots** of streak length vs focus duration would show
  whether long-term users actually focus more effectively than new ones

These insights would allow the Focus Bear team to make evidence-based
product decisions rather than relying on gut feeling — prioritising
features that actually improve user outcomes and identifying friction
points that cause users to disengage.
