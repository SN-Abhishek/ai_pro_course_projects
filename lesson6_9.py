# Create a dictionary to hold structured user data
user_profile = {
    "username": "alex_ai_pro",
    "age": 25,
    "is_enrolled": True,
    "courses": ["AI PRO", "Data Science", "Python Basics"]
}

print("--- Original Profile ---")
print(user_profile)


# Access a value using its key
print(f"\\\\nWelcome, {user_profile['username']}!")

# Accessing an item from a list that is inside a dictionary
first_course = user_profile["courses"][0]
print(f"Your first course was: {first_course}")

# Modifying and adding data
user_profile["is_enrolled"] = False
user_profile["has_graduated"] = True

print("\\\\n--- Updated Profile ---")
print(user_profile)

