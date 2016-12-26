import math
import numpy as np

def movingAverage(n, a):
    #This moving average function requires list a and int n
    if n > len(a):
        return None
    
    result = [a[0]]
    
    for i in range (1,n):
        result = result + [np.mean(a[0:i+1])]
        
    for i in range (n,len(a)):
        result = result + [np.mean(a[i-n+1:i+1])]    
        
    return result
