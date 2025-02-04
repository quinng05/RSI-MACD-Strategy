import pandas as pd
import yfinance as yf

def clean_timezeone_data(data):
    """
    Removes timezone information for seamless excel conversion

    :param data (pandas.DataFrame): Fetched OHLC data
    :return:
    """

    # Removes timezone from the index if present
    if data.index.tz:
        data.index = data.index.tz_localize(None)

    # Remove timezone from data columns
    for col in data.select_dtypes(include=["datetimetz"]).columns:
        data[col] = data[col].dt.tz_localize(None)

    return data



def fetch_data(ticker, interval="1m", period="7d", source="yfinance"):
    """
        Fetch historical OHLC data using yfinance.

        Args:
            ticker (str): The stock or forex symbol
            interval (str): The time interval for the data
            period (str): The length of time to fetch data for

        Returns:
            pandas.DataFrame: A DataFrame containing the historical data.
        """

    # Handles data import for yfinance
    if source == "yfinance":
        print(f"Fetching Yahoo data for {ticker} with interval '{interval}' and period '{period}'...")
        data = yf.download(tickers=ticker, interval=interval, period=period)

        # Flatten MultiIndex data from yfinance
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = data.columns.get_level_values(0)


    # Handles data import for Bloomberg terminal
    elif source == "terminal":
        print(f"Fetching Terminal data for {ticker} with interval '{interval}' and period '{period}'...")
        data = None

    if data.empty:
        raise ValueError("No data fetched. Check the ticker, interval, or period.")
    print(f"Data fetched! {len(data)} rows retrieved.")

    data = clean_timezeone_data(data)

    return data