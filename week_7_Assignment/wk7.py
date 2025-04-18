import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load the iris dataset from sklearn and convert it to a pandas dataframe and handle possible errors during file reading
try:
    # Load the iris dataset
    iris = load_iris()
except FileNotFoundError as e:
    print(f"Error: {e}")
    print("Please check the file path and try again.")
    exit(1)
except ValueError as e:
    print(f"Error: {e}")
    print("Please check the file format and try again.")
    exit(1)

# Convert the iris dataset to a pandas dataframe
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Ensure all columns are printed
pd.set_option('display.max_columns', None)

# examine the first 5 rows of the dataframe
print("\nFirst 5 rows of the iris dataset:")
print(iris_df.head())

# check for missing values
print("\nCheck for missing values in the dataset:")
print(iris_df.isnull().sum())

# check the data types of the columns
print("\nData types of the columns in the dataset:")
print(iris_df.dtypes)

# summary statistics of the dataframe
print("\nSummary statistics of the iris dataset:")
print(iris_df.describe())

# Group the data by species and calculate the mean of each measurement for each species
grouped_iris = iris_df.groupby(iris.target).mean()
print("\nMean measurements for each species:")
print(grouped_iris)

# Visualize the data using a line chart
plt.figure(figsize=(10, 6))
sns.lineplot(data=iris_df, palette="tab10", linewidth=2.5)
plt.title("Iris Dataset Measurements Linechart")
plt.xlabel("Sample Index")
plt.ylabel("Measurement Value")
plt.legend(iris.feature_names)
plt.show()

# Visualize the data using a bar chart
plt.figure(figsize=(10, 6))
sns.barplot(data=iris_df, palette="tab10")
plt.title("Iris Dataset Measurements Bar Chart")
plt.xlabel("Sample Index")
plt.ylabel("Measurement Value")
plt.legend(iris.feature_names)
plt.show()

# visualize using a  histogram
plt.figure(figsize=(10, 6))
sns.histplot(data=iris_df, kde=True, bins=30)
plt.title("Iris Dataset Measurements Histogram")
plt.xlabel("Measurement Value")
plt.ylabel("Frequency")
plt.legend(iris.feature_names)
plt.show()

# visualize using a scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=iris_df, x=iris.feature_names[0], y=iris.feature_names[1], hue=iris.target, palette="tab10")
plt.title("Iris Dataset Scatter Plot")
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.legend(iris.target_names)
plt.show()