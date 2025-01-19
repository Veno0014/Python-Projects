import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load gas prices data
gas_prices = pd.read_csv("/Users/thega/Downloads/gas_prices.csv")

plt.figure(figsize=(8, 5))

# Bar plot for USA
plt.bar(gas_prices.Year - 0.2, gas_prices.USA, width=0.4, color="blue", label="USA")  # Offset years for side-by-side bars
# Bar plot for Canada
plt.bar(gas_prices.Year + 0.2, gas_prices.Canada, width=0.4, color="red", label="Canada")

# Adjust x-ticks for better readability
plt.xticks(gas_prices.Year[::3])  # Show every third year

# Labels and Title
plt.legend()
plt.xlabel("Year")
plt.ylabel("Gas Price (USD per gallon)")
plt.title("Gas Prices Over Time (USA vs Canada)")

# Show plot
plt.show()
