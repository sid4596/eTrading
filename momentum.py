import mathFunc as mf
import matplotlib.pyplot as mat
import portfolio
	
def ma (short, long, data, pf, ticker):
	graph = 0
	debug = 0

	if (graph):
		mat.plot(data['Close'])
	
	maShort = mf.movingAverage(short, list(data['Close']))
	if (graph):	
		mat.plot(maShort)

	maLong = mf.movingAverage(long, list(data['Close']))
	if (graph):
		mat.plot(maLong)


	delta = 5
	amountToBuy = 1
	buyLimitTimer = 0
	buyLimitMax = 50
	threshold = 5
	stopLimit = 50

	for i in range (min (short, long), len(data)):
		if(debug):
			print("Day: "+ str(i))
		
		#keep track of maximum
		if(ticker in pf.holdings):
			if(data['Close'][i] > pf.holdings[ticker][3]):
				pf.holdings[ticker][3] = data['Close'][i]
			if(debug):
				print("New Maximum of {"+ticker+": "+str(pf.holdings[ticker][3])+"}")

		#check stop loss
		if(ticker in pf.holdings):
			if data['Close'][i] <=  pf.holdings[ticker][3] - stopLimit:
				pf.sell(pf.holdings[ticker][0], data['Close'][i], ticker)
				if(debug):
					print("Stop loss reached")
				if (graph):
					mat.plot(i, data['Close'][i], 'bo', ms=10, color='b')
		
		#check if moving average short crosses moving average long
		if abs(maShort[i] - maLong[i]) <= threshold:
			if(debug):
				print("MA crossing")
			if i-delta >=0 and i+delta < len(maShort):
				if (maShort[i]-maShort[i-delta]-(maLong[i]-maLong[i-delta]) > 0):
					if buyLimitTimer == 0:
						pf.buy(amountToBuy, data['Close'][i], ticker)
						if (graph):
							mat.plot(i, data['Close'][i], 'bo', ms=10, color='g')
						buyLimitTimer = buyLimitMax
				elif (maShort[i]-maShort[i-delta]-(maLong[i]-maLong[i-delta]) < 0):
					if(ticker in pf.holdings):
						pf.sell(amountToBuy, data['Close'][i], ticker)
						if (graph):
							mat.plot(i, data['Close'][i], 'bo', ms=10, color='r')

		#stopper for consecutive purchases
		if buyLimitTimer > 0:
			buyLimitTimer-=1
	
	#sell all remaining items in portfolio
	if(ticker in pf.holdings):
		pf.sell(pf.holdings[ticker][0], data['Close'][len(data)-1], ticker)
		
		if (graph):
			mat.plot(len(data)-1, data['Close'][i], 'bo', ms=10, color='r')
	
	if (graph):
		mat.grid(True)
		mat.show()   
		mat.close()    

	returnbalance = pf.balance
	return returnbalance
	