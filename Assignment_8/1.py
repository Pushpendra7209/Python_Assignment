import math
def fun(n,i):
    if n<i:
        return 0;
    return float(i/math.pow(2,i))+fun(n,i+1)
print(fun(4,0))
