#1
class Car:
    def __init__(self,registration_number,maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0


#2


    def accelerate(self,value):
            self.current_speed += value
            if self.current_speed > self.maximum_speed :
                 self.current_speed = self.maximum_speed
            if self.current_speed < 0:
                 self.current_speed = 0


#3



    def drive(self,hours):
        self.travelled_distance += self.current_speed * hours

                  
car = Car("ABC-123",142)

print(f"Registration number is {car.registration_number},maximum speed: {car.maximum_speed}")

car.accelerate(30)
car.accelerate(70)
car.accelerate(50)

print(f"Current speed: {car.current_speed}")

car.accelerate(-200)
print(f"Current speed: {car.current_speed}")
print(f"Distance travelled: {car.travelled_distance}")

car.accelerate(100)
car.drive(20.9)

print(f"Current speed: {car.current_speed}")
print(f"Distance travelled: {car.travelled_distance}")


#4 I needed some assistance with this one and did further research on how to format the information into a clear


import random

cars = []
race_finished = False

for i in range(1, 11):
    maximum_speed = random.randint(100, 200)
    registration_number = f"ABC-{i}"

    car = Car(registration_number, maximum_speed)
    cars.append(car)

while not race_finished:
    for car in cars:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)
        car.drive(1)

    for car in cars:
        if car.travelled_distance >= 10000:
            race_finished = True

print("Registration Number | Maximum Speed | Final Speed | Distance")

for car in cars:
    print(f"{car.registration_number:<20} "
          f"{car.maximum_speed:<15} "
          f"{car.current_speed:<12} "
          f"{car.travelled_distance:.2f}")
