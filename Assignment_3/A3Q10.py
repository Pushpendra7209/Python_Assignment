import math
armstrong=0
def func(a):
    
    p=a
    while (a>0):
        b=a%10
        armstrong = armstrong + pow(b,3)
        a=a//10
    if(p==armstrong):
       print(p)

for i in range(1,1001):
    func(i)
