import pandas as pd
import matplotlib.pyplot as plt
import os

# Retrieves the data from the User's OS
current_directory = os.getcwd()
print(f"Current Working Directory: {current_directory}" )

file_path = os.path.join(current_directory, "combined_orders_dataset.xlsx" )

# Load the dataset
df = pd.read_excel(file_path)
print(df)

# Converting column into date range format and adjusting accordingly
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])

# Removes missing values in required columns
df_clean = df.dropna(subset=['order_purchase_timestamp', 'price', 'freight_value'])

# Calculates the total revenue
df_clean['total_revenue'] = df_clean['price'] + df_clean['freight_value']

# Extracts the year-month for the grouping
df_clean['year_month'] = df_clean['order_purchase_timestamp'].dt.to_period('M')

# it groups by year-month and sum total revenue
monthly_rev = df_clean.groupby('year_month')['total_revenue'].sum()

# coverts the date time for plotting
monthly_rev.index = monthly_rev.index.to_timestamp()


# Plots revenue trends
plt.figure(figsize=(12, 7))
plt.plot(monthly_rev.index, monthly_rev.values, marker='o', linestyle='-', color='black')

# Add titles and labels
plt.title("Monthly Revenue Trends")
plt.xlabel("Month")
plt.ylabel("The Total Revenue")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=1)

# Show the plot
plt.show()
