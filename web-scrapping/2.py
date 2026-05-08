from bs4 import BeautifulSoup

# 1. Load the HTML file from your local machine
with open("practice.html", "r") as file:
    html_content = file.read()

# Create the soup object
soup = BeautifulSoup(html_content, 'html.parser')

print("--- 1. Find Element by ID ---")
# Let's grab the header using its unique ID
header = soup.find(id="main-header")
print(header.h1.text) 
# Output: Scraping Practice Site


print("\n--- 2. Find Element(s) by Class ---")
# Let's find all divs that have the class 'urgent'
urgent_news = soup.find_all(class_="urgent")
for news in urgent_news:
    # Extract the h3 title from within that div
    print(f"URGENT: {news.h3.text}")


print("\n--- 3. Searching the Tree ---")
# Sometimes you need to narrow down your search area first.
# Step A: Find the specific section
status_section = soup.find(id="server-status")

# Step B: Search *inside* that section for offline servers
offline_spans = status_section.find_all('span', class_='status-offline')
for span in offline_spans:
    print(f"Found offline server status: {span.text}")


print("\n--- 4. Find all Child Elements ---")
# Let's find the unordered list (ul) and extract all list items (li)
ul_element = soup.find('ul', class_='node-list')

# .findChildren() returns a list of all elements nested directly inside
children = ul_element.findChildren("li")

print(f"Found {len(children)} server nodes:")
for child in children:
    # .text strips away the HTML tags and gives us just the raw string
    print(child.text)