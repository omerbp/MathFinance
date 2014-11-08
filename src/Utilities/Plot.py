import matplotlib.pyplot as plt # @UnresolvedImport
from pandas import tseries,DataFrame  # @UnresolvedImport
def plotDataFrame(data,cols,title):
    if (type(data.index) == tseries.index.DatetimeIndex):
        data.index = data.index.map(lambda x: x.date())
    z = DataFrame(data,columns=cols)
    DataFrame.plot(z,use_index=True,title="Portfolio")
    plt.show()
def plotManyPortfolios(prtflList,title):
    data = DataFrame() #only the dates
    for prtf in prtflList:
        data[prtf[1]] = prtf[0]["total_revenue"]
    data.index = data.index.map(lambda x: x.date())
    DataFrame.plot(data,use_index=True,title=title)
    plt.show()