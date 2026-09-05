print('Hello, world!')

print('"Hello", said Joe')

print("Good")
print("morning")

print("Good\nmorning")

user = input('Enter your name: ')
print("Nice to meet you, " + user + "!")

points = 50  # points is now 50
print(points)  # prints: 50

points = 120  # now points is 120
print(points)  # prints: 120

print(user)

""" primitive data types

string (string)
number (number),
  integer (int), -9  12_456_123_180
 floating-point number (float) 4.973
 complex number (complex)  -4 + 2j
boolean (boolean) True or False

In addition, other Python data structures can be assigned to variables, such as:

list (list)
tuple (tuple)
dictionary (dictionary)

            String Data Type

single (') or double (") quotation marks


        Mathematical Operations and Type Conversion

fahrenheit_str = input("Enter a temperature in Fahrenheit: ")
fahrenheit = float(fahrenheit_str)
celsius = (fahrenheit-32)*5/9
print("The temperature in Celsius: " + str(celsius))

        Output Formatting

print(f"The temperature in Celsius: {celsius:6.2f}")

.5f: floating-point number with five decimal places
10.2f: floating-point number with two decimal places in a field ten characters wide
<20s: string in a field 20 characters wide, aligned to the left
8d: integer in a field eight characters wide

import math

print(f"{'Pi':12s}:{math.pi:10.5f}")
print(f"{'e':12s}:{math.e:10.5f}")





 """