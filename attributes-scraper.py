import requests
import json
import pandas as pd
from bs4 import BeautifulSoup


def fetch_cryptopunks_html():
    # make a request to the target website
    url = "https://cryptopunks.app/cryptopunks/attributes"
    r = requests.get(url)
    if r.status_code == 200:
        # if the request is successful return the HTML content
        return r.text
    else:
        # throw an exception if an error occurred
        raise Exception("an error occurred while fetching cryptopunks html")


def extract_info(doc):
    # parse the HTML content with Beautiful Soup
    soup = BeautifulSoup(doc, "html.parser")

    # find all the elements in attributes table
    punk_attributes = soup.find_all("tr", {"class": "center attribute-row"})
    # atts = punk_attributes.find("tr")

    # iterate through the elements
    crypto_punks = []
    for attribute in punk_attributes:
        # extract the information needed using our observations
        crypto_punks.append({
            "punk_attribute": attribute.text.strip().replace("\n", " "),
        })

    return crypto_punks


# fetch CryptoPunk's HTML content
html = fetch_cryptopunks_html()

# extract our data from the HTML document
cryptos = extract_info(html)

# save results to JSON file
with open("attributes.json", "w") as f:
    f.write(json.dumps(cryptos, indent=2))

# convert JSON file to CSV file
df = pd.read_json(r'C:\web-scraper\attributes.json')
df.to_csv(r'C:\web-scraper\attributes.csv', index=None)
