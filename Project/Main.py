from Classes.items import *
from Classes.player import *
from Classes.rooms import *
import time


print(cat_food)
a = .2
user = input("What is your name? ")
age = int(input("How old are you? "))


if age < 12:
    print(f"Hello {user}! You are a minor. You need to be at least 12 years old to play this game.")

else:
    print(f"Welcome {user} to Dude Where's my cat!")
    print("You just entered your apartment after a long day of classes at Metropolia University")
    print("All you want to do is lay on the couch with a bag of chips, the remote and your two year old cat who just learned how to hide!")

    inventory =  ["keys"]

    def search_room():
        print("You search the apartment for your black cat...")
        print("You don't find the cat yet.")

    while True:

        print("You are in your apartment, looking for your black cat.")
        print("1. Search the apartment")
        print("2. Show your inventory")
        print("3. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            search_room()
        elif choice == "2":
            show_inventory()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
