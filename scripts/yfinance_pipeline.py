import yfinance as yf
import pandas as pd

# Paths for raw and cleaned data
RAW_PATH = "/Users/ahmadazhar/Desktop/Assignment1/datasets/raw/yahoo_finance_raw.csv"
CLEAN_PATH = "/Users/ahmadazhar/Desktop/Assignment1/datasets/clean/yahoo_finance_clean.csv"

# Define target industries
INDUSTRIES = {
    "Consumer Cyclical": ["Travel Services"],
    "Communication Services": ["Broadcasting", "Advertising Agencies"]
}

# List of stock tickers (replace with actual tickers for the industries)
TICKERS = ["EXPE", "BKNG", "IHG", "WPP", "OMC", "NFLX", "DIS"]  # Example tickers

# READ DATA
def fetch_yahoo_finance_data(tickers, raw_path):
    data = []
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        info = stock.info
        history = stock.history(period="2y")  # Fetch last 2 years of data
        
        for date, row in history.iterrows():
            data.append({
                "ticker": ticker,
                "date": date,
                "sector": info.get("sector", "N/A"),
                "industry": info.get("industry", "N/A"),
                "market_cap": info.get("marketCap", 0),
                "current_price": row["Close"],
                "52_week_high": info.get("fiftyTwoWeekHigh", 0),
                "52_week_low": info.get("fiftyTwoWeekLow", 0),
                "dividend_yield": info.get("dividendYield", 0)
            })
    
    df = pd.DataFrame(data)
    df.to_csv(raw_path, index=False)
    print("Raw Yahoo Finance data saved successfully!")
    return df

# DATA PREPROCESS
def data_preprocessing(input_file, output_file):
    df = pd.read_csv(input_file)
    
    # Check for null values
    null_val = df.isnull().sum().sum()
    print(f"Total null values: {null_val}")
    
    # Check for duplicates
    duplicates = df.duplicated().sum()
    print(f"Total duplicate values: {duplicates}")
    
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    
    df.to_csv(output_file, index=False)
    print("Data cleaned and saved successfully!")
    
# ANALYZE DATA
def analyze_data(clean_file):
    df = pd.read_csv(clean_file)
    
    # Find top company by market cap
    top_company = df.loc[df['market_cap'].idxmax(), ['ticker', 'market_cap']]
    print(f"🏆 Largest Market Cap: {top_company['ticker']} (${top_company['market_cap']:,}) 🏆")
    
    # Highest dividend yield
    top_dividend = df.loc[df['dividend_yield'].idxmax(), ['ticker', 'dividend_yield']]
    print(f"💰 Highest Dividend Yield: {top_dividend['ticker']} ({top_dividend['dividend_yield']*100:.2f}%) 💰")

# RUN THE PIPELINE
if __name__ == "__main__":
    df_raw = fetch_yahoo_finance_data(TICKERS, RAW_PATH)
    data_preprocessing(RAW_PATH, CLEAN_PATH)
    analyze_data(CLEAN_PATH)
