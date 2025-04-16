# Ensure required libraries are installed
try:
    import requests
    from bs4 import BeautifulSoup
    import json
    import csv
except ImportError as e:
    print("Missing library:", e.name)
    print("Please install it using: pip install", e.name)
    exit(1)

# Scrape multiple pages
urls = ['https://www.wikipedia.org/', 'https://www.example.com/']
all_paragraphs = []
for url in urls:
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = [p.text for p in soup.find_all('p')]
        all_paragraphs.extend(paragraphs)
    except requests.exceptions.RequestException as e:
        print(f"Failed to scrape {url}: {e}")

# Save data in multiple formats
with open('scraped_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(all_paragraphs, json_file, ensure_ascii=False, indent=4)

with open('scraped_data.csv', 'w', encoding='utf-8', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Paragraph'])
    for paragraph in all_paragraphs:
        writer.writerow([paragraph])

print("Data scraped and saved in JSON and CSV formats.")