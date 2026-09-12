""" #### Structure of a function
def greet(): Name
    print("Hello!")  task
    return      end   (not needed)

###calling a function

greet()


#3 Function parameters

    def greet(times):
    for i in range(times):
        print("Round " + str(i+1) + " of saying hello.")
    return

print("A new day starts with greetings.")
greet(5)
print("Let's greet some more.")
greet(2)


####Research varaiable types 


#4 Variable scope

global variables touches the left side of the code
    local is inside a function
global (can be changed inside a function using this)
    local


#5 Multiple parameters (NEED TO RESEARCH THIS)

def greet(greeting, times):
    for i in range(times):
        print(greeting + " round: " + str(i+1))
    return

#6 Return value

def sum_of_squares(first, second):
    result = first**2 + second**2
    return result

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
result = sum_of_squares(number1, number2)
print(f"The sum of squares for numbers {number1:.3f} and {number2:.3f} is {result:.3f}.")


#7 List as a parameter

def inventory(items):
    print("You have the following items:")
    for item in items:
        print("- " + item)
	  # Items disappear during the inventory
    items.clear()
    return

backpack = ["Water bottle", "Map", "Compass"]
inventory(backpack)
backpack.append("Swiss Army knife")
inventory(backpack)


(should not edit the global list , use .copy)

#8 More characteristics of functions

def sum(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print("Sum is", sum(1, 2, 3))




def greet(greeting="Hello", times=1):
    for i in range(times):
        print(greeting + " " + str(i+1) + ". time")
    return

greet()
greet(greeting="Hi", times=3)
greet(times=2, greeting="Hey")




            ###########EXAMPLES ################ 
https://github.com/ilkkamtk/python-tuntiesimerkit/blob/main/README_en.md
 """
1. 

def calculate_sum (num1, num2):
    sum = num1 + num2
    return sum

test = calculate_sum(234,2412)

print(test)

2.

def filter_list(strings):
    filered_strings = []

    for string in strings:
        if len(string) > 5:
            filered_strings.append(string)

    return filered_strings

animal_names = ["cat", "dog", "elephant", "lion", "giraffe"]

filter_list =  filter_list(animal_names)

print(animal_names)
print(filter_list)





#6 
import math

def price_of_pizza(diameter,price):
    area= math.pi * (diameter ** 2)


pizza1 = price_of_pizza(20, 23)
pizza2 = price_of_pizza(40,28)

if pizza1 < pizza2:
    print(f"Pizza 1 is {100 - 100 * pizza1/ pizza2:.0f}% cheaper")
else:
    print(f"Pizza 2 is {100 - 100 * pizza2/ pizza1:.0f}% cheaper")