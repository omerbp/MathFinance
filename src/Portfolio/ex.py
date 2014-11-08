# Download some historical data
from pandas.io.data import DataReader # @UnresolvedImport
from pandas.io.data import get_data_yahoo,get_data_google# @UnresolvedImport 
import matplotlib.pyplot as plt  # @UnresolvedImport
import numpy as np
 
def print_full(x):
    for i in xrange(len(x)):
        print x[i]
# SP = DataReader("^GSPC", "yahoo",start='2012/01/01', end='2013/12/01')
# SP.reset_index(inplace=True)
# print(SP.columns)
 
ohlc_data = get_data_yahoo(['AAPL','SPY'], start='1990/01/01', end='2013/12/01')
data = ohlc_data['Close']
# print data.axes


data.plot(x=data.index,y=['AAPL',"SPY"])#,style='o')

plt.show()


gains1 = np.diff(data['AAPL'])/data['AAPL'][:-1]

print sorted(data['AAPL'])[:3]
print gains1[:2]

gains2 = np.diff(data['SPY'])/data['SPY'][:-1]
tr = gains1-gains2
#print_full(tr)

# gains1 = np.zeros_like(r1.adj_close)
# gains2 = np.zeros_like(r2.adj_close)
# gains1[1:] = np.diff(r1.adj_close)/r1.adj_close[:-1]
# gains2[1:] = np.diff(r2.adj_close)/r2.adj_close[:-1]
# r1 = mlab.rec_append_fields(r1, 'gains', gains1)
# r2 = mlab.rec_append_fields(r2, 'gains', gains2)

