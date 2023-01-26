import math
def fun(str, i):
    if i==len(str):
        return
    return math.pow(10,i)*float(str[0]) + fun(str[1:],i+1)
print(fun("1234",0))
