class Car:
    def __init__(self, make, model, maximum_speed):
        self.make = make
        self.model = model
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0  # Not used for this task

    def accelerate(self, change_of_speed):
        """
        Adjusts the car's current speed according to change_of_speed,
        without exceeding maximum_speed or dropping below 0.
        """
        new_speed = self.current_speed + change_of_speed

        # Ensure speed stays within valid bounds
        if new_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed


# ---- Main Program ----
my_car = Car("Toyota", "Corolla", 150)

# Accelerate in steps
my_car.accelerate(30)  # +30 km/h
my_car.accelerate(70)  # +70 km/h
my_car.accelerate(50)  # +50 km/h

# Print current speed
print("Current speed:", my_car.current_speed, "km/h")  # Should not exceed 150 km/h

# Emergency brake
my_car.accelerate(-200)  # Attempt to reduce speed by 200 km/h

# Print final speed
print("Final speed after emergency brake:", my_car.current_speed, "km/h")  # Should be 0 km/h