x = int(input("enter a number "))
count=0
sum=0
for i in range(1,x+1,2):
    count=count+1
    if(count%2==0):
        sum=sum-i
    else:
        sum=sum+1

print(sum)
