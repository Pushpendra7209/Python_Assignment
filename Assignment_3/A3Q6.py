N=int(input("enter a number  : "))
def fun(n):
 for i in range(1,N+1):
    for j in range(1,i+1):
        print(j,end=" ")

    print()
fun(N)


#c
N=int(input("enter a number  : "))
def fun(n):
 for i in range(1,n+1):
    while n>0:
        print(n,end=" ")

    print()
fun(N)
