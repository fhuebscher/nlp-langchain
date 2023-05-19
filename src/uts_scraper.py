import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

# Set the domain you want to crawl
domain = 'https://www.uts.edu.au'

# Initialize the set of visited URLs
visited_urls = set()

# Define a recursive depth-first search function
def dfs(url):
    # Check if the URL has already been visited
    if url in visited_urls:
        return
    
    print(url)
    # Add the URL to the set of visited URLs
    visited_urls.add(url)
    
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all the links in the HTML code
    links = soup.find_all('a')
    
    # Traverse the links and recursively call the dfs function
    for link in links:
        href = link.get('href')
        if href is not None:
            # Build the absolute URL using urljoin
            absolute_url = urljoin(url, href)
            
            # Check if the absolute URL belongs to the same domain
            if urlparse(absolute_url).netloc == urlparse(domain).netloc:
                dfs(absolute_url)
                
                
# Start the depth-first search from the domain URL
dfs(domain)

# Print the list of visited URLs
for url in visited_urls:
    print(url)