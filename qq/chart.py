import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set professional style
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic data
np.random.seed(42)
categories = ["Electronics", "Clothing", "Home & Kitchen", "Sports", "Beauty", "Toys"]
avg_scores = np.random.uniform(3.5, 4.8, size=len(categories))  # scores between 3.5–4.8

data = pd.DataFrame({
    "Product Category": categories,
    "Avg Satisfaction Score": avg_scores
})

# Create the barplot
plt.figure(figsize=(8, 8))  # 8 inches * 64 dpi = 512 px
ax = sns.barplot(
    data=data,
    x="Product Category",
    y="Avg Satisfaction Score",
    palette="Blues_d"
)

# Customize appearance
ax.set_title("Average Customer Satisfaction by Product Category", fontsize=16, weight="bold")
ax.set_xlabel("Product Category", fontsize=14)
ax.set_ylabel("Average Satisfaction Score (1–5)", fontsize=14)
ax.set_ylim(0, 5)

# Rotate x-labels for readability
plt.xticks(rotation=30, ha="right")

# ✅ Save with exact dimensions (no trimming)
plt.savefig("chart.png", dpi=64, pad_inches=0)
plt.close()
