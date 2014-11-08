
class AbstractAgent(object):

    def __init__(self,name):
        self.name = name
    def update(self,args):
        self.currentMoney = args[1]
        self.stocks = args[2]  

    
        