import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# URL of the website to scrape
url = 'https://example.com'

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the elements you want to scrape
# For example, let's scrape all the <a> tags
links = soup.find_all('a')

# Create a list to store the data
data = []

# Extract the text and href attributes from each link
for link in links:
    data.append({
        'text': link.get_text(),
        'href': link.get('href')
    })

# Convert the list to a DataFrame
df = pd.DataFrame(data)

# Ensure the data directory exists
output_dir = '../data'
os.makedirs(output_dir, exist_ok=True)

# Save the DataFrame to a CSV file
output_file = os.path.join(output_dir, 'output.csv')
df.to_csv(output_file, index=False)

print(f'Scraping complete. Data saved to {output_file}')