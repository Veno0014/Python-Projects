# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

fifa = pd.read_csv("/Users/thega/Downloads/fifa_data.csv")

#Pie Chart

left = fifa.loc[fifa["Preferred Foot"] == "Left"].count()[0]
right = fifa.loc[fifa["Preferred Foot"] == "Right"].count()[0]

labels = ["Left", "Right"]
colors = ['red', 'blue']

plt.pie([left, right], labels = labels, colors = colors, autopct ="%.2f %%" )

plt.title("Preferred Feet")

plt.legend()

plt.show()