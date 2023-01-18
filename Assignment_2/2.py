import random

a=random.randrange(0,1000)
print(a)
if a>99:
     x=a%10
     y=a//10
     z=y%10
     b=y//10
     print(x+z+b)

else:
    x=a//10
    y=a%10
    print(x+y)
     
