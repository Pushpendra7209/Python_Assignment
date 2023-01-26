def fun(n,i):
    if i>n:
        return 0
    return 1/i + fun(n,i+1)
print(fun(4.0,1))
