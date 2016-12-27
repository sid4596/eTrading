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

ma100 = mf.movingAverage(100, list(data['Close']))
mat.plot(ma100)

#mat.show()

#amount, acb, pnl
pf = portfolio.portfolio(500)
# pf.printPortfolio()

# pf.buy(10, 1, "AAPL")
# pf.printPortfolio()

# pf.buy(10, 2, "AAPL")
# pf.printPortfolio()

# pf.sell(20, 3, "AAPL")
# pf.printPortfolio()

#for i in range(100, len(data)):
	#if(ma50[i] - ma100[i] <= 0.001):
		#amountToBuy = int(pf.balance/data['Close'][i])
		#if(amountToBuy > 0):
			#pf.buy(amountToBuy, data['Close'][i], "AAPL")
	#if(ma100[i] - ma50[i] <= 0.001):
		#if("AAPL" in pf.holdings):
			#pf.sell(pf.holdings["AAPL"][0], data['Close'][i], "AAPL")
delta = 5
amountToBuy = 1
for i in range (100, len(data)):
	if abs(ma50[i] - ma100[i]) <= 0.0005:
		if (ma50[i-delta]-ma50[i+delta] > 0):
			if("AAPL" in pf.holdings):
				pf.sell(pf.holdings["AAPL"][0], data['Close'][i], "AAPL")
		else:
			pf.buy(amountToBuy, data['Close'][i], "AAPL")
			

			
pf.printPortfolio()
