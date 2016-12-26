import pandas as pd

class portfolio:
    balance = 0
    holdings = pd.DataFrame (columns=('Rate', 'Quantity'))
    
    def __init__ (self, num):
        self.balance = num
        
    def buy (self, rate, quantity):
        if self.balance - rate*quantity >=0:
            print ('Buying')
            self.balance -= rate*quantity
            temp = pd.DataFrame ({'Rate':rate, 'Quantity':quantity})
            self.holdings.append(temp, ignore_index=True)
            self.holdings[0][0] = 5
        