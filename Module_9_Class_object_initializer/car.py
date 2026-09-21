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
         self.current_speed * hours == self.travelled_distance

                  