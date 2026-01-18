import requests
import os
from dotenv import load_dotenv
from groq import Groq # Import the Groq library

load_dotenv() # Load our .env file

# Our get_joke() function stays exactly the same...
def get_joke():
    """Fetches a random joke from a public API and formats it."""
    try:
        api_url = "https://official-joke-api.appspot.com/random_joke"
        response = requests.get(api_url, timeout=5)

        # Raise an error for bad HTTP responses (4xx, 5xx)
        response.raise_for_status()

        # Convert JSON response to dictionary
        data = response.json()

        setup = data["setup"]
        punchline = data["punchline"]

        return f"{setup}\n... {punchline}"

    except requests.exceptions.RequestException as e:
        return f"Error: Could not fetch a joke. Reason: {e}"



# --- NEW AI FUNCTION ---
def analyze_joke_with_ai(joke_text):
    """Sends a joke to an AI model to get its analysis."""
    try:
        # This is how we securely get our API key
        groq_api_key = os.getenv("GROQ_API_KEY")
        if not groq_api_key:
            return "Error: GROQ_API_KEY not found. Please check your .env file."

        client = Groq(api_key=groq_api_key)

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful AI assistant that analyzes jokes."
                },
                {
                    "role": "user",
                    "content": f"Here is a joke: '{joke_text}'. In one short sentence, tell me what kind of joke it is (e.g., a pun, an observation, etc.) and if it's funny."
                }
            ],
            model="llama-3.1-8b-instant",
        )

        # We access the AI's response just like we would with a dictionary
        return chat_completion.choices[0].message.content

    except Exception as e:
        return f"Error analyzing joke with AI: {e}"

# --- Updated Main execution block ---
if __name__ == "__main__":
    # Step 1: Get the joke
    joke = get_joke()
    print("--- Your Random Joke ---")
    print(joke)

    # Step 2: Analyze the joke with AI
    if "Error:" not in joke: # Only analyze if we successfully got a joke
        print("\\\\n--- AI Analysis ---")
        analysis = analyze_joke_with_ai(joke)
        print(analysis)

