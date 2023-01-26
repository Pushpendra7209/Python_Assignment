def fun(a,b):
    if b==1:
        return a
    return a*fun(a,b-1)
print(fun(2,3))
