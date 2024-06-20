"""The code to get quotes of EURUSD symbol and to show as charts"""

import requests
import pandas as pd
import matplotlib.pyplot as plt

api_key = 'Demo'
symbol = 'EURUSD'
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=60min&apikey={api_key}'

# Get data over API
response = requests.get(url)
data = response.json()

# Check if 'key' is in data
if 'Time Series (60min)' not in data:
    print("Error: Check if data contains 'Time Series (60min)' key. Verify request and API key.")
    if 'Error Message' in data:
        print("Error:", data['Error Message'])
    elif 'Note' in data:
        print("Message from API:", data['Note'])
else:
    # Convert data to DataFrame
    df = pd.DataFrame(data['Time Series (60min)']).T
    df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
    df.index = pd.to_datetime(df.index)
    df = df.astype(float)

    # Ascending data sorting
    df.sort_index(inplace=True)

    # Creating dataframes
    df_1h = df.resample('1h').last()
    df_4h = df.resample('4h').last()
    df_1d = df.resample('1D').last()

    # Build chart
    plt.figure(figsize=(12, 8))

    # 1h chart
    plt.subplot(3, 1, 1)
    plt.plot(df_1h.index, df_1h['Close'], label='1 Hour')
    plt.title('EUR/USD 1 Hour')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.legend()

    # 4h chart
    plt.subplot(3, 1, 2)
    plt.plot(df_4h.index, df_4h['Close'], label='4 Hours')
    plt.title('EUR/USD 4 Hours')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.legend()

    # 1d chart
    plt.subplot(3, 1, 3)
    plt.plot(df_1d.index, df_1d['Close'], label='1 Day')
    plt.title('EUR/USD 1 Day')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.legend()

    plt.tight_layout()
    plt.show()
