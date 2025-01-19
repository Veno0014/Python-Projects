import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

fifa = pd.read_csv("/Users/thega/Downloads/fifa_data.csv")

plt.figure(figsize=(8,5))

bin = [40, 50, 60, 70, 80, 90, 100]
plt.hist(fifa.Overall, bins = bin, color = "r")



plt.ylabel("Number of Players")
plt.xlabel("Skill Level")
plt.label("Number of players vs Skill level")

plt.show()


