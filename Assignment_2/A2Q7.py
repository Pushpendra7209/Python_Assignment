import math
def TrianleArea(a,b,c):

   s=(a+b+c)/2
   area=(s*(s-a)*(s-b)*(s-c))**0.5
   print(area)
   return area
    
def main():
    s1=int(input("enter the side of trianle"))
    s2=int(input())
    s3=int(input())
    assert(s1+s2>s3 and s2+s3> s1 and s3+s1>s2)
    TrianleArea(s1,s2,s3)
main()
