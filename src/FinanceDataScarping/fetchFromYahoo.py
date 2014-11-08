import httplib 
# Fetch data from Yahoo server and save to local file

def fetchYahoo(symbol, begYear, begMonth, begDay, endYear, endMonth, endDay,prefix=""): 
    'note: the month goes from 0 to 11!'
    uri = "/table.csv?s=" + symbol + "&d=" + str(endMonth) + "&e=" + str(endDay) + "&f=" + str(endYear) + "&g=d&a=" + str(begMonth) + "&b=" + str(begDay) + "&c=" + str(begYear) + "&ignore=.csv" 
    print "uri=" + uri 
    conn = httplib.HTTPConnection("ichart.finance.yahoo.com") 
    conn.request("GET", uri) 
    r1 = conn.getresponse() 
    data1 = r1.read() 
    fname = prefix+symbol + ".csv" 
    f = open(fname, "w") 
    f.write(data1) 
    f.close() 
    return data1


def fetchData():
    fetchYahoo("%5EVIX", 1990,00,01, 2014,11,06,"DATA\\") # the %5E is URL encoded ^ 
    fetchYahoo("SPY", 1990,00,01, 2014,11,06,"DATA\\")
    fetchYahoo("AAPL", 1990,00,01, 2014,11,06,"DATA\\")
    fetchYahoo("INTC", 1990,00,01, 2014,11,06,"DATA\\")
    fetchYahoo("WMT", 1990,00,01, 2014,11,06,"DATA\\")
    fetchYahoo("MSFT", 1990,00,01, 2014,11,06,"DATA\\")
    fetchYahoo("GOOG", 1990,00,01, 2014,11,06,"DATA\\")

def parseDataToDict(data):
    def tof(x):
        try:
            return float(x)
        except:
            return x
    'returns dict [date]=[Open,High,Low,Close,Volume,Adj Close]'
    dictData = {}
    for line in data.split('\n')[1:]:
        line = line.split(',')
        line = [tof(x) for x in line]
        line[0] = line[0].replace('-','/')
        dictData[line[0]]=line
    dictData.pop('')
    return dictData

def parseDataToList(data):
    def tof(x):
        try:
            return float(x)
        except:
            return x
    'returns dict [date]=[date,Open,High,Low,Close,Volume,Adj Close]'
    listData = []
    for line in data.split('\n')[1:]:
        line = line.split(',')
        line = [tof(x) for x in line]
        line[0] = line[0].replace('-','/')
        listData.append(line)
    listData.remove([''])
    listData.reverse()
    return listData


def ParseDate(dateStr,dateFormat='%Y/%m/%d'):
    from time import strptime
    x =  strptime(dateStr,dateFormat)
    return {"y":x.tm_year,"m":x.tm_mon,"d":x.tm_mday}

def getFromCsv(symbol,start,end):
    'note: the month goes from 0 to 11!'
    uri = "/table.csv?s=" + symbol + "&d=" + str(end['m']-1) + "&e=" + str(end['d']) + "&f=" + str(end['y']) + "&g=d&a=" + str(start['m']-1) + "&b=" + str(start['d']) + "&c=" + str(start['y']) + "&ignore=.csv" 
    print "uri=" + uri 
    conn = httplib.HTTPConnection("ichart.finance.yahoo.com") 
    conn.request("GET", uri) 
    r1 = conn.getresponse() 
    data1 = r1.read() 
    fname = symbol+".csv" 
    f = open(fname, "w") 
    f.write(data1) 
    f.close() 
    from numpy import genfromtxt
    my_data = genfromtxt(fname, delimiter=',') 
    return fname

def getSymbolDataFrame(symbol,start,end):
    x = getFromCsv(symbol,start,end)
    from pandas import DataFrame  # @UnresolvedImport
    x = DataFrame.from_csv(path=x,parse_dates=True)
    print x.columns
    x.columns=[u'Open', u'High', u'Low', u'Close', u'Volume', u'adj_close']
    x.sort_index(inplace=True)
    #x.columns = [symbol+'_'+curr for curr in x.columns]
    return x
def getDataYahoo(lstSymbols,start,end):
    #['AAPL','SPY'], start='1990/01/01', end='2013/12/01'

    data = {}
    for symbol in lstSymbols:
        data[symbol] = getSymbolDataFrame(symbol,ParseDate(start),ParseDate(end))
    return data