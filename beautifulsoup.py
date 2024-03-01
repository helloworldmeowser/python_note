#Scraping HTML Data with BeautifulSoup
from urllib.request import urlopen
from bs4 import BeautifulSoup #pip install beautifulsoup4 first
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Initialize the sum of numbers
total_sum = 0

# Retrieve all of the anchor tags
tags = soup.find_all('span')
for tag in tags:
    # Directly find and sum numbers within each tag
    numbers = re.findall("[0-9]+", str(tag))
    total_sum += sum(int(number) for number in numbers)

print(total_sum)