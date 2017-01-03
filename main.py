import pandas as pd
import matplotlib.pyplot as mat
import numpy as np
import mathFunc as mf
import portfolio
import momentum as mom

from os import listdir
from os.path import isfile, join


def preprocess(filename):
	print(filename)
	data = pd.read_csv ('dataset/'+filename)
	data_dropna = data.dropna()
	data_dropna.to_csv('cleanedData/'+filename[0:len(filename)-4]+"Clean.csv", sep=',', encoding='utf-8')

# datapath = "dataset/"
# files = [f for f in listdir(datapath) if isfile(join(datapath, f)) and f[len(f)-4:len(f)]=='.csv']

# list(map(preprocess, files))

datapath = "cleanedData/"
files = [f for f in listdir(datapath) if isfile(join(datapath, f)) and f[len(f)-4:len(f)]=='.csv']

# pf = portfolio.portfolio(50000)
# data = pd.read_csv("cleanedData/USDJPY5Clean.csv")
# mom.ma (50, 100, data, pf, "USDJPY5Clean.csv")
# pf.printPortfolio()
# pf.reset()

# pf = portfolio.portfolio(50000)
# data1 = pd.read_csv("cleanedData/USDJPY4Clean.csv")
# mom.ma (50, 100, data1, pf, "USDJPY4Clean.csv")
# pf.printPortfolio()
# pf.reset()

pf = portfolio.portfolio(50000)
data2 = pd.read_csv("cleanedData/USDJPY2Clean.csv")
mom.ma (50, 100, data2, pf, "USDJPY2Clean.csv")
pf.reset()

# startingBalance = 50000
# for file in files:
# 	filename = datapath+file
# 	print("="*30)
# 	print (filename)
# 	print('****Results****')
	
# 	data  = pd.read_csv (filename)
# 	pf = portfolio.portfolio(startingBalance)
# 	pf.printPortfolio()
# 	returnBalance = mom.ma(50, 100, data, pf, file[:len(file)-9])
# 	pf.printPortfolio()
# 	difference = (returnBalance - startingBalance)/ startingBalance *100 
# 	print("Start Balance:      "+str(startingBalance))
# 	print("End Balance:        "+str(returnBalance))
# 	print("Return Over Period: "+str(round(difference,2))+"%")



