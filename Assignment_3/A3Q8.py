def fun(n):
    rev=0
    a=n
    while a>0:
        b=a%10
        rev=rev*10+b
        a//=10

    if(n==rev):
        print("true")
    else:
        print("false")
num=123
fun(num)
