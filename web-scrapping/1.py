import requests
from bs4 import BeautifulSoup

# 1. Fetch the webpage
url = "https://quotes.toscrape.com/"
response = requests.get(url)

# 2. Parse the HTML content
# We pass the raw HTML and tell BS4 which parser to use
soup = BeautifulSoup(response.text, 'html.parser')

# 3. Syntax: Finding a single element
# Access the <title> tag of the page
print(f"Page Title: {soup.title.string}")

# 4. Syntax: Finding all elements
# Let's find all the 'span' tags that have the class 'text' (these are the quotes)
quotes = soup.find_all('span', class_='text')

print("\n--- Latest Quotes ---")
for i, quote in enumerate(quotes[:5], 1):
    print(f"{i}. {quote.text}")

# 5. Syntax: Navigating to find an attribute
# Find the first link (<a> tag) and get its 'href' attribute
first_link = soup.find('a')
print(f"\nFirst Link URL: {first_link['href']}")