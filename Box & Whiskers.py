import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

fifa = pd.read_csv("/Users/thega/Downloads/fifa_data.csv")

barcelona = fifa.loc[fifa.Club == "FC Barcelona"]["Overall"]
madrid = fifa.loc[fifa.Club == "Real Madrid"]["Overall"]
rev = fifa.loc[fifa.Club == "New England Revolution"]["Overall"]

labels = ["FC Barcelona", "Real Madrid", "New England Revolution"]

plt.boxplot([barcelona, madrid, rev ], labels=labels, patch_artist = True, medianprops={'linewidth':2})



#boxes = plt.boxplot([barcelona, madrid, rev ], labels=labels )
#for box in boxes["boxes]:
    #box.set(colors="blue", linewidth=2)
    
    #change fill colour
    #box.set(facecolor="red")

plt.title("Soccer Teams")
plt.ylabel("Fifa Overall")


plt.legend()

plt.show()