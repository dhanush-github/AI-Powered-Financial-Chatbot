import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the financial data from an Excel file
df = pd.read_excel("financial_data.xlsx")

# Sort values to ensure proper year-over-year calculations
df.sort_values(by=["Company", "Year"], inplace=True)

# Calculate Year-over-Year Growth Rates
df["Revenue Growth (%)"] = df.groupby("Company")["Total Revenue"].pct_change() * 100
df["Net Income Growth (%)"] = df.groupby("Company")["Net Income"].pct_change() * 100
df["Asset Growth (%)"] = df.groupby("Company")["Total Assets"].pct_change() * 100
df["Liability Growth (%)"] = df.groupby("Company")["Total Liabilities"].pct_change() * 100
df["Cash Flow Growth (%)"] = df.groupby("Company")["Cash Flow from Ops"].pct_change() * 100

# Display the dataframe with growth rates
print(df)

# Plot Total Revenue Trend
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x="Year", y="Total Revenue", hue="Company", marker="o")
plt.title("Total Revenue Trend (Last 3 Years)")
plt.ylabel("Total Revenue (in billion USD)")
plt.xlabel("Year")
plt.grid(True)
plt.show()

# Plot Net Income Growth
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x="Year", y="Net Income Growth (%)", hue="Company", marker="o")
plt.title("Net Income Growth Trend")
plt.ylabel("Net Income Growth (%)")
plt.xlabel("Year")
plt.grid(True)
plt.show()

# Export the updated dataframe with calculated growth rates to a new Excel file
df.to_excel("financial_analysis_output.xlsx", index=False)
