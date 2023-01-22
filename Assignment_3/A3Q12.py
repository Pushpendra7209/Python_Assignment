x = int(input("enter first number "))
y= int(input("enter second number :"))

def fun(x,y):
    i=0
    sum=0
    while(i<y):
        sum=sum+x
        i=i+1
    return sum
print(fun(x,y))
