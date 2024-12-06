class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_speed):
        self.current_speed += change_speed
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

    def show_info(self):
        print("Registration Number:", self.registration_number)
        print("Maximum Speed:", self.maximum_speed, "km/h")
        print("Current Speed:", self.current_speed, "km/h")
        print("Travelled Distance:", self.travelled_distance, "km")

class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed, battery_capacity):
        super().__init__(registration_number, maximum_speed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed, tank_volume):
        super().__init__(registration_number, maximum_speed)
        self.tank_volume = tank_volume

if __name__ == "__main__":
    # Create electric and gasoline cars
    electric_car = ElectricCar("ABC-15", 180, 52.5)
    gasoline_car = GasolineCar("ACD-123", 165, 32.3)

    # Set speeds for both cars
    electric_car.accelerate(150)
    gasoline_car.accelerate(120)

    # Drive both cars for three hours
    electric_car.drive(3)
    gasoline_car.drive(3)

    # Print out kilometer counters
    electric_car.show_info()
    gasoline_car.show_info()
