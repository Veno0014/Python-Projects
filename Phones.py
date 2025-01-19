import pandas as pd
import matplotlib.pyplot as plt
import calendar

# Retrieves and reads CSV file
data = pd.read_csv('phone_sales_2023.csv')

# The purchase date is converted datetime column
data['date_of_purchase'] = pd.to_datetime(data['date_of_purchase'], format='%d/%m/%Y')

# Extracts the brand and month, lambda will shortyen data
data['the month'] = data['date_of_purchase'].dt.month
data['the month'] = data['the month'].apply(lambda x: calendar.month_abbr[x])

# The data is grouped by subtype, brand 
grped = data.groupby(['brand_of_phone', 'the_subtype', 'the month'])['cost']
grped.rename(columns={'cost': 'sales'}, inplace=True)

# Plotting the 2x2 grid
brands = ['Samsung', 'iPhone', 'Xiaomi', 'Huawei']
fig, axes = plt.subplots(2, 2, figsize=(12, 7))

# Each mach will go through for loop
for axes, brand in zip(axes.ravel(), brands):
    # Filtering current brand data
    brnddata = grped[grped['brand_of_phone'] == brand]
    subtypes = brnddata['the_subtype']
    
    # Plotting data
    pivdata = brnddata.pivot(index='the month', columns='the_subtype', values='sales')
   
    # Data is plotted
    pivdata.plot(kind='bar', axes=axes, color=plt.cm.Paired.colors[:len(subtypes)])
    
    # Customize the chart
    axes.set_title(f'{brand} Sales by Subtype (2023)')
    axes.set_ylabel('Sales Count')
    axes.set_xlabel('Month phone was released/purchased')


# Changing layout if need be
plt.layout()
plt.show()
