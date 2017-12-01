import requests
from bs4 import BeautifulSoup

url = "https://nfl.com/injuries"
soup_parser = "html.parser"
r = requests.get(url)
if r.status_code == 200 and r.text:
    soup = BeautifulSoup(r.text, soup_parser)
    with open("scrape.html", "w") as file:
        file.write(soup.prettify())
    print("Done.")
else:
    print("Could not scrape data from {0}" % url)
