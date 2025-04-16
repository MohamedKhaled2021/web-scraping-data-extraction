# Ensure required libraries are installed
try:
    import requests
    from bs4 import BeautifulSoup
except ImportError as e:
    print("Missing library:", e.name)
    print("Please install it using: pip install", e.name)
    exit(1)

# Updated URL to scrape
url = 'https://www.wikipedia.org/'

# Send a GET request
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Extract data (example: all paragraph texts)
paragraphs = [p.text for p in soup.find_all('p')]

# Save to a file
with open('scraped_data.txt', 'w') as file:
    for paragraph in paragraphs:
        file.write(paragraph + '\n')

print("Data scraped and saved to scraped_data.txt")