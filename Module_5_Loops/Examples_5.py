""" #Loop structure (while)

while condition: 
	block to be repeated

#Example 1: Fixed amount of repetitions

rounds = int(input("How many greetings: "))
finished_rounds = 0
while finished_rounds<rounds:
    print("Good morning")
    finished_rounds = finished_rounds + 1   

#Example 2: User ends the repetition

    command = input("Enter command: ")
while command != "stop":
    print("Executing command: " + command)
    command = input("Enter command: ")
print("Execution stopped.")

#Example 3: Varying amount of repetitions

import random
dice1 = dice2 = rolls = 0
while (dice1 != 6 or dice2 != 6):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    rolls = rolls + 1
print(f"Rolled {rolls:d} times.")

#Nested loops

first = 1
while first <= 5:
    second = 1
    while second <= 5:
        print(f"{first} times {second} is {first*second:d}")
        second = second + 1
    first = first + 1

import random
rounds = 0
total_rolls = 0

while rounds < 100000:
    dice1 = dice2 = rolls = 0
    while (dice1 != 6 or dice2 != 6):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
	rolls = rolls + 1
    #print(f"Rolled {rolls:d} times.")
    rounds = rounds + 1
    total_rolls = total_rolls + rolls

average_rolls = total_rolls/rounds
print(f"Average rolls required: {average_rolls:6.2f}")

#breaks

command = input("Enter command: ")
while command != "stop":
    if command == "MAYDAY":
        break
    print("Executing command: " + command)
    command = input("Enter command: ")
print("Execution stopped.")

#While-else

command = input("Enter command: ")
while command != "stop":
    if command == "MAYDAY":
        break
    print("Executing command: " + command)
    command = input("Enter command: ")
else:
    print("Goodbye.")
print("Execution stopped.")


#Infinite loop
When a loop isnt closed correctly 

            #Examples

#1

positive_int = int(input("Enter a positive integer: "))

if positive_int > 0:
    number = 0
    while number <= positive_int:
        if number % 2 == 0:
            print (number)
        number = number + 1
else:
    print("Positive Integers Only!")

#2

sum = 0
amount = 0
while sum <= 1000:
    integer = int(input("Enter an integer: "))
    sum = sum + integer
    amount = amount + 1
print (f"Final sum:{sum}")
print(f"Number of numbers: {amount}")

"""
