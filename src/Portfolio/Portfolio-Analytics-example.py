# Download some historical data
from pandas.io.data import get_data_yahoo
from portfolio.optimizations.solvers import SolverPortfolio
import portfolio.objectives as objective
import portfolio.constraints as constraint


#"start":'1995/01/10',"end":'2014/11/10'
ohlc_data = get_data_yahoo(["AAPL","SPY",'INTC','MSFT',"WMT"], start='1995/01/10', end='2014/11/10')
data = ohlc_data['Close']

# Now let's optimize our portfolio weights


portfolio = SolverPortfolio(objective.expected_return) # or risk
# Forbid short positions
#portfolio.add_constraint(constraint.long_only())
# Invest every cent of our cash
portfolio.add_constraint(constraint.full_investment())

# Get optimal weights in %
print portfolio.optimize(["AAPL","SPY",'INTC','MSFT',"WMT"], data)