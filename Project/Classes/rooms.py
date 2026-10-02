class Room:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

hallway = Room("Hallway")
kitchen = Room("Kitchen")
bathroom = Room("Bathroom")
bedroom = Room("Bedroom")
living_room = Room("Living Room")