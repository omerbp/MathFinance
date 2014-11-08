import matplotlib.pyplot as plt # @UnresolvedImport
from Utilities import ParseToDatetime
def plot(data,title):
    '''
    data[0] - x axis
    data[1] - y axis
    '''
    # plot the return
    fig, ax = plt.subplots()
    ax.plot(data[0],data[1])
    ax.set_title(title)
    ax.grid()
    fig.autofmt_xdate()
    plt.show()
def PlotAgentStockGraphs(stockData,records,title): #records - cash,stocks,portfolioValue,buying quantity
    dateList = []
    for dayNum in xrange(len(stockData)):
        #print ParseDate(data[stocks[0]][dayNum][0],'%Y/%m/%d')
        dateList.append(ParseToDatetime(stockData[dayNum][0],'%Y/%m/%d'))
    plot([dateList,[x[0] for x in records]],title+' Cash chart') #cash    
    plot([dateList,[x[1] for x in records]],title+' Stocks chart') #stocks
    plot([dateList,[x[2] for x in records]],title+' Portfolio Value chart') #portfolio value 
def plotDataFrame(data,names,title):
    '''
    data[0] - x axis
    data[1] - y axis
 
    '''
    numOfAgents =  len(data[1])
    fig, ax = plt.subplots()
    lines = [i for i in xrange(0,numOfAgents)]
    for agentNum in xrange(0,numOfAgents):
        lines[agentNum], = ax.plot(data[0],data[1][agentNum],label=names[agentNum])
        lines[agentNum].set_linewidth(3)
 
    ax.set_title(title)
    ax.grid()
    #plt.legend(lines)
    #plt.legend(bbox_to_anchor=(1.00, 1), loc=2, borderaxespad=0.)
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.10),fancybox=True, shadow=True, ncol=5,fontsize="x-large",numpoints=1)
    fig.autofmt_xdate()
    plt.show()
 
def PlotComparedAgentsStockGraphs(stockData,records,names,title =""): #records - cash,stocks,portfolioValue,buying quantity
    dateList = []
    for dayNum in xrange(len(stockData)):
        #print ParseDate(data[stocks[0]][dayNum][0],'%Y/%m/%d')
        dateList.append(ParseToDatetime(stockData[dayNum][0],'%Y/%m/%d'))
#     plotDataFrame([dateList,[[x[0] for x in records[i]] for i in xrange(len(records))]],names,title+' Cash chart') #cash    
#     plotDataFrame([dateList,[[x[1] for x in records[i]] for i in xrange(len(records))]],names,title+' Stocks chart') #stocks
    plotDataFrame([dateList,[[x[2] for x in records[i]] for i in xrange(len(records))]],names,title+' Portfolio Value chart') #portfolio value 