import pandas as pd
import matplotlib.pyplot as plt
import os

# تأكد من وجود مجلد النتائج
os.makedirs("results", exist_ok=True)

# ===============================
# 1) Load data
# ===============================
df = pd.read_csv("data/sales_data.csv", parse_dates=["date"])

# Compute revenue
df["revenue"] = df["units_sold"] * df["unit_price"] * (1 - df["discount"])

print("First rows:")
print(df.head(), "\n")

# ===============================
# 2) Basic summary
# ===============================
print("Summary statistics:")
print(df[["units_sold", "unit_price", "revenue"]].describe(), "\n")

print("Total revenue by city:")
print(df.groupby("city")["revenue"].sum().sort_values(ascending=False), "\n")

print("Total revenue by product category:")
print(df.groupby("product_category")["revenue"].sum().sort_values(ascending=False), "\n")

print("Total revenue by channel:")
print(df.groupby("channel")["revenue"].sum(), "\n")

# ===============================
# 3) Revenue over time
# ===============================
daily_rev = df.groupby("date")["revenue"].sum().reset_index()

plt.figure(figsize=(8, 4))
plt.plot(daily_rev["date"], daily_rev["revenue"], marker="o")
plt.title("Daily Revenue Over Time")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("results/daily_revenue.png")
plt.close()

# ===============================
# 4) Revenue by city (bar chart)
# ===============================
city_rev = df.groupby("city")["revenue"].sum().sort_values(ascending=False)

plt.figure(figsize=(6, 4))
city_rev.plot(kind="bar")
plt.title("Total Revenue by City")
plt.xlabel("City")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("results/revenue_by_city.png")
plt.close()

# ===============================
# 5) Revenue by product category
# ===============================
cat_rev = df.groupby("product_category")["revenue"].sum().sort_values(ascending=False)

plt.figure(figsize=(6, 4))
cat_rev.plot(kind="bar")
plt.title("Total Revenue by Product Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("results/revenue_by_category.png")
plt.close()

print("✅ Analysis complete. Charts saved in 'results/' folder.")
