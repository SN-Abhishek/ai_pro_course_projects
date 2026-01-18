import requests

print("\n--- Random Quote from the Internet ---")

url = "https://zenquotes.io/api/random"
response = requests.get(url)
data = response.json()

print(f"'{data[0]['q']}' - {data[0]['a']}") 