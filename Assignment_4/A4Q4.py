n = int(input("enter a number "))
def func(n):
    i=1
    fact=1
    while(i<n+1):
        fact=fact*i
        i=i+1
    return fact
print("factorial of " ,n ," = ",func(n))
