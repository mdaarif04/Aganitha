import pandas as pd

# Load CSV data
df = pd.read_csv("sales_data.csv")

# Process: Calculate total sales per product
sales_summary = df.groupby("Product")["Sales"].sum().reset_index()

# Save results
sales_summary.to_csv("sales_summary.csv", index=False)

print("Sales summary generated successfully!")
