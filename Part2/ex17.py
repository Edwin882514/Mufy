
name= input("What is your name?")

import random
adjective=["Chill","Strong","Hungry","Lucky","Nasty","Big"]
animal=["Lion","Chicken","Monkey","Tiger","Sealion","Bear"]


print(f"{name},your codename is:", random.choice(adjective)+" "+random.choice(animal))
print("Your lucky number is:", random.randint(1,99))
