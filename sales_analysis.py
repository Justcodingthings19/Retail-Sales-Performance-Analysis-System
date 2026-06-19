import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("dataset/retail_sales.csv")

print("Dataset Preview")
print(data.head())

print("\nDataset Information")
print(data.info())

print("\nSummary Statistics")
print(data.describe())

total_sales = data["Sales"].sum()

print("\nTotal Sales:", total_sales)

monthly_sales = data.groupby("Month")["Sales"].sum()

plt.figure(figsize=(10,5))
monthly_sales.plot(kind="bar")

plt.title("Monthly Sales Analysis")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.tight_layout()
plt.show()
