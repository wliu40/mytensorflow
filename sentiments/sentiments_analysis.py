from nltk.sentiment import SentimentIntensityAnalyzer

# Collect titles from Google RSS, Twitter, and Reddit (example titles)
titles = [
    "Bitcoin Surges to New All-Time High",
    "Ethereum Gains Momentum as DeFi Booms",
    "Crypto Market Faces Uncertainty Amid Regulatory Concerns",
    # ... add more titles
]

analyzer = SentimentIntensityAnalyzer()

normalized_scores = []
for title in titles:
    compound_score = analyzer.polarity_scores(title)['compound']
    normalized_score = (compound_score + 1) * 50
    normalized_scores.append(normalized_score)

average_score = sum(normalized_scores) / len(normalized_scores)

print(f"Crypto Market Sentiment Score: {average_score:.2f}")

if average_score < 50:
    print("Bearish sentiment")
else:
    print("Bullish sentiment")