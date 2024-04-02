import feedparser
import requests
from bs4 import BeautifulSoup

# Google News RSS feed URL for Bitcoin
rss_url = "https://news.google.com/rss/search?q=bitcoin"

# Parse the RSS feed
feed = feedparser.parse(rss_url)

titles = []
# Iterate over the news articles
for entry in feed.entries:
    title = entry.title
    link = entry.link
    published_date = entry.published
    description = entry.description
    
    # Print the basic news article data
    print(f"Title: {title}")
    print(f"Link: {link}")
    print(f"Published Date: {published_date}")
    print(f"Description: {description}")
    titles.append(title)

len(feed.entries)

titles