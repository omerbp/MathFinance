import numpy as np
import pandas
import matplotlib.pyplot as plt
from matplotlib.finance import candlestick, candlestick2
import matplotlib.dates as mdates
from pandas.io.data import DataReader

# get daily stock price data from yahoo finance for S&P500
SP = DataReader("^GSPC", "yahoo")
SP.reset_index(inplace=True)
print(SP.columns)
SP['Date2'] = SP['Date'].apply(lambda date: mdates.date2num(date.to_pydatetime()))
fig, ax = plt.subplots()
csticks = candlestick(ax, SP[['Date2', 'Open', 'Close', 'High', 'Low']].values)
plt.show()