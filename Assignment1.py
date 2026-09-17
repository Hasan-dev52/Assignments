# Student Data Management Using Python Collections

students = {
    127: ("Andrew", "CSE", 85),
    128: ("John", "ECE", 94),
    129: ("Alice", "ME", 95),
    130: ("Bob", "CSE", 80)
}

# List of student records
student_list = [
    (127, "Andrew", "CSE", 85),
    (128, "John", "ECE", 94),
    (129, "Alice", "ME", 95),
    (130, "Bob", "CSE", 80)
]

# Add a new student record
students[131] = ("David", "IT", 88)

# Delete an existing student record
del students[127]

# Update details of a student
students[128] = ("John", "CSE", 92)

# Display final student records
print("Final Student Records:")
for roll_no, details in students.items():
    print("Roll No:", roll_no, "Name:", details[0], 
          "Branch:", details[1], "Marks:", details[2])