import pdb
#pdb.set_trace()

def max3(n1,n2,n3):
    maxx=0
    if n1>n2:
        if n1>n3:
            maxx=n1
        else:
            maxx=n3

    elif n2>n3:
     maxx=n2

    else:
     maxx=n3

    return maxx

def main():
    n1=int(input("Enter n1:"))
    n2=int(input("Enter n2:"))
    n3=int(input("Enter n3:"))
    maximum=max3(n1,n2,n3)
    print("The maximum of the number is",maximum)

if __name__=="__main__":
    main()
0
