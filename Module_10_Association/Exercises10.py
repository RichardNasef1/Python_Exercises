 #1
""" 
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        self.current_floor += 1
        print(f"Elevator is on floor {self.current_floor}")

    def floor_down(self):
        self.current_floor -= 1
        print(f"Elevator is on floor {self.current_floor}")

    def go_to_floor(self, floor):
        if floor > self.current_floor:
            while self.current_floor < floor:
                self.floor_up()

        elif floor < self.current_floor:
            while self.current_floor > floor:
                self.floor_down()


#2 

class Building:
    def __init__(self, bottom_floor, top_floor, number_of_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []

        for i in range(number_of_elevators):
            elevator = Elevator(bottom_floor, top_floor)
            self.elevators.append(elevator)

    def run_elevator(self, elevator_number, destination_floor):
        elevator = self.elevators[elevator_number - 1]
        elevator.go_to_floor(destination_floor)

#3

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom_floor)


building = Building(1, 10, 3)

building.run_elevator(1, 5)
 """

#4

import random


class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, value):
        self.current_speed += value

        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)

    def print_status(self):
        print(f"\n{self.name}")
        print(f"{'Registration':<15}{'Speed':<10}{'Distance':<15}{'Max speed':<10}")

        for car in self.cars:
            print(f"{car.registration_number:<15}"
                f"{car.current_speed:<10}"
                f"{car.travelled_distance:<15.1f}"
                f"{car.maximum_speed:<10}")
            
    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True

        return False


cars = []

for i in range(10):
    car = Car(f"ABC-{i + 1}", random.randint(100, 200))
    cars.append(car)

race = Race("Grand Demolition Derby", 8000, cars)

hour = 0

while not race.race_finished():
    race.hour_passes()
    hour += 1

    if hour % 10 == 0:
        race.print_status()

race.print_status()