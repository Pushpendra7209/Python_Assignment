def num(n):
    if n==0:
        return 0;
    return n%10+num(n//10)
print(num(12345))
