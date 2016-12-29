import pandas as pd
import matplotlib.pyplot as mat
import numpy as np
import mathFunc as mf
import portfolio

from os import listdir
from os.path import isfile, join


def preprocess(filename):
	print(filename)
	data = pd.read_csv ('dataset/'+filename)
	data_dropna = data.dropna()
	data_dropna.to_csv('cleanedData/'+filename[0:len(filename)-4]+"Clean.csv", sep=',', encoding='utf-8')

# datapath = "dataset/"
# files = [f for f in listdir(datapath) if isfile(join(datapath, f)) and f[len(f)-4:len(f)]=='.csv']
# print(files)

# list(map(preprocess, files))

datapath = "cleanedData/"
files = [f for f in listdir(datapath) if isfile(join(datapath, f)) and f[len(f)-4:len(f)]=='.csv']

for file in files:
	filename = datapath+file
	print(filename)
	data  = pd.read_csv (filename)
	mat.plot(data['Close'])

	ma50 = mf.movingAverage(50, list(data['Close']))
	mat.plot(ma50)

	ma100 = mf.movingAverage(200, list(data['Close']))
	mat.plot(ma100)

	pf = portfolio.portfolio(500)

	delta = 5
	amountToBuy = 1
	limitSwitch = 0

	for i in range (55, len(data)):
		#print(i)
		#keep track of maximum
		if("AAPL" in pf.holdings):
			if(data['Close'][i] > pf.holdings["AAPL"][3]):
				pf.holdings["AAPL"][3] = data['Close'][i]

		#find stop loss
		if("AAPL" in pf.holdings):
			#print("val: "+str((pf.holdings["AAPL"][3] - data['Close'][i])/(pf.holdings["AAPL"][3] - pf.holdings["AAPL"][2])))
			if data['Close'][i] <=  pf.holdings["AAPL"][3] - 0.5:
				#print("Stop loss")
				pf.sell(pf.holdings["AAPL"][0], data['Close'][i], "AAPL")
				mat.plot(i, data['Close'][i], 'bo', ms=10, color='b')

		if abs(ma50[i] - ma100[i]) <= 0.1:
			if i-delta >=0 and i+delta < len(ma50):
				if (ma50[i]-ma50[i-delta]-(ma100[i]-ma100[i-delta]) > 0):
					if limitSwitch == 0:
						pf.buy(amountToBuy, data['Close'][i], "AAPL")
						mat.plot(i, data['Close'][i], 'bo', ms=10, color='g')
						limitSwitch = 50
				elif (ma50[i]-ma50[i-delta]-(ma100[i]-ma100[i-delta]) < 0):
					if("AAPL" in pf.holdings):
						pf.sell(amountToBuy, data['Close'][i], "AAPL")
						mat.plot(i, data['Close'][i], 'bo', ms=10, color='r')
		if limitSwitch > 0:
			limitSwitch-=1

	if("AAPL" in pf.holdings):
		pf.sell(pf.holdings["AAPL"][0], data['Close'][len(data)-1], "AAPL")
		mat.plot(len(data)-1, data['Close'][i], 'bo', ms=10, color='r')
	pf.printPortfolio()
	#mat.show()
