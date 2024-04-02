import requests
from bs4 import BeautifulSoup

# Specify the username of the user you want to scrape tweets from
username = "duoctongn"

# Send a GET request to the user's Twitter page
url = f"https://twitter.com/{username}"
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all the tweet elements on the page
tweet_elements = soup.select('div[data-testid="tweet"]')

# Extract the text and other relevant information from each tweet
for tweet_element in tweet_elements:
    # Extract the tweet text
    tweet_text = tweet_element.find('div', {'class': 'css-901oao'}).get_text(strip=True)
    
    # Extract the tweet timestamp
    tweet_timestamp = tweet_element.find('time')['datetime']
    
    # Extract the number of likes and retweets
    tweet_stats = tweet_element.find_all('div', {'class': 'css-1dbjc4n'})
    tweet_likes = tweet_stats[0].get_text(strip=True)
    tweet_retweets = tweet_stats[1].get_text(strip=True)
    
    # Print the extracted information
    print("Tweet Text:", tweet_text)
    print("Timestamp:", tweet_timestamp)
    print("Likes:", tweet_likes)
    print("Retweets:", tweet_retweets)
    print("---")