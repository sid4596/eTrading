import numpy as np
import mathFunc as mf

class transaction:
	action = -1
	quantity = 0
	rate = 0
	ticker = ""
	def __init__(self, action, quantity, rate, ticker):
		#buy == 1, sell == 0
		self.action = action
		self.quantity = quantity
		self.rate = rate
		self.ticker = ticker

