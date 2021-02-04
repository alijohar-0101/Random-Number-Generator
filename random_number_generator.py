import random
from random import randrange

print("Give me two numbers, a minimum and a maximum")
a = int(input("Select minimum. "))
b = int(input("Select maximum. "))
c = 0
while c < 10:
    print(randrange(a, b))
    c += 1