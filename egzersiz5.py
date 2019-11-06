
import math

def asal(x):
    if x<=1:
        return 0
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return 0
    return 1

def super_asal(x):
    if asal(x):
        if x<10:
            return 1
        else:
            return super_asal(x//10)
    else:
        return 0
    
    
for i in range(10000,100000):
    if super_asal(i):
        print(i)
