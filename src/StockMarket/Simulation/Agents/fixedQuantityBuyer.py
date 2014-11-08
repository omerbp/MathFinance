from Agents.AbstractAgent import AbstractAgent

class fixedQuantityBuyer(AbstractAgent):
    '''
    args: [0]: Date(0),open(1),high(2),low(3),close(4),volume(5),adj_close(6)
          [1]: current amount of money
          [2]: current amount of stocks
    '''
    def __init__(self,name,fixedQuantity=1):
        super(fixedQuantityBuyer,self).__init__(name)
        self.fixedQuantity = fixedQuantity
        self.historicalData = []
        self.daysTraded = -1
 
    def trade(self,args):
        super(fixedQuantityBuyer,self).update(args)
        hist = self.historicalData        
        self.daysTraded += 1
        currIdx = self.daysTraded
        hist.append(args[0])
        if self.daysTraded==0:
            return 2
        if hist[currIdx][6]>hist[currIdx-1][6]:
            return self.fixedQuantity
        if hist[currIdx][6]<hist[currIdx-1][6]:
            return -self.fixedQuantity
        else:
            return 0.0