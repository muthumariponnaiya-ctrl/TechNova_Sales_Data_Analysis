import pandas as pd
import matplotlib.pyplot as plt
import os

# Create charts folder if it doesn't exist
os.makedirs("charts", exist_ok=True)

# Load dataset
df = pd.read_csv("sales_data.csv")

# Create Revenue column
df["Revenue"] = df["Quantity"] * df["Price"]

# Display first 5 rows
print("Sales Data:")
print(df.head())

# Total Revenue
total_revenue = df["Revenue"].sum()
print("\nTotal Revenue:", total_revenue)

# Sales by Category
sales_by_category = df.groupby("Category")["Revenue"].sum()
print("\nSales by Category:")
print(sales_by_category)

# Top Products
top_products = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)
print("\nTop Products:")
print(top_products)

# Sales by Region
sales_by_region = df.groupby("Region")["Revenue"].sum()
print("\nSales by Region:")
print(sales_by_region)

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Monthly Sales
monthly_sales = df.groupby(df["Date"].dt.to_period("M"))["Revenue"].sum()
monthly_sales.index = monthly_sales.index.astype(str)

# -----------------------------
# Chart 1: Sales by Category
# -----------------------------
plt.figure(figsize=(6,4))
sales_by_category.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("charts/sales_by_category.png")
plt.close()

# -----------------------------
# Chart 2: Top Products
# -----------------------------
plt.figure(figsize=(8,4))
top_products.plot(kind="bar")
plt.title("Top Products")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("charts/top_products.png")
plt.close()

# -----------------------------
# Chart 3: Sales by Region
# -----------------------------
plt.figure(figsize=(6,4))
sales_by_region.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("charts/sales_by_region.png")
plt.close()

# -----------------------------
# Chart 4: Monthly Sales
# -----------------------------
plt.figure(figsize=(6,4))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(True)
plt.tight_layout()
plt.savefig("charts/monthly_sales.png")
plt.close()

print("\nAnalysis Completed Successfully!")
print("Charts are saved inside the 'charts' folder.")
# -----------------------------
# Pivot Table Summary
# -----------------------------
pivot_table = pd.pivot_table(
    df,
    values="Revenue",
    index="Category",
    columns="Region",
    aggfunc="sum",
    fill_value=0
)

print("\nPivot Table Summary:")
print(pivot_table)

# Save pivot table as CSV
pivot_table.to_csv("pivot_summary.csv")