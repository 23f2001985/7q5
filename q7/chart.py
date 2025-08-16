import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# ---------------------------
# Generate synthetic data
# ---------------------------
np.random.seed(42)

categories = ["Electronics", "Clothing", "Home & Kitchen", "Sports", "Beauty", "Toys"]
avg_scores = [7.8, 6.9, 8.2, 7.1, 7.5, 6.8]  # average satisfaction scores (0-10 scale)

# Create DataFrame
df = pd.DataFrame({
    "Category": categories,
    "Satisfaction": avg_scores
})

# ---------------------------
# Seaborn styling
# ---------------------------
sns.set_style("whitegrid")
sns.set_context("talk")  # larger font sizes for presentation

# ---------------------------
# Create barplot
# ---------------------------
plt.figure(figsize=(8, 8))  # ensures 512x512 pixels when dpi=64
ax = sns.barplot(
    x="Category", 
    y="Satisfaction", 
    data=df,
    palette="viridis"
)

# Titles and labels
ax.set_title("Average Customer Satisfaction by Product Category", fontsize=16, pad=20)
ax.set_xlabel("Product Category", fontsize=14)
ax.set_ylabel("Average Satisfaction (0–10)", fontsize=14)

# Rotate category labels for readability
plt.xticks(rotation=20)

# ---------------------------
# Save chart as PNG (512x512 px)
# ---------------------------
plt.tight_layout()
plt.savefig("chart.png", dpi=64, bbox_inches='tight')  # 8*64 = 512 px
plt.close()
