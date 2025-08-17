import pandas as pd
import matplotlib.pyplot as plt

EMAIL = "23f2001985@ds.study.iitm.ac.in"

df = pd.read_csv("equipment_efficiency_2024.csv")
target = 90.0

# Stats
avg = round(df["efficiency_rate"].mean(), 2)
min_q = df.loc[df["efficiency_rate"].idxmin()]
max_q = df.loc[df["efficiency_rate"].idxmax()]
improvement_q3_q4 = round(df.loc[3, "efficiency_rate"] - df.loc[2, "efficiency_rate"], 2)

print("Email:", EMAIL)
print("Average:", avg)
print("Lowest Quarter:", min_q.quarter, min_q.efficiency_rate)
print("Highest Quarter:", max_q.quarter, max_q.efficiency_rate)
print("Q3→Q4 improvement:", improvement_q3_q4)

# Visualization
plt.figure(figsize=(8,5))
plt.plot(df["quarter"], df["efficiency_rate"], marker="o")
plt.axhline(target, linestyle="--")
plt.title("Equipment Efficiency Rate – 2024 Trend vs Industry Target")
plt.xlabel("Quarter")
plt.ylabel("Efficiency Rate")
for x, y in zip(df["quarter"], df["efficiency_rate"]):
    plt.text(x, y+0.6, f"{y}", ha="center")
plt.tight_layout()
plt.savefig("trend_vs_target.png")
print("Saved chart to trend_vs_target.png")
