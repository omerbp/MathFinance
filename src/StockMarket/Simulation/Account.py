import config
class Account(object):
    def __init__(self,params):
        self.cash = params[0]
        self.possibleCashDebt = params[1]
        self.inactive = False
        self.stocks = 0
        self.records = [] #cash,stocks,portfolioValue,buying quantity
    def record(self,price,buyingQuantity):
        self.records.append((self.cash,self.stocks,self.cash+self.stocks*price,buyingQuantity))
    def recordBankrupt(self):
        self.records.append((0,0,-10000,0))
    def portfolioValue(self,price):
        return self.cash+self.stocks*price
    def tradeStocks(self,quantity,price):
        if self.portfolioValue(price)<0:
            self.inactive = True
        if self.inactive == True:
            self.recordBankrupt()
            return
        elif self.cash - quantity*price > self.possibleCashDebt:# and -self.stocks*price < self.portfolioValue(price)*config.maxShortPercentageOfPortfolioValue :
            self.cash -= quantity*price
            self.stocks += quantity    
        self.record(price,quantity)
        return self.stocks,self.cash            
    def finalize(self,price):
        self.cash += self.stocks*price
        self.stocks = 0
        self.record(price,"end of trading")
        return self.cash
    
        