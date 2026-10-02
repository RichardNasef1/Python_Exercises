# #1 
# ""
publications=[]

class publication:
    
    def __init__(self,name):
        self.name = name
    
    def print_information(self):
        print(f"{self.name}")

class book(publication):
    def __init__(self,name,author,page_count):
        self.author = author
        self.page_count = page_count
        super().__init__(name)

    def print_information(self):
        super().print_information()
        print(f"Author:{self.author} Page Count:{self.page_count}")

class magazine(publication):

    def __init__(self, name,chief_editor):
        self.chief_editor = chief_editor
        super().__init__(name)

    def print_information(self):
        super().print_information()
        print(f"Chief Editor:{self.chief_editor}")

publications.append(magazine("Donald Duck","Aki Hyyppä"))
publications.append(book("Compartment No.6","Rosa Liksom","192 pages"))

for e in publications:
    e.print_information()


#2 didnt like using the list method for this example 

cars = []

class Car:
    def __init__(self,registration_number,maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self,value):
            self.current_speed += value
            if(self.current_speed > self.maximum_speed):
                 self.current_speed = self.maximum_speed
            if(self.current_speed < 0):
                 self.current_speed = 0

    def drive(self,hours):
         self.travelled_distance = self.current_speed * hours

class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed,battery_cap):
        super().__init__(registration_number, maximum_speed)
        self.battery_cap = battery_cap

class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed,tank):
        super().__init__(registration_number, maximum_speed)
        self.tank = tank

cars.append(ElectricCar("ABC-15",180,52.5))
cars.append(GasolineCar("ABC-123",165,32.3))

cars[0].accelerate(50)
cars[1].accelerate(40)
cars[0].drive(3)
cars[1].drive(3)

print (cars[0].travelled_distance)
print (cars[1].travelled_distance)