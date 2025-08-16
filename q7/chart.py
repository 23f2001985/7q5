import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generate synthetic data
np.random.seed(42)
categories = ["Electronics", "Clothing", "Home & Kitchen", "Sports", "Books"]
satisfaction = [np.random.normal(loc=75, scale=5) for _ in categories]

df = pd.DataFrame({"Category": categories, "Satisfaction": satisfaction})

# Professional Seaborn style
sns.set_style("whitegrid")
sns.set_context("talk")

# Plot
plt.figure(figsize=(8, 8))
ax = sns.barplot(
    data=df,
    x="Category",
    y="Satisfaction",
    hue="Category",       # ✅ Fix: use hue
    palette="Set2",
    legend=False          # ✅ Avoid duplicate legend
)

# Titles and labels
ax.set_title("Average Customer Satisfaction by Product Category", fontsize=16, weight="bold")
ax.set_ylabel("Satisfaction Score")
ax.set_xlabel("Product Category")

# Rotate labels for readability
plt.xticks(rotation=30)

# Save as 512x512
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
