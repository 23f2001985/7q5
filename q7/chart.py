# chart.py
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set Seaborn style
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic data
np.random.seed(42)
categories = ["Electronics", "Clothing", "Home", "Beauty", "Sports"]
satisfaction_scores = [np.random.normal(loc=80, scale=5, size=50).mean() for _ in categories]

# Create DataFrame
df = pd.DataFrame({
    "Category": categories,
    "Satisfaction": satisfaction_scores
})

# Create figure (8 inches * 64 dpi = 512 pixels)
plt.figure(figsize=(8, 8), dpi=64)

# Create barplot
ax = sns.barplot(x="Category", y="Satisfaction", data=df, palette="Set2")

# Style chart
ax.set_title("Average Customer Satisfaction by Product Category", fontsize=14, weight="bold")
ax.set_xlabel("Product Category", fontsize=12)
ax.set_ylabel("Average Satisfaction Score", fontsize=12)

# Rotate x labels for readability
plt.xticks(rotation=20)

# Save chart with exact size 512x512
plt.savefig("chart.png", dpi=64, bbox_inches="tight", pad_inches=0.1)
plt.close()

print("Chart saved as chart.png with size 512x512 pixels")
