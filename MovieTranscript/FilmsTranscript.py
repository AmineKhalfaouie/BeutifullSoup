from bs4 import BeautifulSoup
import requests

# Set the root URL for the website
root = 'https://subslikescript.com'

# Specify the main URL for movies on the website
website = f'{root}/movies'

# Make a GET request to the specified URL
request = requests.get(website)

# Get the HTML content of the page
content = request.text

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(content, 'lxml')

# Find the main article section on the page
box = soup.find('article', class_='main-article')

# Create a list to store movie links
links = []

# Extract all the movie links from the main article section
for link in box.find_all('a', href=True):
    links.append(link['href'])

# Print the list of movie links
print(links)

# Iterate through each movie link and extract transcript
for link in links:
    # Build the full URL for each movie page
    website = f'{root}/{link}'

    # Make a GET request to the movie page
    request = requests.get(website)

    # Get the HTML content of the movie page
    content = request.text

    # Create a new BeautifulSoup object to parse the movie page HTML
    soup = BeautifulSoup(content, 'lxml')

    # Find the main article section on the movie page
    box = soup.find('article', class_='main-article')

    # Extract the movie title from the h1 tag
    title = box.find('h1').get_text()

    # Extract the movie transcript from the div with class 'full-script'
    transcript = box.find('div', class_='full-script').get_text(strip=True, separator='\n')

    # Write the movie transcript to a text file with the movie title as the filename
    with open(f'{title}.txt', 'w', encoding='utf-8') as file:
        file.write(transcript)
