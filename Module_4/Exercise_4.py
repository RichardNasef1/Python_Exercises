#4. Conditional structures (if)

###1.

""" min_length = 42
length = int(input("Please enter the length of the zander in cm here: "))
if length <= min_length:
    print(f"This zander is {min_length - length} cm too small. Please return it to the waters")
else: 
    print ("Nice catch! This zander is big enough to take home!")
 
###2.

cabin = input("Welcome aboard! Please enter your cabin class: ")
if cabin == "LUX": 
    print("LUX: upper-deck cabin with a balcony.")
elif cabin == "A":
    print("A: above the car deck, equipped with a window.")
elif cabin == "B":
    print("B: windowless cabin above the car deck.")
elif cabin == "C":
    print("C: windowless cabin below the car deck.")
else:
    print("Invalid cabin class")

###3. 

gender = input("What is your biological gender? ")
hemo = float(input("What is your hemoglobin value (g/l)? "))
if gender == "male" and hemo <= 137:
    print("Your hemoglobin levels are low!")
elif gender == "male" and  137 <= hemo <= 167:
    print("Your hemoglobin levels are normal.")
elif gender == "male" and hemo > 167:
    print("Your hemoglobin levels are high!")
elif gender == "female" and hemo <= 117:
    print("Your hemoglobin levels are low!")
elif gender == "female" and  117 <= hemo < 155:
    print("Your hemoglobin levels are normal.")
elif gender == "female" and hemo >= 155:
    print("Your hemoglobin levels are high!")
else:
    print("Please double check all answers and try again. ")
"""
###4.
year = int(input("Please enter a year, any year! "))
if year % 400 ==0 or year % 4 == 0 and year % 100 > 0:
        print(f"The year {year} is a leap year!") 
else:
        print(f"The year {year} is not a leap year!")