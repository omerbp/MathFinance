

def ParseDate(dateStr,dateFormat='%d/%m/%Y'):
    'input looks like 06/11/2014 '
    from time import strptime
    x =  strptime(dateStr,dateFormat)
    return {"y":x.tm_year,"m":x.tm_mon,"d":x.tm_mday}
def ParseToDatetime(dateStr,dateFormat):
    import datetime
    x = ParseDate(dateStr,dateFormat)
    return datetime.datetime(x["y"],x["m"],x["d"])
def dictPrint(dic,view=True):
    if view==False:
        return
    for k in sorted(dic.keys()):
        print k,dic[k]
def listPrint(lst,view=True):
    if view==False:
        return
    for k in xrange(len(lst)):
        print k,lst[k]
                                                               
                                                               
    