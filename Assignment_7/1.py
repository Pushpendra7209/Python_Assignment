def summation(n):
     total=0
     for count in range(1,n+1):
          total+=count
     return total

def main():
     n=int(input("Enter number of terms\n"))
     total = summation(n)
     print("The sum of first ",n," positive integers: \n",total)

if(__name__=="__main__"):
     main()
     
