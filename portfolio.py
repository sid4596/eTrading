import numpy as np
import mathFunc as mf
import transaction as tr


class portfolio:
	balance = 0
	transactions = []	
	holdings = {}


	def __init__(self, balance):
		self.balance = balance
		self.holdings = {}
		self.transactions = []

	def buy(self, quantity, rate, ticker):
		#add borrow money later
		if self.balance - quantity*rate >= 0 :
			#print("Buy:  { Quantity="+str(quantity)+", Rate="+str(rate)+", Ticker="+ticker+"}");
			self.balance -= quantity*rate
			transaction = tr.transaction(1, quantity, rate, ticker)
			self.transactions.append(transaction)
			if ticker not in self.holdings:
				self.holdings[ticker] = [quantity, rate, -1*quantity* rate, rate]
			else:
				amount = self.holdings[ticker][0]
				#adjusted cost base
				acb = self.holdings[ticker][1]
				pnl = self.holdings[ticker][2]
				maxrate = self.holdings[ticker][3]
				newacb = 0
				if(quantity + amount != 0):
					newacb = (rate*quantity+ acb*amount)/(quantity+amount)

				self.holdings[ticker] = [amount+quantity, newacb, pnl - quantity* rate, maxrate]
		
			return transaction

		

	def sell(self, quantity, rate, ticker):
		#print("Sell: { Quantity="+str(quantity)+", Rate="+str(rate)+", Ticker="+ticker+"} Difference: "+str(rate-self.holdings[ticker][1]));
		if(ticker not in self.holdings):
			self.holdings[ticker] = [0, 0, 0, 0]

		# if(quantity > self.holdings[ticker][0]):
		# 	print("Shorting")

		self.balance += quantity*rate
		transaction = tr.transaction(0, quantity, rate, ticker)
		self.transactions.append(transaction)
		
		amount = self.holdings[ticker][0]
		acb = self.holdings[ticker][1]
		pnl = self.holdings[ticker][2]
		maxrate = self.holdings[ticker][3]
		self.holdings[ticker] = [amount-quantity, acb, pnl + quantity * rate, maxrate]

	
	def liquidateAll(self, endingPrices):
		for ticker in self.holdings:
			if(self.holdings[ticker][0] > 0):
				self.sell(self.holdings[ticker][0], endingPrices[ticker], ticker)
			elif(self.holdings[ticker][0] < 0):
				self.buy(self.holdings[ticker][0]*-1, endingPrices[ticker], ticker)
		self.refreshHoldings()

	def refreshHoldings(self):
		refreshed = {}
		for ticker in self.holdings:
			if(self.holdings[ticker][0] != 0):
				refreshed[ticker] = self.holdings[ticker]

		self.holdings = refreshed


	def printPortfolio(self):
		print("Balance: "+str(self.balance))
		print("Holdings: "+str(self.holdings))

	def reset(self):
		self.balance = 0
		self.transactions = []	
		self.holdings = {}


