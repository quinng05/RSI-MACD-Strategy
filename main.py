from data_loader import fetch_data
from indicators import add_indicators
# from strategy import generate_signals
# from backtest import backtest_strategy
# from visualization import plot_results

def main():
    # Test data fetching
    ticker = "AAPL"
    interval = "1m"
    period = "8d"

    # Fetch data
    data = fetch_data(ticker=ticker, interval=interval, period=period)

    # Add MACD and RSI to dataframe
    data = add_indicators(data)

    # Convert dataframe to excel file
    data.to_excel("data.xlsx")
    print("Exported data to excel")
    print(data.head())  # Print the first few rows of the data



if __name__ == "__main__":
    main()



