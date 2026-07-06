import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# ---- 1. LINE CHART ----
days = [1, 2, 3, 4, 5, 6, 7]
focus_minutes = [30, 45, 40, 60, 55, 70, 65]

plt.figure(figsize=(8, 4))
plt.plot(days, focus_minutes, color="blue", marker="o")
plt.title("Daily Focus Minutes - Week 1")
plt.xlabel("Day")
plt.ylabel("Minutes")
plt.grid(True)
plt.savefig("line_chart.png")
plt.show()

# ---- 2. BAR CHART ----
features = ["Habits", "Focus Mode", "Break Reminders", "Reports"]
usage_count = [150, 200, 90, 60]

plt.figure(figsize=(8, 4))
plt.bar(features, usage_count, color=["#4CAF50", "#2196F3", "#FF9800", "#9C27B0"])
plt.title("Focus Bear Feature Usage")
plt.xlabel("Feature")
plt.ylabel("Number of Users")
plt.savefig("bar_chart.png")
plt.show()

# ---- 3. SCATTER PLOT ----
sleep_hours = [5, 6, 7, 8, 9, 6, 7, 8, 5, 9]
productivity = [40, 55, 65, 80, 85, 50, 70, 75, 35, 90]

plt.figure(figsize=(8, 4))
plt.scatter(sleep_hours, productivity, color="red", s=100)
plt.title("Sleep Hours vs Productivity Score")
plt.xlabel("Sleep Hours")
plt.ylabel("Productivity Score")
plt.savefig("scatter_plot.png")
plt.show()

# ---- 4. SEABORN HISTOGRAM ----
focus_data = np.random.normal(loc=50, scale=15, size=200)

plt.figure(figsize=(8, 4))
sns.histplot(focus_data, bins=20, color="teal", kde=True)
plt.title("Distribution of Daily Focus Minutes")
plt.xlabel("Focus Minutes")
plt.savefig("histogram.png")
plt.show()

# ---- 5. SEABORN HEATMAP ----
correlation_data = pd.DataFrame({
    "Sleep": [1.0, 0.7, 0.5, 0.3],
    "Focus": [0.7, 1.0, 0.6, 0.4],
    "Exercise": [0.5, 0.6, 1.0, 0.2],
    "Mood": [0.3, 0.4, 0.2, 1.0]
}, index=["Sleep", "Focus", "Exercise", "Mood"])

plt.figure(figsize=(6, 5))
sns.heatmap(correlation_data, annot=True, cmap="coolwarm", vmin=0, vmax=1)
plt.title("Correlation Between Wellbeing Factors")
plt.savefig("heatmap.png")
plt.show()

print("All charts saved!")