# Data Cleaning & Visualization Project

## Project Overview
This project focuses on cleaning, processing, and visualizing a raw employee dataset using Python.

## Technologies Used
- Python
- Pandas
- Matplotlib

## Dataset Details
The dataset contains the following columns:
- Name
- Age
- Salary
- Join Date
- Department

## Data Cleaning Steps
- Identified and handled missing values.
- Removed duplicate records.
- Handled outliers in the Salary column using the IQR method.
- Converted Join Date into datetime format.
- Applied One-Hot Encoding to the Department column.

## Data Visualization
Created the following visualizations:
1. Bar Chart – Department Distribution
2. Histogram – Salary Distribution
3. Line Graph – Salary vs Age
4. Scatter Plot – Salary vs Age by Department

## Project Outcome
Successfully cleaned and processed the employee dataset and created visualizations to understand employee salary, age, and department distribution.

## How to Run
1. Install the required libraries:
   `pip install pandas matplotlib`
2. Keep `raw_dataset.csv` and the Python file in the same folder.
3. Run the Python file:
   `python data.py`
