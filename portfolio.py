import numpy as np
import mathFunc as mf
import transaction as tr

class portfolio:
	balance = 0
	transactions = []	
	holdings = {}

	def __init__(self, balance):
		self.balance = balance

	def buy(self, quantity, rate, ticker):
		#add borrow money later
		if self.balance - quantity*rate >= 0 :
			print("Buy:  { Quantity="+str(quantity)+", Rate="+str(rate)+", Ticker="+ticker+"}");
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
				self.holdings[ticker] = [amount+quantity, (rate*quantity+ acb*amount)/(quantity+amount), pnl - quantity* rate, maxrate]

	def sell(self, quantity, rate, ticker):
		#add short selling later
		if ticker in self.holdings:
			if self.holdings[ticker][0] - quantity >= 0 :
				print("Sell: { Quantity="+str(quantity)+", Rate="+str(rate)+", Ticker="+ticker+"} Difference: "+str(rate-self.holdings[ticker][1]));

				self.balance += quantity*rate
				transaction = tr.transaction(0, quantity, rate, ticker)
				self.transactions.append(transaction)
				
				amount = self.holdings[ticker][0]
				acb = self.holdings[ticker][1]
				pnl = self.holdings[ticker][2]
				maxrate = self.holdings[ticker][3]
				self.holdings[ticker] = [amount-quantity, acb, pnl + quantity * rate, maxrate]

				if(self.holdings[ticker][0] == 0):
					del self.holdings[ticker] 
		else:
			print("Can't sell")


	def printPortfolio(self):
		print("Balance: "+str(self.balance))
		print("Holdings: "+str(self.holdings))




