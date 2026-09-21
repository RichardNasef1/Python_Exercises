""" 
Ex#1


class ShoppingList:
    def __init__(self):
        self.items = []

    def add_items(self, item:str):
        if not item in self.items:
            self.items.append(item)

    def print_list(self):
        for item in sorted(self.items):
            print(item)

    def longest_name(self):
        helper1 = ""
        helper2 = 0
        for item in self.items:
            if len(item) > self.helper2:
                helper2 = len(item)
                helper1 = item

        print(f"The item that has the longest name is {helper1})
        return helper1
veget = ShoppingList()
veget.add_items("tomato")
veget.add_items("spaghetti")
veget.add_items("parmesan")
veget.print_list()
veget.longest_name()




#temp association Ex#2

class Car:
    def __init__(self, plate_number, color):
        self.plate_number = plate_number
        self.color = color

class PaintShop:
    def paint(self,car,color):
        car.color = color

car = Car ("ABC-999", "blue")
print("The car is now: " + car.color)


class Visitor:
    def __init__(self,name: str, height: int):
        self.name = name
        self.height = height

class Attractions:
    def __init__(self,name: str, min_height: int):
         self.visitor_list = []
         self.name = name
         self.min_height = min_height

    def check_height (self, person : Visitor):
        if person.height >= self.min.height:
            self.visitor_list.append(person)
            print(f"{person.name} gets on board")
        else:
            print(f"{person.name} is too short! Sorry")

    def __str__(self):
        for person in self.visitor_list:
            print(person.name)
        return f"{self.name} ({len(self.visitor_list)}visitors)"

roller_coaster = Attractions("Roller coaster", 120)
sanduni = Visitor("Sanduni", 168)
muna = Visitor("Muna",165)
aurora = Visitor("Aurora", 118)

roller_coaster.check_height(sanduni)

class People:
    def __init__(self, name :str, height :int):
        self.name = name
        self.height= height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.people = []

    def add(self, person:People):
        self.people.append(person)

    def is_empty(self):
        return len(self.people) == 0
    
    def print_info(self):
        print(f"There are {len(self.people)}"
              f"in people in the classroom")
        for person in self.people:
            print (f"-{person.name} ({person.height}cm)")

    def check_tallest(self):
        tallest_per = None
        for person in self.people:
            if tallest_per is None or person.height > height_tallest:
                tallest_per = person
                height_tallest = person.height
        return tallest_per

    
    def remove_tallest(self):
        tallest_per = self.check_tallest()
        if tallest_per:
            self.people.remove(tallest_per)
        return tallest_per

room1 = Room()
print("Whether the room is empty?", room1.is_empty())
print("The tallest person is :", room1.check_tallest())

room1.add(People("sanduni",186))
room1.add(People("sanduni",186))
room1.add(People("sanduni",186))
room1.add(People("sanduni",186))

 """


