import yfinance as yf
import pandas as pd
from ntscraper import Nitter

def fetch_stock_data(ticker, start_date, end_date, interval='1d'): # Changed default to 1d
    try:
        print(f"Fetching data for {ticker}...")
        stock_df = yf.download(ticker, start=start_date, end=end_date, interval=interval)
        if stock_df.empty:
            print("No data found, check ticker or dates.")
        return stock_df
    except Exception as e:
        print(f"Error fetching stock data: {e}")
        return pd.DataFrame()

# In the notebook Cell 2, try this:
nvda_prices = fetch_stock_data("NVDA", "2025-06-01", "2026-02-01", interval='1d')

def fetch_twitter_data(term, count=100):
    """
    Scrapes recent tweets containing a specific term/cashtag using Nitter.
    """
    print(f"Scraping tweets for {term}...")
    scraper = Nitter()
    tweets = scraper.get_tweets(term, mode='term', number=count)
    
    data = []
    for tweet in tweets['tweets']:
        data.append([tweet['date'], tweet['text'], tweet['stats']['likes'], tweet['stats']['retweets']])
    
    df = pd.DataFrame(data, columns=['timestamp', 'text', 'likes', 'retweets'])
    return df

if __name__ == "__main__":
    # Test the fetcher
    nvda_prices = fetch_stock_data("NVDA", "2024-01-01", "2024-12-31")
    nvda_prices.to_csv("data/nvda_prices.csv")
    print("Stock data saved to data/nvda_prices.csv")