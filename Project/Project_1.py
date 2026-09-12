user = input("What is your name? ")
age = int(input("How old are you? "))

if age < 12:
    print(f"Hello {user}! You are a minor.")

else:
    print(f"Welcome {user}! You are {age} years old!")

    inventory =  []

    def add_item():
        inventory.append("cat food")
        print("You found some cat food and added it to your inventory.")

    def show_inventory():
        print("Your inventory:")
        for item in inventory:
            print(item)

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
        