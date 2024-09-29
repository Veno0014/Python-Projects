import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Entering the Graph Data
experience = np.array([1, 2, 3, 5, 7, 8, 10, 12, 15, 18])
education_level = np.array([0, 0, 1, 1, 0, 2, 1, 2, 1, 2])  
salary = np.array([50, 55, 65, 75, 80, 95, 90, 105, 110, 125])

# Different plot colors for the respective label
plt.figure(figsize=(12, 7))

# Plotting the different education levels
for level, color, label in zip([0, 1, 2], ['red', 'orange', 'brown'], ["Bachelor's", "Master's", 'PhD']):
    plt.scatter(experience[education_level == level], salary[education_level == level], color=color, label=label)

# Printing title and X and Y axis
plt.xlabel("Years of Experience")
plt.ylabel("Salary (in thousands of USD)")
plt.title("Software Engineers Experience vs. Salary by their Education Level")
plt.legend()

# Setting up regression line for the experience level and education level
X = np.column_stack((experience, education_level))

# Organising all plots to fit on a regression momdel
model = LinearRegression()
model.fit(X, salary)

# Printing the coefficients and intercept
print(f" Coefficients (Experience, Education Level): {model.coef_}" )
print(f"Intercept: {model.intercept_}")

# Predicting salary from the examples
prediction_1 = model.predict([[7, 0]])  
prediction_2 = model.predict([[12, 3]]) 

print(f"The predicted salary for a software developer that has 6 years of experience and Bachelor's: {prediction_1[0]:.2f}k USD")
print(f"The predicted salary for a software developer that has 9 years of experience and PhD: {prediction_2[0]:.2f}k USD")

# Adding lines for the best fit
x_range = np.linspace(1, 18, 100)
for level, color in zip([0, 1, 2], ['red', 'orange', 'brown']):
    salaries_fit = model.predict(np.column_stack((x_range, np.full(x_range.shape, level))))
    plt.plot(x_range, salaries_fit, color=color, linestyle='--')

# Highlighting the predictions
plt.scatter([7], [prediction_1[0]], color= "green", label='Prediction (6 years, Bachelor)', s=150, marker='x')
plt.scatter([12], [prediction_2[0]], color="blue", label='Prediction (9 years, PhD)', s=150, marker='x')

plt.legend()
plt.show()
