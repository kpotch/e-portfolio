# firstname_lastname_grades.py
# This program collects test grades from the user, stores them in a list,
# and performs various operations such as calculating the average,
# sorting, reversing, and finding min/max values.

grades = []  # List to store grades

print("Enter test grades one by one.")
print("Enter -1 to stop entering grades.\n")

while True:
    try:
        grade = float(input("Enter a grade: "))
        
        if grade == -1:  # Sentinel value to stop input
            break
        
        grades.append(grade)  # Add grade to list
    
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# Check if any grades were entered
if len(grades) == 0:
    print("\nNo grades were entered.")
else:
    # Calculate average
    average = sum(grades) / len(grades)
    
    # Sort grades (lowest to highest)
    grades.sort()
    
    # Display results
    print("\n--- Results ---")
    
    print(f"Average grade: {average:.2f}")
    
    print("\nGrades (Lowest to Highest):")
    print(grades)
    
    print("\nGrades (Highest to Lowest):")
    print(list(reversed(grades)))
    
    print(f"\nLowest grade: {grades[0]}")
    print(f"Highest grade: {grades[-1]}")
