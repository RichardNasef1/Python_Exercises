""" #1 

n = 1
while n <= 1000:
    if n%3 == 0: 
        print(n)
    n = n + 1

#2

prompt = "How many inches? "
inches = float(input(prompt))
while inches >= 0:
    print(f"In centimeters it is: {inches*2.54:.1f}")
    inches = float(input(prompt))


#3

prompt = "Enter a number: "
a = input(prompt)
if a != "":
    smallest = int(a)
    largest = smallest
    while a != "":
        n = int(a)
        if n < smallest:
            smallest = n
        elif n > largest:
            largest = n
        a = input(prompt)
    else:
        print(f"The smallest number is {smallest}, and the largest is {largest}")

#4

import random
number = random.randint(1,10)
prompt = "Guess the number! "
guess = int(input(prompt))
while number != guess:
    if guess > number:
        print("Too high")
    else:
        print("Too low")
    guess = int(input(prompt))
else:
    print("Correct!")


#5

username = "python"
password = "rules"
n = 5
while n >= 0:
    u = input("Username: ")
    p = input("Password: ")
    if u == username and p == password:
        print("Welcome!")
        break
    n = n - 1
else:
    print(f"Either your password or username you entered is incorrect.")

"""

#6
import random
N = int(input("How many random points to generate?"))
n = 0
i = 0
while i < N:
    x = random.uniform(-1., 1.)
    y = random.uniform(-1., 1.)

    if x**2 + y**2 < 1.:
        n = n + 1

    i = i + 1
pi = 4.*n/N
print(f"Pi is {pi}")