from math import ceil,floor
from StockMarket.Simulation import config
'''
every Trading function gets: (AgentArgs,historicalData,pastAccountValues)
AgentArgs - {windowSize,fixedQuantity,fixedPercentage}
historicalData
pastAccountValues - (cash,stocks,portfolioValue,buying quantity)
'''
def buyStocks(money,price,percentage):
    '''returns the amount of stocks you want to buy. 
    there is not limit on the amount of stocks in case of selling '''
    return floor(money*1.0*percentage/(price*1.0))
def sell(money,price,percentage,ownedStocks):
    toSell = ceil(money*1.0*percentage/(price*1.0))
    if toSell < ownedStocks:
        return toSell
    else:
        return min(toSell,ownedStocks+money*config.maxShortPercentageOfPortfolioValue/(price*1.0))
def MovingAvg(lst,windowSize):
    if len(lst)<windowSize:
        return None
    return sum(lst[-windowSize:]) / (windowSize*1.0)

def trade_fPerc_Cash_MovAvg(AgentArgs,historicalData,pastAccountValues):
    price = historicalData[-1][6] 
    cash = pastAccountValues[-1][0]
    portfolioValue = pastAccountValues[-1][2]
    ownedStocks = pastAccountValues[-1][1]
    percentage = AgentArgs["fixedPercentage"]
    avgPrice = MovingAvg([h[6] for h in historicalData[-AgentArgs["windowSize"]-1:-1]],AgentArgs["windowSize"])
    if historicalData[-1][6]>avgPrice:
        return buyStocks(cash,price,percentage)
    if historicalData[-1][6]<avgPrice:
        return -sell(portfolioValue,price,percentage,ownedStocks)
    else:
        return 0.0
def trade_fPerc_Val_MovAvg(AgentArgs,historicalData,pastAccountValues):
    price = historicalData[-1][6] 
    portfolioValue = pastAccountValues[-1][2]
    ownedStocks = pastAccountValues[-1][1]
    percentage = AgentArgs["fixedPercentage"]
    avgPrice = MovingAvg([h[6] for h in historicalData[-AgentArgs["windowSize"]-1:-1]],AgentArgs["windowSize"])
    if avgPrice==None:
        return 0.0
    if historicalData[-1][6]>avgPrice:
        buyStocks(portfolioValue,price,percentage)
    if historicalData[-1][6]<avgPrice:
        return -sell(portfolioValue,price,percentage,ownedStocks)
    else:
        return 0.0
def trade_famount_Val_MovAvg(AgentArgs,historicalData,pastAccountValues):
    price = historicalData[-1][6] 
    ownedStocks = pastAccountValues[-1][1]
    payment = AgentArgs["fixedPayment"]
    avgPrice = MovingAvg([h[6] for h in historicalData[-AgentArgs["windowSize"]-1:-1]],AgentArgs["windowSize"])
    if avgPrice==None:
        return 0.0
    if historicalData[-1][6]>avgPrice:
        buyStocks(payment,price,1.0)
    if historicalData[-1][6]<avgPrice:
        return -sell(payment,price,1.0,ownedStocks)
    else:
        return 0.0