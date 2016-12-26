import numpy as np

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

test = []

for i in range(100):
    test.append(i)