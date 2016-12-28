import pandas as pd
import matplotlib.pyplot as mat
import numpy as np
import mathFunc as mf
import portfolio


def preprocess(filename):
	data = pd.read_csv (filename)
	data_dropna = data.dropna()
	data_dropna.to_csv(filename[0:len(filename)-4]+"Clean.csv", sep=',', encoding='utf-8')

filename = "dataset/USDJPY5.csv"
preprocess(filename)

data  = pd.read_csv (filename[0:len(filename)-4]+"Clean.csv")
mat.plot(data['Close'])

ma50 = mf.movingAverage(50, list(data['Close']))
mat.plot(ma50)

ma100 = mf.movingAverage(200, list(data['Close']))
mat.plot(ma100)


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
limitSwitch = 0

for i in range (55, len(data)):
	if("AAPL" in pf.holdings):
		if(data['Close'][i] > pf.holdings["AAPL"][3]):
			pf.holdings["AAPL"][3] = data['Close'][i]

	if("AAPL" in pf.holdings):
		print("val: "+str((pf.holdings["AAPL"][3] - data['Close'][i])/(pf.holdings["AAPL"][3] - pf.holdings["AAPL"][2])))
		if (pf.holdings["AAPL"][3] - data['Close'][i])/(pf.holdings["AAPL"][3] - pf.holdings["AAPL"][2]) <= -0.003:
			print("Stop loss")
			pf.sell(pf.holdings["AAPL"][0], data['Close'][len(data)-1], "AAPL")


	if abs(ma50[i] - ma100[i]) <= 0.001:
		print(i)
		if i-delta >=0 and i+delta < len(ma50):
			if (ma50[i-delta]-ma50[i] > 0):
				if("AAPL" in pf.holdings):
					pf.sell(amountToBuy, data['Close'][i], "AAPL")
			else:
				if limitSwitch == 0:
					pf.buy(amountToBuy, data['Close'][i], "AAPL")
					limitSwitch = 30
	if limitSwitch > 0:
		limitSwitch-=1

if("AAPL" in pf.holdings):
	pf.sell(pf.holdings["AAPL"][0], data['Close'][len(data)-1], "AAPL")
pf.printPortfolio()
mat.show()
