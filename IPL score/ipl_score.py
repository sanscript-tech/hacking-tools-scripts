import requests
from bs4 import BeautifulSoup as bs
import sys


def ipl_score(url):
    """This function takes the liove score website url as input,
       performs operation using soup object and returns the ipl
       score on the command line.

    Args:
        url (string): url of the live score providing website.
    """

    # To handle connection error
    try:
        response = requests.get(url)

    except requests.exceptions.ConnectionError:
        sys.exit("Check your connection please!!")

    soup = bs(response.content, 'html.parser')  # Creating a soup object

    # To handle missing values
    try:
        cricket_divs = soup.findAll(
            "div", {"class": "cb-col-100 cb-col cb-schdl"})
    except Exception:
        cricket_divs = None
        sys.exit("No live Match going on at the present moment.")

    # looping over the divs and printing target values
    for divs in cricket_divs:
        value = divs.find('a')
        print(value.text.strip())

    # for stadium info and match number
    stadium_match_no = soup.findAll("span", {"class": "text-gray"})

    # looping over the stadium info
    for value in stadium_match_no:
        print(value.text.strip(), end=' ')


if __name__ == "__main__":
    print("Current Match Information: \n")
    # Url for the live score fetching
    url = "https://www.cricbuzz.com/cricket-match/live-scores"

    ipl_score(url)
