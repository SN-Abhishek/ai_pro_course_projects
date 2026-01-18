def add_two_numbers(num1, num2):
    # This function doesn't print anything.
    # It just performs a calculation and returns the result.
    result = num1 + num2
    return result

# Call the function and store the returned value in a new variable
sum_of_numbers = add_two_numbers(5, 10)

print(f"The result from our function is: {sum_of_numbers}")

# Now we can use this result for other things
print(f"Double the result is: {sum_of_numbers * 2}")
