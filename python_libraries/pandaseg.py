import pandas as pd
# Create a DataFrame with 5 students : name, age, grade
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'age': [20, 21, 19, 22, 20],
    'grade': [85, 90, 78, 88, 92]
}
df = pd.DataFrame(data)
# Display the DataFrame
print("Original DataFrame:")
print(df)

# Add a new column 'passed' based on the condition that grade > 87 => True, else False
df['passed'] = df['grade'] > 87
# Display the updated DataFrame
print("\nUpdated DataFrame with 'passed' column:")
print(df)
# Calculate the average grade
average_grade = df['grade'].mean()
print("\nAverage grade:", average_grade)
# Filter students who passed
passed_students = df[df['passed']]
print("\nStudents who passed:")
print(passed_students)