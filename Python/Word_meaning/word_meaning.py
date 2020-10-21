import requests
import sys


def fetch_meaning(user_defined_word):
    """This function takes a user defined word as input, fetches
       response from the dictionary api andreturns the various
       meanings of a word on the command line.

    Args:
        user_defined_word (str): The word whose meaning the user wants to know.
    """

    # Url of the dictionary api
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/"

    # response object of the get requests on the above url, along with the word
    response = requests.get(url+user_defined_word)

    if response.status_code in range(200, 299):  # For successful response
        # response object concerned with the meaning key
        meanings_response = response.json()[0]['meanings']

        # Looping over the meanings response a word may have multiple meanings
        for meanings in meanings_response:

            # Looping over the definition key
            for meaning in meanings['definitions']:
                # Fetching the part of speech for the particular case
                print(f'Part of Speech: {meanings["partOfSpeech"]}')
                # Fetching the meaning as per the part of speech
                print(f'Meaning: {meaning["definition"]} \n')
    # for handling client side errors
    elif response.status_code in range(400, 499):
        sys.exit("Please check your internet or the word you typed")

    # for handling server side errors
    elif response.status_code in range(500, 599):
        sys.exit("Oops a server side error has occured!")


if __name__ == "__main__":
    word = input("Please enter a word: ")
    fetch_meaning(word)
