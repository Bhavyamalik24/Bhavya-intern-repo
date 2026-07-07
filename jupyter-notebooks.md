# Jupyter Notebooks for Interactive Analysis

## What are Jupyter Notebooks?
Jupyter Notebooks are interactive documents that combine live Python code,
visualizations, and formatted text (Markdown) in a single file. Unlike
a regular Python script that runs top to bottom and shows output only in
the terminal, a Jupyter Notebook lets you run individual cells one at a
time, see the output immediately below each cell, and document your
thinking alongside your code.

## What I Did

Created a notebook called `FocusBear.ipynb` that:
- Loaded a simulated Focus Bear dataset of 20 users using Pandas
- Inspected the dataset structure and basic statistics
- Created a box plot comparing focus minutes between free and premium users
- Created a scatter plot showing habits completed vs days active
- Used Markdown cells to document insights and explain each section

### Key Finding from the Analysis
Premium users focus significantly more than free users — the median focus
time for premium users (around 80 minutes) is roughly double that of free
users (around 30 minutes). There is also a clear positive correlation
between days active and habits completed, suggesting that longer-term
users build stronger habit consistency over time.

---

## Reflection

### What are the advantages of using Jupyter Notebooks for data analysis?
- **Interactive execution:** You can run one cell at a time and see
  results immediately, making it easy to experiment and debug without
  re-running the entire script
- **Inline visualizations:** Charts appear directly below the code that
  generated them, keeping context and output together
- **Mixed content:** Code, charts, and written explanations all live in
  the same document, making it easy to share insights with non-technical
  stakeholders
- **Iterative exploration:** You can modify a single cell and re-run it
  without affecting other cells, which is ideal for exploratory analysis
- **Reproducibility:** Anyone can open the notebook and re-run all cells
  to reproduce the exact same results

### How does Jupyter improve workflows compared to standalone Python scripts?
A standalone Python script runs all at once and only shows terminal
output — if something breaks halfway through, you have to fix it and
re-run everything from the start. Jupyter lets you run code in small
chunks, inspect the output at each step, and fix issues in isolation.

For data analysis specifically, this is transformative. Instead of
writing a full analysis script, running it, seeing a chart that looks
wrong, hunting for the bug, and running everything again — you can build
the analysis incrementally, verifying each step before moving to the next.
This makes Jupyter far faster for exploration and debugging than
traditional scripts.

### What are Markdown cells and why are they useful?
Markdown cells are cells that render formatted text rather than running
code. They support headings, bold, italic, bullet points, and tables —
making it possible to write professional documentation directly inside
the notebook.

They are useful because they turn a notebook from a collection of code
snippets into a coherent, readable document. A notebook with proper
Markdown cells reads like a report — explaining what the analysis is
trying to answer, what each piece of code does, and what the results
mean. This makes notebooks shareable with people who don't need to
understand the code, just the insights.

### How could Jupyter Notebooks be used for analysing Focus Bear's user trends?
Jupyter Notebooks would be ideal for Focus Bear's data analytics work
in several ways:

- **User retention analysis:** Load session data and visualize how
  engagement changes over time — identifying when users typically drop
  off and what might cause it
- **Feature usage exploration:** Query the database for feature usage
  stats and create bar charts showing which features drive the most
  engagement across different user segments
- **A/B test analysis:** Compare metrics between two groups of users
  who experienced different features or onboarding flows, with charts
  and statistical summaries in one document
- **Weekly/monthly reporting:** Build a reusable notebook that
  automatically pulls fresh data and generates charts for team meetings
- **Habit completion patterns:** Analyse which habits users complete
  most consistently, which they abandon, and whether completion rates
  improve over time — directly informing product decisions about which
  habits to promote or simplify
