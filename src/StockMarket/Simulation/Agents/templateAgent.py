
class templateAgent():
    '''
    args: [0]: Date(0),open(1),high(2),low(3),close(4),volume(5),adj_close(6)
          [1]: current amount of money
          [2]: current amount of stocks
    '''
    def __init__(self,constArgs,tradeFunction,name):
        self.AgentArgs = constArgs
        self.historicalData = []
        self.pastAccountValues = []
        self.name = name
        self.daysTraded = -1   
        self.tradeFunction = tradeFunction
    def trade(self,args):
        self.pastAccountValues.append([args[1],args[2],args[1]+args[2]*args[0][6]])
        hist = self.historicalData        
        self.daysTraded += 1
        hist.append(args[0])
        self.pastAccountValues[-1].append(self.tradeFunction(self.AgentArgs,self.historicalData,self.pastAccountValues))
        return self.pastAccountValues[-1][3]
        
        