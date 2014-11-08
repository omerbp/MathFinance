import AbstractAgent as abstract
from math import ceil,floor

class constPercentageAgent(abstract.AbstractAgent):
    '''
    args: [0]: Date(0),open(1),high(2),low(3),close(4),volume(5),adj_close(6)
          [1]: current amount of money
          [2]: current amount of stocks
    '''
    def __init__(self,name,constPercentage=0.1):
        super(constPercentageAgent,self).__init__(name)
        self.constPercentage = constPercentage
        self.historicalData = []
        self.daysTraded = -1
    def moneyToStocksConverter(self,price,precentage):
        'returns the amount of stocks you want to buy'
        if precentage > 0:
            func = floor
        else:
            func = ceil
        return func(self.currentMoney*precentage/price)   
    def trade(self,args):
        super(constPercentageAgent,self).update(args)
        hist = self.historicalData        
        self.daysTraded += 1
        currIdx = self.daysTraded
        hist.append(args[0])
        if self.daysTraded==0:
            return 2
        if hist[currIdx][6]>hist[currIdx-1][6]:
            return self.moneyToStocksConverter(hist[currIdx][6],self.constPercentage) 
        if hist[currIdx][6]<hist[currIdx-1][6]:
            return -self.moneyToStocksConverter(hist[currIdx][6],self.constPercentage)
        else:
            return 0.0
            
            
        