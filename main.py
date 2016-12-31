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

datapath = "dataset/"
files = [f for f in listdir(datapath) if isfile(join(datapath, f)) and f[len(f)-4:len(f)]=='.csv']

list(map(preprocess, files))

datapath = "cleanedData/"
files = [f for f in listdir(datapath) if isfile(join(datapath, f)) and f[len(f)-4:len(f)]=='.csv']

# pf = portfolio.portfolio(50000)
# data = pd.read_csv("cleanedData/S&P1Clean.csv")
# mom.ma (50, 100, data, pf, "AAPL")

startingBalance = 50000

for file in files:
	filename = datapath+file
	print("="*30)
	print (filename)
	print('****Results****')
	
	data  = pd.read_csv (filename)
	pf = portfolio.portfolio(startingBalance)

	returnBalance = mom.ma(50, 100, data, pf, "AAPL")
	difference = returnBalance/startingBalance *100
	print("Start Balance: "+str(startingBalance))
	print("End Balance:   "+str(returnBalance))
	print("Difference:    "+str(difference)+"%")

	
