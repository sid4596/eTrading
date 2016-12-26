import pandas as pd
import matplotlib.pyplot as mat
import numpy as np
import mathFunc as mf
import portfolio


def preprocess(filename):
	data = pd.read_csv (filename)
	data_dropna = data.dropna()
	data_dropna.to_csv(filename[0:len(filename)-4]+"Clean.csv", sep=',', encoding='utf-8')

filename = "GBPUSD.csv"
preprocess(filename)

data  = pd.read_csv (filename[0:len(filename)-4]+"Clean.csv")
mat.plot(data['Close'])

ma50 = mf.movingAverage(50, list(data['Close']))
mat.plot(ma50)
print(str(ma50[0]))

ma100 = mf.movingAverage(100, list(data['Close']))
mat.plot(ma100)

mat.show()

#amount, acb, pnl
# pf = portfolio.portfolio(500)
# pf.printPortfolio()

# pf.buy(10, 1, "AAPL")
# pf.printPortfolio()

# pf.buy(10, 2, "AAPL")
# pf.printPortfolio()

# pf.sell(20, 3, "AAPL")
# pf.printPortfolio()

