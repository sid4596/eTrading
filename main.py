import pandas as pd
import matplotlib.pyplot as mat
import numpy as np
import mathFunc as mf

test  = pd.read_csv ('GBPUSD.csv')
print(len(test['Close']))
test2 = test.dropna()
print(len(test2['Close']))
mat.plot(test2['Close'].)
test2['Close'].plot()
temp = mf.movingAverage(50, list(test2['Close']))
print (len(temp))
mat.plot(temp)
mat.show()