import AbstractAgent as abstract
from math import ceil,floor

class movingAvgAgent(abstract.AbstractAgent):
    '''
    args: [0]: Date(0),open(1),high(2),low(3),close(4),volume(5),adj_close(6)
          [1]: current amount of money
          [2]: current amount of stocks
    '''
    def __init__(self,name,constPercentage=0.1,window=2):
        super(movingAvgAgent,self).__init__(name)
        self.constPercentage = constPercentage
        self.window = window
        self.historicalData = []
        self.daysTraded = -1
    def moneyToStocksConverter(self,price,precentage):
        'returns the amount of stocks you want to buy'
        if precentage > 0:
            func = floor
        else:
            func = ceil
        return func(self.currentMoney*precentage/price) 
    def valueToStocksConverter(self,price,precentage):
        'returns the amount of stocks you want to buy'
        if precentage > 0:
            func = floor
        else:
            func = ceil
        return func((self.currentMoney/price+self.stocks)*precentage)    
    def calulatedMovingAvg(self):
        hist = self.historicalData
        sumPrice = 0.0
        for h in hist[-self.window-1:-1]:
            sumPrice+= h[6]
        return sumPrice/self.window
    def trade(self,args):
        super(movingAvgAgent,self).update(args)
        hist = self.historicalData        
        self.daysTraded += 1
        currIdx = self.daysTraded
        hist.append(args[0])
        if self.daysTraded<self.window:
            return 0
        avgPrice = self.calulatedMovingAvg()
        if hist[currIdx][6]>avgPrice:
            return self.valueToStocksConverter(hist[currIdx][6],self.constPercentage) 
        if hist[currIdx][6]<avgPrice:
            return -self.valueToStocksConverter(hist[currIdx][6],self.constPercentage)
        else:
            return 0.0
            
            
        