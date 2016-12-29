import mathFunc as mf
import matplotlib.pyplot as mat
import portfolio
	
def ma (short, long, data, pf):
	graph = 1
	if (graph):
		mat.plot(data['Close'])
	ma50 = mf.movingAverage(short, list(data['Close']))
	if (graph):	
		mat.plot(ma50)

	ma100 = mf.movingAverage(long, list(data['Close']))
	if (graph):
		mat.plot(ma100)

	delta = 5
	amountToBuy = 1
	limitSwitch = 0
	threshold = 5
	stopLimit = 50

	for i in range (min (short, long), len(data)):
		#print(i)
		#keep track of maximum
		if("AAPL" in pf.holdings):
			if(data['Close'][i] > pf.holdings["AAPL"][3]):
				pf.holdings["AAPL"][3] = data['Close'][i]

		#find stop loss
		if("AAPL" in pf.holdings):
			#print("val: "+str((pf.holdings["AAPL"][3] - data['Close'][i])/(pf.holdings["AAPL"][3] - pf.holdings["AAPL"][2])))
			if data['Close'][i] <=  pf.holdings["AAPL"][3] - stopLimit:
				#print("Stop loss")
				pf.sell(pf.holdings["AAPL"][0], data['Close'][i], "AAPL")
				if (graph):
					mat.plot(i, data['Close'][i], 'bo', ms=10, color='b')

		if abs(ma50[i] - ma100[i]) <= threshold:
			if i-delta >=0 and i+delta < len(ma50):
				if (ma50[i]-ma50[i-delta]-(ma100[i]-ma100[i-delta]) > 0):
					if limitSwitch == 0:
						pf.buy(amountToBuy, data['Close'][i], "AAPL")
						if (graph):
							mat.plot(i, data['Close'][i], 'bo', ms=10, color='g')
						limitSwitch = 50
				elif (ma50[i]-ma50[i-delta]-(ma100[i]-ma100[i-delta]) < 0):
					if("AAPL" in pf.holdings):
						pf.sell(amountToBuy, data['Close'][i], "AAPL")
						if (graph):
							mat.plot(i, data['Close'][i], 'bo', ms=10, color='r')
		if limitSwitch > 0:
			limitSwitch-=1

	if("AAPL" in pf.holdings):
		pf.sell(pf.holdings["AAPL"][0], data['Close'][len(data)-1], "AAPL")
		if (graph):
			mat.plot(len(data)-1, data['Close'][i], 'bo', ms=10, color='r')
	pf.printPortfolio()
	if (graph):
		mat.show()        