import yfinance as yf

def fetch_data(ticker, interval="1m", period="7d"):
    """
        Fetch historical OHLC data using yfinance.

        Args:
            ticker (str): The stock or forex symbol
            interval (str): The time interval for the data
            period (str): The length of time to fetch data for

        Returns:
            pandas.DataFrame: A DataFrame containing the historical data.
        """
    print(f"Fetching data for {ticker} with interval '{interval}' and period '{period}'...")
    data = yf.download(tickers=ticker, interval=interval, period=period)
    if data.empty:
        raise ValueError("No data fetched. Check the ticker, interval, or period.")
    print(f"Data fetched! {len(data)} rows retrieved.")
    return data