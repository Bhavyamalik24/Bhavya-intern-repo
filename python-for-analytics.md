# Introduction to Python for Data Analytics

## Setup Completed

- Created a virtual environment called `focusbear-env` using `python -m venv`
- Activated the environment and installed pandas, matplotlib, seaborn,
  and numpy
- Wrote a script `python_analytics_intro.py` that loads the Focus Bear
  user dataset and prints shape, column names, first 5 rows, and basic
  statistics
- Confirmed all library versions are installed and working

---

## Reflection

### Why is Python preferred for data analytics over other languages?
Python has become the dominant language for data analytics for several
reasons:

- **Rich ecosystem:** Libraries like Pandas, NumPy, Matplotlib, Seaborn,
  and Scikit-learn cover the entire analytics workflow from data loading
  to machine learning, all in one language
- **Readable syntax:** Python reads almost like plain English, making it
  accessible to analysts who are not traditional software developers
- **Community and documentation:** Python has one of the largest data
  science communities in the world, meaning almost every problem has
  a Stack Overflow answer, tutorial, or library already built for it
- **Integration:** Python connects easily to databases, APIs, cloud
  services, and other tools — making it practical for real production
  analytics pipelines
- **Versatility:** The same language used for data analysis can also be
  used for automation, web scraping, backend development, and machine
  learning — meaning skills transfer across the entire technology stack

Compared to alternatives like R (less general purpose), Excel (limited
scale and automation), or SQL alone (no visualization or ML), Python
offers the best combination of power, flexibility, and ease of use for
end-to-end data analytics work.

### What role does Pandas play in data analysis?
Pandas is the foundation of almost every Python data analytics workflow.
It provides the DataFrame — a two-dimensional table structure similar
to a spreadsheet or database table — that makes it easy to load, inspect,
clean, filter, sort, group, and aggregate data.

Key things Pandas handles:
- Loading data from CSV, JSON, Excel, and SQL databases
- Inspecting data with `head()`, `describe()`, `dtypes`, and `isnull()`
- Filtering rows with boolean indexing
- Aggregating data with `groupby()` and `pivot_table()`
- Cleaning missing values with `fillna()`, `dropna()`, and `replace()`
- Merging datasets with `merge()` and `join()`

Without Pandas, all of these operations would require writing manual
loops and custom data structures — Pandas abstracts that complexity into
clean, readable one-liners that work on datasets of any size.

### How do Matplotlib and Seaborn help with data visualization?
Matplotlib is the foundational plotting library — it gives you complete
control over every element of a chart. Line charts, bar charts, scatter
plots, and histograms can all be created with Matplotlib, with full
customisation of colours, labels, titles, grid lines, and sizing.

Seaborn builds on top of Matplotlib and specialises in statistical
visualizations. It requires less code to produce polished charts and
adds chart types that Matplotlib doesn't have built in — like heatmaps,
box plots, and distribution plots with KDE curves.

In practice both are used together — Seaborn for quick, beautiful
statistical charts and Matplotlib for precise customisation when needed.
Together they cover the full range of visualization needs for a data
analytics role.

### What are some use cases for data analytics in Focus Bear?
Having now worked through Pandas, Matplotlib, Seaborn, and Jupyter
Notebooks, I can see several concrete ways Python analytics would apply
directly to Focus Bear:

- **User retention analysis:** Load session data into a DataFrame, group
  by signup cohort, and calculate what percentage of users remain active
  after 7, 14, and 30 days — identifying drop-off points in the user
  journey
- **Habit completion trends:** Aggregate habit completion data by habit
  type and visualize which habits users complete consistently vs abandon,
  informing product decisions about which habits to simplify or promote
- **Feature engagement:** Group event data by feature and membership type
  to identify which features drive the most engagement among premium vs
  free users
- **Focus session analysis:** Analyse the distribution of focus session
  lengths to understand whether users are hitting their intended session
  goals or consistently cutting sessions short
- **A/B test reporting:** Load experiment data for two user groups,
  calculate key metrics for each, and visualize the difference to
  determine whether a new feature improved outcomes

These are exactly the kinds of analyses I expect to work on during
the active collaboration phase of my internship with the Focus Bear
team.
