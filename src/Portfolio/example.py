"""
Illustrate the rec array utility funcitons by loading prices from a
csv file, computing the daily returns, appending the results to the
record arrays, joining on date
"""
import urllib
import numpy as np
import matplotlib.pyplot as plt  # @UnresolvedImport
import matplotlib.mlab as mlab  # @UnresolvedImport
from datetime import datetime

# grab the price data off yahoo
u1 = urllib.urlretrieve('http://ichart.finance.yahoo.com/table.csv?s=AAPL&d=11&e=6&f=2014&g=d&a=0&b=1&c=1990&ignore=.csv')
u2 = urllib.urlretrieve('http://ichart.finance.yahoo.com/table.csv?s=MSFT&d=11&e=6&f=2014&g=d&a=0&b=1&c=1990&ignore=.csv')

# load the CSV files into record arrays
r1 = mlab.csv2rec(file(u1[0]))
r2 = mlab.csv2rec(file(u2[0]))

# compute the daily returns and add these columns to the arrays
gains1 = np.zeros_like(r1.adj_close)
gains2 = np.zeros_like(r2.adj_close)
gains1[1:] = np.diff(r1.adj_close)/r1.adj_close[:-1]
gains2[1:] = np.diff(r2.adj_close)/r2.adj_close[:-1]
r1 = mlab.rec_append_fields(r1, 'gains', gains1)
r2 = mlab.rec_append_fields(r2, 'gains', gains2)

# now join them by date; the default postfixes are 1 and 2.  The
# default jointype is inner so it will do an intersection of dates and
# drop the dates in AAPL which occurred before GOOG started trading in
# 2004.  r1 and r2 are reverse ordered by date since Yahoo returns
# most recent first in the CSV files, but rec_join will sort by key so
# r below will be properly sorted
r = mlab.rec_join('date', r1, r2)
#r = r.astype([('date', 'S10'), ('open1', '<f8'), ('high1', '<f8'), ('low1', '<f8'), ('close1', '<f8'), ('volume1', '<i4'), ('adj_close1', '<f8'), ('gains1', '<f8'), ('open2', '<f8'), ('high2', '<f8'), ('low2', '<f8'), ('close2', '<f8'), ('volume2', '<i4'), ('adj_close2', '<f8'), ('gains2', '<f8')])

#head = ",".join([x[0] for x in r.dtype.descr])


y = [(r.date[i],r1.adj_close[i],gains1[i],r2.adj_close[i],gains2[i]) for i in xrange(len(r.date))]
z = np.rec.array(y,dtype=[('date',datetime),('AAPL_adj_close', '<f8'),('AAPL_gains','<f8'),('SPY_adj_close2', '<f8'),('SPY_gains','<f8')])

# y = [(r.date[i],gains1[i],gains2[i]) for i in xrange(len(r.date))]
# z = np.rec.array(y,dtype=[('date',datetime),('AAPL_gains','<f8'),('SPY_gains','<f8')])
head = ",".join([x[0] for x in z.dtype.descr])
np.savetxt('test.csv', z, delimiter=',',fmt=["%s"]+["%.3f",]*4,header=head)
#np.savetxt('test.csv', r, delimiter=',',fmt=["%s"]+["%.3f",]*14,header=head)

# long appl, short goog
g = r.gains1-r.gains2
tr = (1+g).cumprod()  # the total return

# plot the return
fig, ax = plt.subplots()
ax.plot(r.date, tr)
ax.set_title('total return: long APPL, short s&p500')
ax.grid()
fig.autofmt_xdate()
plt.show()