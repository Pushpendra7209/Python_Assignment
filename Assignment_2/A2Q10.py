def digitseperate(num):
    n4=int(num%10)
    num/=10
    n3=int(num%10)
    num/=10
    n2=int(num%10)
    num/=10
    n1=int(num%10)
    sum = int(n1*int(1-n1%2)+ n2*int(1-n2%2)+n3*int(1-n3%2)+ n4*int(1-n4%2))
    print("Sum of even digit in a digit no. is ",sum)


    
num=int(input("enter a 4 digit number : "))
digitseperate(num)
    
