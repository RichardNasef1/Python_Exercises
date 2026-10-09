from .items import *
from colorama import Fore, Style

class Player:
    def __init__(self, name, location):
        self.name = name
        self.inventory = []
        self.location = location


    def take_item(self, room, item):
        if item in room.items:
            room.items.remove(item)
            self.inventory.append(item)
            print(Fore.GREEN + f"You picked up {item.name}." + Style.RESET_ALL)
        else:
            print(Fore.RED + "That item is not here." + Style.RESET_ALL)

    def show_inventory(self):
        if len(self.inventory) == 0:
            print("Your inventory is empty.")
        else:
            print("Your inventory:")
        
            for item in self.inventory:
                print(item.name)
          