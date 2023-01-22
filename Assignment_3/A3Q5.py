a= int(input("enter first number : "))
b= int(input("enter second number: "))

def compute_gcd(a,b):
    if(a>b):
        smaller=b
    else:
        smaller=a

    while smaller >0 :
        if(a%smaller==0 and b%smaller==0):
           gcd=smaller
           break
        smaller-=1

    return gcd
print(compute_gcd(a,b))

    
