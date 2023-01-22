x = int(input('enter first number '))
y = int(input('enter second number '))
def func( a, b):
    for i in range (2,a):
        if(a%i==0 and b%i==0):
           return False
    return True
print((func(x,y)))

print(bool(1))
