import talib
import numpy as np

def add_indicators(data):
    print(f"Columns in data: {data.columns}")

    # Ensure we're working with a clean dataframe
    if "Close" not in data.columns:
        raise KeyError("'Close' column not found in the data")

    close_prices = np.array(data["Close"]).flatten()

    # Calculate MACD using TA-Lib
    macd, macd_signal, macd_hist = talib.MACD(close_prices, fastperiod=12, slowperiod=26, signalperiod=9)

    # Add MACD columns to the dataframe
    data["macd"] = macd
    data["macd_signal"] = macd_signal
    data["macd_hist"] = macd_hist

    # Drop rows where MACD values are NaN (first 26 bars might be NaN)
    data.dropna(subset=["macd", "macd_signal", "macd_hist"], inplace=True)

    print("MACD added!")
    return data
