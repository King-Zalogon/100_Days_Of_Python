import requests


def get_random_quote():

    url = "https://zenquotes.io/api/random/"

    # Send a GET request to the API
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Get the quote from the response JSON
        quote = data[0]['q']

        return quote
    else:
        return False
