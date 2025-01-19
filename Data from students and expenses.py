# Filter the data for "Tutoring Lesson Expense" and corresponding "Sales" (income from tutoring)
tutoring_data = sheet_data[sheet_data['Category'].str.contains("Tutoring Lesson Expense|Sales", case=False, na=False)]

# Calculate total income and expense specifically for tutoring
tutoring_summary = tutoring_data.groupby('Category')['Amount'].sum()

# Plotting tutoring-related data
plt.figure(figsize=(8, 5))
tutoring_summary.plot(kind='bar', color=['red', 'green'], edgecolor='black')
plt.title('Tutoring Income and Expenses (2024)', fontsize=16)
plt.ylabel('Total Amount (ZAR)', fontsize=12)
plt.xlabel('Category', fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Display the plot
plt.show()

# Function to print the tutoring summary data
def print_tutoring_summary(data):
    print("Tutoring Income and Expense Summary:")
    print(data)

# Print the tutoring-related summary data
print_tutoring_summary(tutoring_summary)
