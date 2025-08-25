import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def fetch_stock_data(ticker, period="1y", interval="1d"):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period, interval=interval)
    if data.empty:
        print(f"❌ No data found for {ticker}.")
    return data

def analyze_stock(data, ticker):
    print(f"\n📊 Statistics for {ticker}:")
    print(f"Mean Closing Price: {data['Close'].mean():.2f}")
    print(f"Max Closing Price: {data['Close'].max():.2f}")
    print(f"Min Closing Price: {data['Close'].min():.2f}")
    print(f"Standard Deviation: {data['Close'].std():.2f}")

def plot_stocks(stock_dict):
    plt.figure(figsize=(12,6))
    
    for ticker, data in stock_dict.items():
        plt.plot(data['Close'], label=f'{ticker} Close')
        # Plot 50-day moving average
        plt.plot(data['Close'].rolling(window=50).mean(), '--', label=f'{ticker} 50-day MA')
        # Plot 200-day moving average
        plt.plot(data['Close'].rolling(window=200).mean(), ':', label=f'{ticker} 200-day MA')
    
    plt.title("Stock Closing Prices & Moving Averages")
    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    tickers = input("Enter stock symbols separated by commas (e.g., AAPL,TSLA,MSFT): ")
    tickers = [t.strip().upper() for t in tickers.split(",")]

    stock_data = {}
    for ticker in tickers:
        data = fetch_stock_data(ticker)
        if not data.empty:
            analyze_stock(data, ticker)
            stock_data[ticker] = data

    if stock_data:
        plot_stocks(stock_data)

if __name__ == "__main__":
    main()
