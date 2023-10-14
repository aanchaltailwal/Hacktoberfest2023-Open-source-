import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = 'https://example.com'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract data by selecting HTML elements using CSS selectors
    # For example, to extract all the links on the page:
    links = soup.find_all('a')
    
    # Iterate through the links and print their text and href attributes
    for link in links:
        link_text = link.get_text()
        link_url = link.get('href')
        print(f"Text: {link_text}, URL: {link_url}")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
