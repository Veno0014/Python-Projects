import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

gas_prices = pd.read_csv("/Users/thega/Download/gas_prices.csv")

plt.figure(figsize=(8,5))

plt.plot(gas_prices.Year, gas_prices.USA, "b.-", label = "USA" )
plt.plot(gas_prices.Year, gas_prices.Canada, label = "Canada", color = "red")


print(gas_prices.Year[::3])

plt.xticks(gas_prices.Year[::3])

plt.legend()
plt.xlabel("Year")
plt.ylabel("Gas Price (USD per gallon)")
plt.title("Gas Prices Over Time(USA vs Canada)")

plt.show()