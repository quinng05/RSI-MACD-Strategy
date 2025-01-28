from data_loader import fetch_data
# from indicators import add_indicators
# from strategy import generate_signals
# from backtest import backtest_strategy
# from visualization import plot_results

def main():
    # Test data fetching
    ticker = "SPY"
    interval = "1m"
    period = "7d"
    data = fetch_data(ticker=ticker, interval=interval, period=period)
    print(data.head())  # Print the first few rows of the data

if __name__ == "__main__":
    main()



