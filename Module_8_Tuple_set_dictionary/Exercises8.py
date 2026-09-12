
#1
seasons = ("winter", "spring", "summer", "autumn")
month = int(input("Enter the number of a month: "))

if month == 12 or month == 1 or month == 2:
    print(seasons[0])
elif month == 3 or month == 4 or month == 5:
    print(seasons[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons[2])
elif month == 9 or month == 10 or month == 11:
    print(seasons[3])
else:
    print("Invalid month")


#2
names = set()
name = input("Enter a name to add to the list, if you wish to see full list press Enter: ")
while name != "":
    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)
    name = input("Enter a name to add to the list, if you wish to see full list press Enter: ")
print("Names entered:")
for name in names:
    print(name)

#3

airports = {}

while True:
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")
    choice = input("Choose an option: ")
    if choice == "1":
        icao = input("Enter the ICAO code: ")
        airport =input("Enter the airport name:")
        airports[icao] = airport
    elif choice == "2":
        icao_choice = input("Please enter the ICAO code:")
        if icao_choice in airports:
            print(f"The airport is {airports[icao_choice]}")
        else:
            print("This airport is not found in this database")
    elif choice == "3":
        print("Thank you for using this database: Moi moi")
        break