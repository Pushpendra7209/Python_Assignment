import random
x=random.random()+5
print(x)

print(random.random())

print(random.randrange(3, 9))
print(random.randint(3, 9))

mylist = ["apple", "banana", "cherry"]

print(random.choice(mylist))


mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)

print(mylist)

mylist = ["apple", "banana", "cherry"]

print(random.choices(mylist, weights = [10, 1, 1], k = 14))


mylist = ["apple", "banana", "cherry"]

print(random.sample(mylist, k=2))
