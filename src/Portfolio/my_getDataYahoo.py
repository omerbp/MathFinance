from FinanceDataScarping.fetchFromYahoo import getDataYahoo
from pandas import DataFrame,tseries
import numpy as np
import matplotlib.pyplot as plt
from Utilities import Plot


ohlc_data = getDataYahoo(['AAPL','SPY'], start='1995/01/10', end='1995/01/25') #Y(m-1)D
data = ohlc_data

gains1 = np.diff(data['AAPL']['adj_close'])/data['AAPL']['adj_close'][:-1]
gains1[data['AAPL'].index[0]] = 0.0

gains2 = np.diff(data['SPY']['adj_close'])/data['SPY']['adj_close'][:-1]
gains2[data['SPY'].index[0]] = 0.0
 
g = gains1-gains2
g.name = 'g_i'
tr = (1+g).cumprod()
tr.name = "total_revenue"

#add the index
csvData = DataFrame(data['AAPL'][:-1],columns=[])

#add the 
csvData['AAPL_adj_close'] = data['AAPL']['adj_close'][:-1]
csvData['SPY_adj_close'] = data['SPY']['adj_close'][:-1]
print csvData
print data['AAPL']['adj_close']
#adding g_i and total_revenue
csvData['g_i'] = g
csvData['total_revenue'] = tr
print type(csvData.index) 
csvData.index = csvData.index.map(lambda x: x.date())
print csvData.index

# z = DataFrame(csvData,columns=['AAPL_adj_close','SPY_adj_close'])
# print z
# DataFrame.plot(z,use_index=True,title="Portfolio")
# plt.show()


Plot.plotDataFrame(csvData,['AAPL_adj_close','SPY_adj_close'], "the stocks")
