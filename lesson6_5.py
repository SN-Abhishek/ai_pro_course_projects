age = 10

print(f"Checking ticket price for age: {age}")

# Now, let's write our conditional logic
if age < 13:
    # This block runs if the age is less than 13
    ticket_price = 8.00
    print(f"Child ticket price: ${ticket_price}")
elif age >= 65:
    # This block runs ONLY if the first condition was false,
    # and this new condition is true.
    ticket_price = 7.00
    print(f"Senior ticket price: ${ticket_price}")
else:
    # This block runs if ALL of the above conditions were false.
    # This covers everyone from 13 up to 64.
    ticket_price = 12.00
    print(f"Adult ticket price: ${ticket_price}")

print("--- End of transaction ---")
