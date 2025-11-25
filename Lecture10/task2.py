class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance_travelled = 0

    def set_speed(self, speed):
        # speed cannot exceed the max speed
        self.current_speed = min(speed, self.max_speed)

    def drive(self, hours):
        self.distance_travelled += self.current_speed * hours


class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume


# Main program
electric = ElectricCar("ABC-15", 180, 52.5)
gasoline = GasolineCar("ACD-123", 165, 32.3)

# Set speeds
electric.set_speed(150)
gasoline.set_speed(140)

# Drive both for 3 hours
electric.drive(3)
gasoline.drive(3)

# Print kilometer counters
print(f"Electric car distance: {electric.distance_travelled} km")
print(f"Gasoline car distance: {gasoline.distance_travelled} km")