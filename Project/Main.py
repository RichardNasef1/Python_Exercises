from Classes.items import *
from Classes.player import *
from Classes.rooms import *
from Classes.searchable import *
from Classes.intro import game_intro
import time
import random
from colorama import Fore, Style
import json
import os

time_delay = .5

key_hook = Searchable("Key hook")

fridge = Searchable("Fridge")
cabinet = Searchable("Cabinet")
counter = Searchable("Counter")

sink = Searchable("Sink")
shower = Searchable("Shower")
bathroom_cabinet = Searchable("Bathroom Cabinet")

bed = Searchable("Bed")
closet = Searchable("Closet")
laundry_basket = Searchable("Laundry basket")

couch = Searchable("Couch")
tv = Searchable("TV")
coffee_table = Searchable("Coffee table")
searchables = [key_hook,fridge,cabinet,counter,sink,shower,bathroom_cabinet,bed,closet,laundry_basket,couch,tv,coffee_table]

cat_food = Item("cat food","Your cat's favorite food, they usually runs straight to you when they hears you open the package")
empty_food_bowl = Item("empty cat food bowl","Your cat's empty food bowl")
empty_water_bowl = Item("empty water bowl","Your cat has been thirsty")
smelly_sock = Item("smelly sock","Just a smelly sock")
keys = Item("keys","Apartment keys")
long_cat_toy = Item("long cat toy","Your cat's favorite toy, they goes feral when they sees this!")
remote_control = Item("remote control","The remote for the television. You need this if you want to watch your show.")
hot_cheetos = Item("hot cheetos","The last bag of Hot Cheetos. You've been thinking about these all day.")

items = {
    "cat food": cat_food,
    "empty cat food bowl": empty_food_bowl,
    "empty water bowl": empty_water_bowl,
    "smelly sock": smelly_sock,
    "keys": keys,
    "long cat toy": long_cat_toy,
    "remote control": remote_control,
    "hot cheetos": hot_cheetos
    }

hallway = Room(" Not much is here, it connects all the rooms in your apartment.","Hallway",[key_hook])
kitchen = Room(" You see cabinets,a counter and a fridge","Kitchen",[fridge, cabinet, counter])
bathroom = Room(" You see a sink, shower, and toilet.","Bathroom",[sink, shower, bathroom_cabinet])
bedroom = Room(" It's so messy in here, you can't remember the last time you cleaned up.","Bedroom",[bed, closet, laundry_basket])
living_room = Room(" You're favorite show just released the last episode of the final season but can't watch it until your cat is settled!","Living Room",[couch, tv, coffee_table])


hallway.connect_room(living_room)
hallway.connect_room(bedroom)
hallway.connect_room(bathroom)
hallway.connect_room(kitchen)


kitchen.connect_room(living_room)
kitchen.connect_room(hallway)

bathroom.connect_room(hallway)

bedroom.connect_room(living_room)
bedroom.connect_room(hallway)

living_room.connect_room(kitchen)
living_room.connect_room(bedroom)
living_room.connect_room(hallway)

fridge.add_item(cat_food)
cabinet.add_item(hot_cheetos)

bathroom_cabinet.add_item(smelly_sock)
sink.add_item(empty_water_bowl)

bed.add_item(long_cat_toy)

couch.add_item(remote_control)
coffee_table.add_item(empty_food_bowl)



def item_menu(player, searchable):
    if len(searchable.items) == 0:
        return
    
    print("You find:")

    number = 1

    for item in searchable.items:
        print(f"{number}. {item.name}")
        number = number + 1

    print(f"{number}. Leave everything")


    item_choice = int(input("What do you want to take? "))

    if item_choice == number:
        print("You leave everything.")

    elif item_choice >= 1 and item_choice <= len(searchable.items):
        selected_item = searchable.items[item_choice - 1]
        player.take_item(searchable, selected_item)

    else:
        print("Invalid choice.")



def save_game(player, cat, cat_location, cat_settled):

    save_data = {
        "user": player.name,
        "cat": cat,
        "location": player.location.name,
        "cat_location": cat_location.name,
        "cat_settled": cat_settled,
        "inventory": [],
        "searchables": {}
    }

    for item in player.inventory:
        save_data["inventory"].append(item.name)

    for searchable in searchables:
        save_data["searchables"][searchable.name] = []

        for item in searchable.items:
            save_data["searchables"][searchable.name].append(item.name)

    with open("savegame.json", "w") as file:
        json.dump(save_data, file)

    print("Game saved!")



def load_game(user):

    if not os.path.exists("savegame.json"):
        return None

    with open("savegame.json", "r") as file:
        save_data = json.load(file)

    if save_data["user"] == user:
        print("Save game found!")
        return save_data

    else:
        print("No save game found for that name.")
        return None


    
## Game Start ##
user = input("What is your name? ")

#save data load
save_data = load_game(user)

if save_data != None:

    cat = save_data["cat"]

    if save_data["location"] == "Hallway":
        player_location = hallway
    elif save_data["location"] == "Kitchen":
        player_location = kitchen
    elif save_data["location"] == "Bathroom":
        player_location = bathroom
    elif save_data["location"] == "Bedroom":
        player_location = bedroom
    elif save_data["location"] == "Living Room":
        player_location = living_room

    player = Player(user, player_location)

    for item_name in save_data["inventory"]:
        player.inventory.append(items[item_name])

        for searchable in searchables:
            searchable.items = []

    for searchable in searchables:

        saved_items = save_data["searchables"][searchable.name]

        for item_name in saved_items:
            searchable.items.append(items[item_name])

    cat_settled = save_data["cat_settled"]

    if save_data["cat_location"] == "Bedroom":
        cat_location = bedroom
    elif save_data["cat_location"] == "Kitchen":
        cat_location = kitchen
    elif save_data["cat_location"] == "Bathroom":
        cat_location = bathroom

    print(f"Welcome back, {user}!")

else:

    age = int(input("How old are you? "))

    if age < 12:
        print(f"Hello {user}! You need to be at least 12 years old to play this game.")
        quit()

    cat = input("If you had a cat, what would you name them? ")

    player = Player(user, hallway)
    player.inventory.append(keys)

    cat_location = random.choice([bedroom, kitchen, bathroom])
    cat_settled = False

game_won = False


game_intro(user, cat, time_delay)

#main menu
while True:
    print()
    print(f"-You are in the {Fore.CYAN}{player.location.name}{Style.RESET_ALL}.{player.location.description}")
    print("-----------------------------------------------------------------------------------------------------------------------------")
    print("1. Search the room")
    print("2. Check your inventory")
    print("3. Go to another room")
    print("4. Quit and Save")

    choice = input("What do you want to do? ")
#search the room
    if choice == "1":
        print()
        print(f"In the {player.location.name} you see the following. ")
        print()

        while True:
            search_choice = player.location.search_menu()

            if player.location == hallway:

                if search_choice == "1":
                    print("You look at the key hook.")

                    if keys in player.inventory:
                        print("You hang your keys on the key hook.")
                        print()
                        player.inventory.remove(keys)
                        key_hook.add_item(keys)

                    else:
                        print("Your keys are already hanging on the key hook.")
                        print()

                elif search_choice == "2":
                    print("You stop searching the hallway.")
                    print()
                    break

                else:
                    print("Invalid choice.")
            if player.location == kitchen:

                if search_choice == "1":
                    print("You open the fridge.")
                        
                    if cat_location == kitchen and cat_settled == False and cat_food in player.inventory and empty_food_bowl in player.inventory:



                        print()
                        time.sleep(time_delay)
                        print(Fore.YELLOW + f"You hear {cat} meowing somewhere in the kitchen." + Style.RESET_ALL)
                        time.sleep(time_delay)
                        print("You put some food into the empty food bowl.")
                        time.sleep(time_delay)
                        print(Fore.GREEN + f"{cat} comes running over to eat!" + Style.RESET_ALL)
                        time.sleep(time_delay)

                        player.inventory.remove(cat_food)
                        player.inventory.remove(empty_food_bowl)

                        print(Fore.GREEN + f"{cat} is happily eating their food." + Style.RESET_ALL)
                        time.sleep(time_delay)
                        print(Fore.GREEN + "Now it's time to relax on the couch with your favorite bag of chips." + Style.RESET_ALL)
                        cat_settled = True
                

                    else:
                        print()
                        time.sleep(time_delay)
                        print(Fore.YELLOW + f"You hear {cat} somewhere in the kitchen." + Style.RESET_ALL)
                        time.sleep(time_delay)
                        print(Fore.YELLOW + "Maybe you can lure them out with their favorite food." + Style.RESET_ALL)
                        time.sleep(time_delay)

                    item_menu(player, fridge)

                elif search_choice == "2":
                    print("You open the cabinets.")
                    item_menu(player, cabinet)

                elif search_choice == "3":
                    print("You search the counter.")
                    item_menu(player, counter)

                elif search_choice == "4":
                    print("You stop searching the kitchen.")
                    break
                else:
                    print("Invalid choice.")

            elif player.location == bathroom:
                if search_choice == "1":
                    print("You search the sink.")
                    print()
                    
                    if cat_location == bathroom and cat_settled == False:

                            if empty_water_bowl in player.inventory:

                                print()
                                time.sleep(time_delay)
                                print(Fore.YELLOW + f"You hear {cat} meowing from somewhere in the bathroom." + Style.RESET_ALL)
                                time.sleep(time_delay)
                                print("You fill the empty water bowl with fresh water.")
                                time.sleep(time_delay)

                                player.inventory.remove(empty_water_bowl)

                                print(Fore.GREEN + f"{cat} comes running over for a drink!" + Style.RESET_ALL)
                                time.sleep(time_delay)
                                print(Fore.GREEN + f"{cat} is happily drinking the water." + Style.RESET_ALL)
                                time.sleep(time_delay)
                                print(Fore.GREEN + "Now it's time to relax on the couch with your favorite bag of chips." + Style.RESET_ALL)

                                cat_settled = True

                            else:
                                print()
                                time.sleep(time_delay)
                                print(Fore.YELLOW + f"You hear {cat} somewhere in the bathroom." + Style.RESET_ALL)
                                time.sleep(time_delay)
                                print(Fore.YELLOW + "Maybe they are thirsty." + Style.RESET_ALL)
                                time.sleep(time_delay)
                    item_menu(player, sink)

                elif search_choice == "2":
                    print("You open the curtains to your shower and find NOTHING.")
                    print()
                    item_menu(player, shower)

                elif search_choice == "3":
                    print(f"You open the cabinet and find some cleaning supplies, it's no time for cleaning right now! {cat} needs you!! ")
                    print()
                    item_menu(player,bathroom_cabinet)
                elif search_choice == "4":
                    print("You stop searching the bathroom.")
                    print()
                    break
                else:
                    print("Invalid choice.")

            elif player.location == bedroom:
                if search_choice == "1":
                    print("You look under your bed")
                    print()

                    if cat_location == bedroom and cat_settled == False:

                        if long_cat_toy in player.inventory:
                            print()
                            print(Fore.YELLOW + f"You hear {cat} moving under the bed." + Style.RESET_ALL)
                            time.sleep(time_delay)
                            print("You wave the long cat toy around.")
                            time.sleep(time_delay)
                            print(Fore.GREEN + f"{cat} comes running out from under the bed!" + Style.RESET_ALL)
                            time.sleep(time_delay)
                            print(Fore.GREEN + f"You found {cat}!" + Style.RESET_ALL)
                            time.sleep(time_delay)
                            print(Fore.GREEN + "Now it's time to relax on the couch with your favorite bag of chips." + Style.RESET_ALL)
                            cat_settled = True
                        else:
                            print()
                            print(Fore.YELLOW + f"You hear {cat} under the bed, but they won't come out." + Style.RESET_ALL)
                            time.sleep(time_delay)
                            print(Fore.YELLOW + "Maybe there is something you can use to lure them out." + Style.RESET_ALL)
                            time.sleep(time_delay)
                    item_menu(player, bed)

                elif search_choice == "2":
                    print("You open your closet.")
                    print()
                    item_menu(player, closet)

                elif search_choice == "3":
                    print("You dig through your laundry basket, You've been avoiding doing laundry for a week now.")
                    print()
                    item_menu(player, laundry_basket)

                elif search_choice == "4":
                    print("You stop searching the bedroom.")
                    print()
                    break
                else:
                    print("Invalid choice.")

            elif player.location == living_room:
                if search_choice == "1":
                    print("You search the couch.")
                    print()
                    item_menu(player, couch)

                    if cat_settled == True:

                        if remote_control in player.inventory and hot_cheetos in player.inventory:

                            print()
                            print(Fore.GREEN + "You have everything you need." + Style.RESET_ALL)
                            time.sleep(time_delay)
                            print(Fore.GREEN + f"{cat} is settled." + Style.RESET_ALL)
                            time.sleep(time_delay)
                            print(Fore.GREEN + "You have your Hot Cheetos." + Style.RESET_ALL)
                            time.sleep(time_delay)
                            print(Fore.GREEN + "You have the remote." + Style.RESET_ALL)
                            time.sleep(time_delay)
                            print()
                            print("You sit down on the couch.")
                            time.sleep(time_delay)
                            print("You turn on the TV...")
                            time.sleep(time_delay)
                            print(f"{cat} jumps on your lap ready to steal a hot cheeto.")
                            time.sleep(1)
                            print("Your favorite show begins.")
                            time.sleep(1)
                            print(Fore.RED + "Y" + Fore.YELLOW + "O" + Fore.GREEN + "U" + Fore.CYAN + " " + Fore.BLUE + "W" + Fore.MAGENTA + "I" + Fore.RED + "N" + Style.RESET_ALL)
                            
                            game_won = True
                            break

                elif search_choice == "2":
                    print("You look behind the TV.")
                    print()
                    item_menu(player, tv)

                elif search_choice == "3":
                    print("You check under the coffee table.")
                    print()
                    item_menu(player, coffee_table)

                elif search_choice == "4":
                    print("You stop searching the living room.")
                    print()
                    break
                else:
                    print("Invalid choice.")

#inventory
 

    elif choice == "2":
        print()
        player.show_inventory()

#move to another room
    elif choice == "3":
        room_choice = player.location.movement_menu()

        if room_choice != str(len(player.location.connected_rooms) + 1):
            player.location = player.location.connected_rooms[int(room_choice) - 1]
#save and quit
    elif choice == "4":
        save_game(player, cat, cat_location, cat_settled)
        print(f"Goodbye {user}!")
        break

    else:
        print("Invalid choice.")
        
    if game_won == True:
        break



