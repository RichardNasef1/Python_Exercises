class Player:
    def __init__(self, name, location):
        self.name = name
        self.inventory = []
        self.location = location

    def add_item(self,item):
        self.inventory.append(item)
        print(f"You added {item} to your inventory.")
    
    def show_inventory(self,inventory):
        print("Your inventory: {inventory} ")
          