# import packages

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
# Download and Parse the HTML

print("Please add the URL you want to be Scrapped")
start_url = input("Type the URL you want to scrap: ")

#Download the HTML from the start_url
downloaded_html = requests.get(start_url)

Savingto = input("Where you want to save: ")

#Parse the HTML with BeatifulSoup and create a soup object
soup = BeautifulSoup(downloaded_html.text)

# Save a local copy
with open(Savingto, 'w') as file:
    file.write(soup.prettify())
