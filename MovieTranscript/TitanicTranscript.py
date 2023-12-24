from bs4 import BeautifulSoup
import requests

# Specify the URL for a specific movie script page
website = 'https://subslikescript.com/movie/Titanic-120338'

# Make a GET request to the specified URL
request = requests.get(website)

# Get the HTML content of the page
content = request.text

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(content, 'lxml')

# Find the main article section on the page
box = soup.find('article', class_='main-article')

# Extract the movie title from the h1 tag
title = box.find('h1').get_text()

# Extract the movie transcript from the div with class 'full-script'
transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

# Write the movie transcript to a text file with the movie title as the filename
with open(f'{title}.txt', 'w', encoding='utf-8') as file:
    file.write(transcript)
