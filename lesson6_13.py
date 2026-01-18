import os
from dotenv import load_dotenv

# First, we import the necessary toolkits: 'os' to interact with the
# operating system, and 'load_dotenv' from our new library.

# This is the magic line. It finds the .env file and loads the
# variables from it into the environment for our script to use.
load_dotenv()

# Now, we can securely get our secret key using the os module's
# getenv() function. We pass it the key name we want to retrieve.
my_secret_key = os.getenv("OPENAI_API_KEY")

# Let's write some code to check if it worked.
if my_secret_key:
    # As a security best practice, we can show a small part of the key
    # for confirmation, but we should NEVER print the whole secret key!
    print(f"Successfully loaded API key. It starts with: {my_secret_key[:6]}...")
else:
    print("Error: Could not find the API key. Make sure your .env file is correct.")

