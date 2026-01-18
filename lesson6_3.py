# This is a comment. Python ignores anything after a '#' sign.

# 1. Let's create a String variable
student_name = "Alex"

# 2. Now, an Integer variable
student_age = 25

# 3. Next, a Float for a decimal number
progress_percentage = 75.5

# 4. And finally, a Boolean for a True/False value
is_enrolled = True 

# Let's inspect our 'student_name' variable
print("Student Name:", student_name)
print("Type of student_name:", type(student_name))

# Now let's inspect 'student_age'
print("Student Age:", student_age)
print("Type of student_age:", type(student_age))

# And 'progress_percentage'
print("Progress Percentage:", progress_percentage)
print("Type of progress_percentage:", type(progress_percentage))

# Finally, 'is_enrolled'
print("Is Enrolled:", is_enrolled)
print("Type of is_enrolled:", type(is_enrolled))


# Old way: print("Student Name:", student_name)
# New way with f-string:
print(f"Student Name: {student_name}")
print(f"The type is: {type(student_name)}") 

