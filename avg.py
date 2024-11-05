# List of student grades
grades = [85, 92, 78, 90, 88, 76]

# Function to calculate the average grade
def calculate_average(grades):
    return sum(grades) / len(grades)

# Calculate the average
average_grade = calculate_average(grades)

# Write the result to a text file
with open('average_grade.txt', 'w') as file:
    file.write(f"The average grade is: {average_grade:.2f}\n")

# Print confirmation message
print(f"The average grade has been written to 'average_grade.txt'.")
