""" #Lists

shopping_list = ["apple","butter","milk","eggs"]
print(shopping_list)
shopping_list[2] = "almond milk"
#changing a value from the list
shopping_list.append("rice")  #add new item to list
shopping_list.insert(1, "chicken") #add item to the designated list location 
print(shopping_list)

#slice the list 

print(shopping_list[:2])
print(shopping_list[2:])


#remove a vaulue

shopping_list.pop(3)
#remove using  remove
shopping_list.remove("butter")


#expand a list
shopping_list2 =["pasta","ice_cream"]
(shopping_list.extend(shopping_list2))
print(shopping_list)


#check iof an item exists:
if "pasta" in shoppping_list:
    print("hurra") 


# to sort a list's items in alpha or # order 
shopping_list.sort
print(shopping_list) 

for number in range(0,11):
    print(number)

for number in range(5):
    print("cheers!")

#example !
name = input("Enter your name: ")
for character in name:
    print(character)

#example 2 
number = int(input("Give a numbner: ")) 
if number <= 0:
    print("Error: Please enter a positive number")
else:
    for i in range(0,number+1, 2):
        if i % 2 == 0:
            print(i)


#example 3 

number_list = []
while True:
    entry_number = input("Enter a number: ")
    if entry_number == "":
        break
    number_list.append(int(entry_number))

printed_list = []
for num in number_list:
    if num > 100 and num not in printed_list:
        print(num)
        printed_list.append(num)

#example 4:

sentence = input("Enter a sentence: ") 
sentence = " " + sentence
for index_number in range(1, len(sentence)):
    if sentence[index_number - 1]== " " and sentence[index_num] != " ":
        print(sentence[index_num])
    index_number += 1 """