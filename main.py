import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd 
import data_importer as di

style.use("ggplot")

start_date = dt.datetime(2020,1,1)
end_date = dt.datetime(2019,1,1)
ticker_list = ["JPM"]
di.run_importer(ticker_list, start_date, end_date)

df = di.read_csv_to_df("JPM")
print(df.head(5))

df["100ma"] = df["Adj Close"].rolling(window = 100, min_periods = 0).mean()

ax1 = plt.subplot2grid((6,1),(0,0),rowspan=5, colspan = 1)
ax2 = plt.subplot2grid((6,1),(5,0),rowspan=1, colspan = 1, sharex=ax1)
ax1.plot(df.index, df["Adj Close"])
ax1.plot(df.index, df["100ma"])
ax2.plot(df.index, df["Adj Close"])
#df[["Open","Close"]].plot()
#plt.show()