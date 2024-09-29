import matplotlib.pyplot as plt
import numpy as np

# 4.1 Data from the table
years = [2019, 2020, 2021, 2022, 2023]
fict = [120, 110, 130, 125, 140]
non_fict = [95, 100, 110, 115, 120]
child_books = [55, 65, 70, 75, 80]
textbooks = [80, 85, 75, 90, 95]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 7))


#  4.2 Generating Bar Graph
bar1 = plt.bar(years, fict, label='Fiction', color='lightblue')
bar2 = plt.bar(years, non_fict, label='Non-Fiction', bottom=fict, color='yellow')
bar3 = plt.bar(years, child_books, label="Children's Books", bottom=np.array(fict) + np.array(non_fict), color='grey')
bar4 = plt.bar(years, textbooks, label='Textbooks', bottom=np.array(fict) + np.array(non_fict) + np.array(child_books), color='lightgreen')

# 4.5 Segmenting Graphs and adding labels
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., bar.get_y() + height/2., '%d' % int(height), ha='center', va='center', color='black')

# 4.3 placing a label function in each bar
add_labels(bar1)
add_labels(bar2)
add_labels(bar3)
add_labels(bar4)

# 4.4 Adding respective titles
plt.xlabel('Year')
plt.ylabel('Sales (in thousands of dollars)')
plt.title('Sales sales for each book enre between (2019-2023)')
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()
