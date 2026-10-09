from .items import *

class Room:
    def __init__(self, description, name,searchable_things):
        self.name = name
        self.description = description
        self.items = []
        self.connected_rooms = []
        self.searchable_things = searchable_things

    def add_item(self, item):
        self.items.append(item)

    def connect_room(self, room):
        self.connected_rooms.append(room)


    def search_menu(self):
    
        number = 1

        for thing in self.searchable_things:
            print(f"{number}. {thing.name}")
            number = number + 1

        print(f"{number}. Go back")

        return input("What do you want to search? ")


    def movement_menu(self):
        print("Where do you want to go?")

        number = 1

        for room in self.connected_rooms:
            print(f"{number}. {room.name}")
            number = number + 1

        print(f"{number}. Go back")
        print()

        return input("Choose a room: ")
