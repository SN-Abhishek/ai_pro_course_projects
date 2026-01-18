import requests

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


if __name__ == "__main__":
    joke = get_joke()
    print("--- Your Random Joke ---")
    print(joke)

