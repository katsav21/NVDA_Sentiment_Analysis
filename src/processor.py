import pandas as pd
import re

def clean_tweet_text(text):
    """
    Basic text cleaning for tweets: removing links, special characters, and cashtags.
    """
    text = re.sub(r'http\S+', '', text) # Remove URLs
    text = re.sub(r'\$\w+', '', text)   # Remove Cashtags ($NVDA)
    text = re.sub(r'@\w+', '', text)   # Remove Mentions
    text = text.replace('\n', ' ').strip()
    return text

def aggregate_sentiment_by_day(sentiment_df):
    """
    Groups tweets by date and calculates the average sentiment score.
    """
    # Ensure timestamp is datetime
    sentiment_df['timestamp'] = pd.to_datetime(sentiment_df['timestamp'])
    # Group by day and calculate mean sentiment
    daily_sentiment = sentiment_df.groupby(sentiment_df['timestamp'].dt.date)['sentiment_score'].mean()
    return daily_sentiment