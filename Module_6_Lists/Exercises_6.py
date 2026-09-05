#1
import random

rolls = int(input("How many dice to roll?"))
total = 0

for amount in range(rolls):
    dice = random.randint(1,6)
    total = total + dice

print( total)

#2
numbers = []
number = input("Enter a number, to stop press enter ")
while number !="":
    number= int(number)
    numbers.append(number)
    number = input("Enter a number, to stop press enter ")
numbers.sort(reverse=True)
print(numbers[:5])

#3

number = int(input("Enter an integer: "))
prime = True
for numbers in range(2,number):
    if number % numbers == 0:
        prime =False
if prime:
    print(f"{number} is a prime number")
else:
    print (f"{number} is not a prime number")

#4

cities = []

city = input("Enter the first city: ")
for  n in range(5):
    cities.append(city)
    city = input("Enter the next city: ")
for city in cities:
    print(city)