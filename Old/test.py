import pandas as pd
import matplotlib.pyplot as mat
import numpy as np
import framework as fm

test  = pd.read_csv ('GBPUSD2.csv')
test_close = [i for i in test['Close'] if (~np.isnan(i))]
test_close = pd.DataFrame({'Close':test_close})

def max_profit (a):
    current_max = a[len(a)-1]
    
    profit = 0
    
    for j in range (len(a)-2, -1, -1):
        if ~np.isnan(a[j]):
            if current_max < a[j]:
                current_max = a[j]
            else:
                profit += (current_max - a[j])
            
    print (profit)

def movingAverage(n, a):
    #This moving average function requires list a and int n
    #If n is for example 3, proc[i] is the average over a[i - 1], a[i], a[i + 1]
    #At the end points, if a[i -1] does not exist for example, the value is not considered
    if n > len(a):
        
        return None
    
    n = int(n/2)
    
    proc = []
    a = [i for i in a if (~np.isnan(i))]
    for i in range(0, n):   
        proc.append(np.mean(a[0: n + i + 1]))
            
    for i in range(n, len(a) - n):
        proc.append(np.mean(a[i - n: i + n + 1]))
        
    for i in range(len(a) - n, len(a)):
        proc.append(np.mean(a[i - n + 1: len(a)]))
        
    return proc 

def avg (a):
    result = 0
    count = 0
    for i in a:
        if ~np.isnan(i):
            result += i
            count += 1
    return result/count

def movingAvg (n, data):
    if len(data) < n:
        return None
    else:
        result = []
        for i in range (0,len(data)-n):
            result.append(avg(data[i:i+n]))
    return result
        
haha1 = movingAverage (50, test_close['Close'])
haha2 = movingAverage (200, test_close['Close'])
haha = pd.DataFrame({'Test1': haha1, 'Test2': haha2})

mat.plot(haha['Test1'])
mat.plot(haha['Test2'])
mat.plot(test_close)

#lol.plot()
#test_close.plot()
mat.show()

p1 = fm.portfolio (5) 
p1.buy(1,1)