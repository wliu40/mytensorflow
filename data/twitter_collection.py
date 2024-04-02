import tweepy

# Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Specify the username of the user you want to scrape tweets from
username = "duoctongn"

# Retrieve tweets from the user
tweets = api.user_timeline(screen_name=username, count=200)

# Process and print the scraped tweets
for tweet in tweets:
    print(tweet.text)

