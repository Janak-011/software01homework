class Car:
    def __init__(self, make, model, maximum_speed):
        self.make = make
        self.model = model
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_of_speed):
        """
        Adjusts the car's current speed according to change_of_speed,
        without exceeding maximum_speed or dropping below 0.
        """
        new_speed = self.current_speed + change_of_speed

        if new_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed

    def drive(self, hours):
        """
        Increases travelled_distance based on current_speed and hours driven.
        """
        if hours < 0:
            raise ValueError("Hours cannot be negative")
        self.travelled_distance += self.current_speed * hours


# ---- Example Usage ----
car = Car("Toyota", "Corolla", 150)
car.travelled_distance = 2000
car.current_speed = 60

car.drive(1.5)  # Drive for 1.5 hours

print("Travelled distance:", car.travelled_distance, "km")