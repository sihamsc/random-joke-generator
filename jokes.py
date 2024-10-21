import requests

def get_joke():
    """Fetch a random joke from the Joke API"""
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)

    if response.status_code == 200:
        joke = response.json()
        setup = joke['setup']
        punchline = joke['punchline']
        return f"{setup} - {punchline}"
    else:
        return "Failed to fetch a joke. Try again!"


if __name__ == "__main__":
    joke = get_joke()
    print(joke)
