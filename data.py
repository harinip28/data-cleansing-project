import pandas as pd

# Load the dataset
data = pd.read_csv("raw_dataset.csv")

print(data)

# Identify Missing Values
print("\nMissing Values Count:")
print(data.isnull().sum())


# Handle Missing Values

data['Age'] = data['Age'].fillna(data['Age'].median())

data['Salary'] = data['Salary'].fillna(data['Salary'].mean())

data = data.dropna(subset=['Join Date'])

print("\nAfter Handling Missing Values:")
print(data)


# Check and Remove Duplicate Rows

data = data.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

data = data.apply(lambda x: x.str.lower() if x.dtype == "object" else x)

print("\nBefore Removing Duplicates:")
print(data)

data = data.drop_duplicates(subset=['Name', 'Age'])

print("\nAfter Removing Duplicates:")
print(data)

print("\nDuplicate Count:")
print(data.duplicated().sum())


# Handle Outliers

# Calculate IQR for Salary

Q1 = data['Salary'].quantile(0.25)

Q3 = data['Salary'].quantile(0.75)

IQR = Q3 - Q1

# Filter Out Outliers

data = data[
    (data['Salary'] >= Q1 - 1.5 * IQR) &
    (data['Salary'] <= Q3 + 1.5 * IQR)
]

print("\nAfter Handling Outliers:")
print(data)


# Convert Data Types

data['Join Date'] = pd.to_datetime(data['Join Date'])

print("\nData Types:")
print(data.dtypes)


# One-Hot Encode the Department Column

data = pd.get_dummies(
    data,
    columns=['Department'],
    drop_first=True
)

# Convert One-Hot Encoded Columns to Integers

binary_columns = [
    col for col in data.columns
    if col.startswith('Department_')
]

data[binary_columns] = data[binary_columns].astype(int)

print("\nEncoded Dataset:")
print(data)


# Save the Dataset

data.to_csv("cleaned_dataset.csv", index=False)

print("\nDataset Saved Successfully!")


# Visualization

import matplotlib.pyplot as plt

# Load Cleaned Dataset

data = pd.read_csv("cleaned_dataset.csv")

# Display First Few Rows

print("\nCleaned Dataset:")
print(data.head())


# Bar Chart

department_counts = data[binary_columns].sum()

department_counts.plot(
    kind='bar',
    color=['blue', 'green'],
    figsize=(8, 6)
)

plt.title("Department Distribution")

plt.xlabel("Department")

plt.ylabel("Number of Employees")

plt.show()


# Histogram

plt.figure(figsize=(8, 6))

plt.hist(
    data['Salary'],
    bins=10,
    color='orange',
    edgecolor='black'
)

plt.title("Salary Distribution")

plt.xlabel("Salary")

plt.ylabel("Frequency")

plt.grid(True)

plt.show()


# Line Plot

plt.figure(figsize=(8, 6))

plt.plot(
    data['Age'],
    data['Salary'],
    marker='o',
    linestyle='-',
    color='purple'
)

plt.title("Salary vs Age")

plt.xlabel("Age")

plt.ylabel("Salary")

plt.grid(True)

plt.show()


# Scatter Plot for Salary and Department

plt.figure(figsize=(8, 6))

colors = [
    'blue' if dept == 1 else 'green'
    for dept in data['Department_hr']
]

plt.scatter(
    data['Salary'],
    data['Age'],
    c=colors,
    alpha=0.7,
    edgecolor='black'
)

plt.title("Salary vs Age by Department (HR in Blue & Others in Green)")

plt.xlabel("Salary")

plt.ylabel("Age")

plt.grid(True)

plt.show()

print("\nPROJECT COMPLETED SUCCESSFULLY!")
