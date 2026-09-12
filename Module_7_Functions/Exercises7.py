""" 
#1 
import random


def dice_roll():
    return random.randint(1,6)
    
dice = dice_roll()
while dice != 6:
    print(dice)
    dice = dice_roll()
print(dice) 

#2
import random
sides = int(input("How many sides do you want on your die?"))

def dice_roll(sides):
    return random.randint(1,sides)

dice = dice_roll(sides)
while dice != sides:
    dice = dice_roll(sides)
    print(dice)
print(dice)

#3
gallons = float(input("How many gallons of gasoline?"))

def gallon_con(gallons):
    liters = gallons *  3.78541
    return liters

while gallons >= 0:
    litres = gallon_con(gallons)
    print(f"{gallons} gallon(s) is {litres} litres")
    gallons = float(input("How many gallons?"))

#4

numlist =(2,4,6,82)

def calulate_sum(numlist):
    total =  0
    for number in numlist:
        total = total + number 
    return total

total = calulate_sum(numlist)
print(total)

#5

numlist = (1,2,3,4,5,6,7,8,9,10,11,12,13)
print(numlist)

def sort_nums(numlist):
    even_nums = []
    for number in numlist:
        if number % 2 == 0:
            even_nums.append(number)
    return even_nums

even_nums = sort_nums(numlist)

print("Orginal list:", numlist)
print("List with odd numbers removed:", even_nums)

#6

import math

def price_of_pizza(diameter,price):
    radius = diameter / 2
    area_cm = math.pi * (radius ** 2)
    area_m = area_cm / 10000
    unit_price = price / area_m
    return unit_price

diameter1 = float(input("Enter the diameter of pizza 1 in cm: "))
price1 = float(input("Enter the price of pizza 1 in euros: "))

diameter2 = float(input("Enter the diameter of pizza 2 in cm: "))
price2 = float(input("Enter the price of pizza 2 in euros: "))

pizza1 = price_of_pizza(diameter1,price1)
pizza2 = price_of_pizza(diameter2, price2)

if pizza1 < pizza2:
    print("Pizza 1 provides better value for money.")
elif pizza2 < pizza1:
    print("Pizza 2 provides better value for money.")
else:
    print("Both pizzas provide the same value for money.")


    """