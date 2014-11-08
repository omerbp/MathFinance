import AbstractAgent as abstract
from math import ceil,floor

class staticInvestor(abstract.AbstractAgent):
    '''
    args: [0]: Date(0),open(1),high(2),low(3),close(4),volume(5),adj_close(6)
          [1]: current amount of money
          [2]: current amount of stocks
    '''
    def __init__(self,name):
        super(staticInvestor,self).__init__(name)
        self.daysTraded = -1
    def moneyToStocksConverter(self,price,precentage):
        'returns the amount of stocks you want to buy'
        if precentage > 0:
            func = floor
        else:
            func = ceil
        return func(self.currentMoney*precentage/price) 
    def trade(self,args):
        super(staticInvestor,self).update(args)  
        self.daysTraded += 1
        return self.moneyToStocksConverter(args[0][6], 1.0)

            
        