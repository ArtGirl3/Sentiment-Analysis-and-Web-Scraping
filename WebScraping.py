import requests
from bs4 import BeautifulSoup
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon') #Only do this the first time you run the code
#make sure to install the packages: "requests", "BeautifulSoup4", "pandas", "nltk" before starting.

###### WEB SCRAPING #####

#url of website you are trying to scrape.
url = 'https://catalog.feedbooks.com/page/best_sellers'

#request data from the url and ensure you only get html
response = requests.get(url, headers = {"Accept": "text/html"})

#Use python's built-in html parser and store response in variable "parsed_response"
parsed_response = BeautifulSoup(response.text, 'html.parser')

#html code has now been retrieved from the webpage. Prettify() makes it more readable.
#print(parsed_response.prettify())

##### Getting specific results from the data #####


try:
    titles = parsed_response.find_all('h1')
    for title in titles:
        print(title)
    print('sorted response')
except:
    print("unable to sort response")



