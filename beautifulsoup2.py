#Following Links in HTML Using BeautifulSoup
import urllib.request
from bs4 import BeautifulSoup

# Prompt user for input
url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: ')) - 1

for i in range(count):
    # Fetch and read HTML content
    response = urllib.request.urlopen(url)
    html = response.read()

    # Parse HTML
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all('a')  # Find all <a> tags

    # Ensure the position is within the range of links found
    if position < len(links):
        link = links[position].get('href', None)
        print("Retrieving:", link)
        url = link  # Update the URL to the link to follow in the next iteration
    else:
        print("Position out of range.")
        break