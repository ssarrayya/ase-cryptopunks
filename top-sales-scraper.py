import requests
import json
import pandas as pd
from bs4 import BeautifulSoup


def fetch_cryptopunks_html():
    # make a request to the target website
    url = "https://cryptopunks.app/cryptopunks/topsales"
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

    # find all the elements in parent div
    nft_elements = soup.find_all("div", {"class": "col-md-2 col-sm-3 col-xs-6 container-punk-event-large"})

    # iterate through the elements
    crypto_punks = []
    for nft in nft_elements:
        # extract the information needed from our observation of the structure
        crypto_punks.append({
            "crypto_punk": nft.text.strip().replace("\n", " "),
            "image": nft.find("img")['src']
        })

    return crypto_punks


# fetch CryptoPunk's HTML content
html = fetch_cryptopunks_html()

# extract our data from the HTML document
cryptos = extract_info(html)

# save results to JSON file
with open("cryptopunks.json", "w") as f:
    f.write(json.dumps(cryptos, indent=2))

# convert JSON file to CSV file
df = pd.read_json(r'C:\web-scraper\cryptopunks.json')
df.to_csv(r'C:\web-scraper\cryptopunks.csv', index=None)
