from FinanceDataScarping.fetchFromYahoo import fetchYahoo,parseDataToDict,parseDataToList,fetchData
from Agents.constPercentageAgent import constPercentageAgent
from Agents.fixedQuantityBuyer import fixedQuantityBuyer
from Agents.movingAvgAgent import movingAvgAgent
from Agents.staticInvestor import staticInvestor
from Agents.templateAgent import templateAgent
from Account import Account
from Utilities import ParseDate,listPrint
from Plotter.PlotAgentStockGraphs import PlotComparedAgentsStockGraphs
from Agents import TradingFunctions


def Agents():
#     return [constPercentageAgent("constPercentageAgent 0.3",0.3),
#             staticInvestor("Stock Real Value"),
# #             fixedQuantityBuyer("fixed Quantity Buyer",2),
# #             constPercentageAgent("constPercentageAgent 0.5 ",0.5),
#             movingAvgAgent("movingAvgAgent",0.1,1)
#             ]
    return [staticInvestor("Stock Real Value"),
            templateAgent({"windowSize":1,"fixedPercentage":0.1},TradingFunctions.trade_fPerc_Cash_MovAvg,name="trade_fPerc_Cash_MovAvg(1,0.1)"),
            templateAgent({"windowSize":3,"fixedPercentage":0.3},TradingFunctions.trade_fPerc_Val_MovAvg,name="trade_fPerc_Cash_MovAvg(3,0.3)"),
            templateAgent({"windowSize":1,"fixedPayment":500.0},TradingFunctions.trade_famount_Val_MovAvg,name="trade_famount_Val_MovAvg(1,500.0)")
            ]

def Dates():
    #24/09/2008
    return {"start":'1/9/1990',"end":'08/10/2014'}
def Stocks():
    return ["AAPL"]
def InitMoney():
    return 10000,-1000
def Printer(x,view = True):
    if view==False:
        return
    print x

    
    

def StockMarketSimulation(view = True):
    agents = Agents()
    accounts = []
    for _ in xrange(len(agents)):
        accounts.append(Account(InitMoney()))
    startDate = ParseDate(Dates()["start"])
    endDate = ParseDate(Dates()["end"])
    stocks = Stocks()
    data = {}
    for s in stocks:
        data[s] = parseDataToList(fetchYahoo(s,startDate['y'],startDate['m']-1,startDate['d'],endDate['y'],endDate['m']-1,endDate['d'],"DATA\\TODELETE123"))
    print 'dayNum,agentNum,cash,stocks,portfolioValue,buying quantity'
    for dayNum in xrange(len(data[stocks[0]])-1): #the final day is only used to finalize;
        for s in stocks:
            stockDayData = data[s][dayNum]
            for agentNum in xrange(len(agents)):
                if accounts[agentNum].inactive == False: #if the player has bankrupted - skip
                    quantity = agents[agentNum].trade([stockDayData,accounts[agentNum].cash,accounts[agentNum].stocks])
#                     if dayNum>0:
#                         print dayNum,agentNum,quantity
                    accounts[agentNum].tradeStocks(quantity,stockDayData[6])
                else:
                    accounts[agentNum].recordBankrupt()
        
    for agentNum in xrange(len(agents)):
        accounts[agentNum].finalize(data[s][dayNum][6])
    PlotComparedAgentsStockGraphs(data[stocks[0]],[accounts[i].records for i in xrange(len(agents))],[agents[i].name for i in xrange(len(agents))])
     

def main():
    #fetchData()
    StockMarketSimulation()
    
if __name__ == '__main__':
    main()