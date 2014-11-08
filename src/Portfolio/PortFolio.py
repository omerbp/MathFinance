from Utilities import ParseDate,listPrint,Plot
from FinanceDataScarping.fetchFromYahoo import getDataYahoo
import numpy as np
from pandas import DataFrame  # @UnresolvedImport
from pandas.io.data import get_data_yahoo # @UnresolvedImport
from portfolio.optimizations.solvers import SolverPortfolio # @UnresolvedImport
import portfolio.objectives as objective # @UnresolvedImport
import portfolio.constraints as constraint # @UnresolvedImport
def Dates():
    return {"start":'2005/01/10',"end":'2014/11/10'} #YYYY/MM/DD
def getPortfolioData(symbList,weightDict,start,end):
    data = getDataYahoo(symbList, start,end)
    #get gains for each symbol
    gains = {}
    csvData = DataFrame(data[symbList[0]][:-1],columns=[])
    for symb in symbList:
        gains[symb] = np.diff(data[symb]['adj_close'])/data[symb]['adj_close'][:-1]
        gains[symb][data[symb].index[0]] = 0.0
    g = sum([weightDict[symb]*gains[symb] for symb in symbList])
    g.name = 'g_i'
    tr = (1+g).cumprod()
    tr.name = "total_revenue"
    for symb in symbList:
        csvData[symb+'_adj_close'] = data[symb]['adj_close'][:-1]
    #adding g_i and total_revenue
    csvData['g_i'] = g
    csvData['total_revenue'] = tr
    print csvData
    csvData.to_csv('PortfolioData.csv')
    #Plot.plotDataFrame(csvData,['total_revenue'], "the revenue")
    #Plot.plotDataFrame(csvData,[symb+'_adj_close' for symb in symbList], "the stocks")
    return csvData
def optimizePortfolio(symbList,start,end):
    ohlc_data = get_data_yahoo(symbList,start,end)
    data = ohlc_data['Close']
    # Now let's optimize our portfolio weights    
    portfolio = SolverPortfolio(objective.expected_return)
    # Forbid short positions
    portfolio.add_constraint(constraint.long_only())
    # Invest every cent of our cash
    portfolio.add_constraint(constraint.full_investment())
    
    # Get optimal weights in %
    return  portfolio.optimize(symbList, data)
def main():
    s = ['YHOO',"AAPL","SPY",'INTC','MSFT',"WMT",'QCOM','BRCM','EBAY','FITB','SBUX','ESLT']
    start,end = Dates()['start'],Dates()['end']
    w = optimizePortfolio(s,start,end)
    print w
    x1 = getPortfolioData(s,w,Dates()['start'],Dates()['end'])
    w = dict(zip(s,[1.0/len(s) for _ in s]))
    x2 = getPortfolioData(s,w,Dates()['start'],Dates()['end'])
    Plot.plotManyPortfolios([(x1,"optimized"),(x2,'not opt')],"PortFolio Comparison")
if __name__ == '__main__':
    main()