try:
    numerator = 10
    # The input() function gets text from the user.
    # The int() function tries to convert that text to an integer.
    user_input = input("Enter a number to divide by: ")
    denominator = int(user_input)

    result = numerator / denominator
    print(f"The result is {result}")

except ZeroDivisionError:
    # This block ONLY runs if the user enters 0.
    print("Error: You can't divide by zero! Please run the program again.")

except ValueError:
    # This block ONLY runs if int() fails (e.g., user enters "hello").
    print("Error: You must enter a valid whole number! Please run the program again.")

except Exception as e:
    # This is a good practice. It's a general catch-all for any OTHER
    # unexpected error. 'e' will hold the error message.
    print(f"An unexpected error occurred: {e}")

finally:
    # The 'finally' block is special. It ALWAYS runs,
    # whether there was an error or not.
    # It's perfect for cleanup tasks.
    print("\\\\n--- Calculation attempt finished ---")

