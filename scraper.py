import requests
import json
import shutil
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

    # find all the elements in collections table
    nft_elements = soup.find_all("div", {"class": "col-md-2 col-sm-3 col-xs-6 container-punk-event-large"})

    # iterate through the elements
    crypto_punks = []
    for nft in nft_elements:
        # extract the information needed using our observations
        crypto_punks.append({
            "crypto_punk": nft.text.strip(),
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
