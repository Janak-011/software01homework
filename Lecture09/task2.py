class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator moved up to floor {self.current_floor}.")
        else:
            print("Already at the top floor.")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator moved down to floor {self.current_floor}.")
        else:
            print("Already at the bottom floor.")

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print("Target floor is out of range!")
            return

        print(f"Elevator heading to floor {target_floor}...")
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()
        print(f"Arrived at floor {self.current_floor}.\n")


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []

        # Create the requested number of elevators
        for i in range(num_elevators):
            self.elevators.append(Elevator(bottom_floor, top_floor))

    def run_elevator(self, elevator_number, destination_floor):
        if elevator_number < 1 or elevator_number > len(self.elevators):
            print("Invalid elevator number!")
            return

        print(f"\nRunning elevator {elevator_number}...")
        elevator = self.elevators[elevator_number - 1]
        elevator.go_to_floor(destination_floor)


# -------- Main Program --------
if __name__ == "__main__":
    # Create a building from floors 0 to 10 with 3 elevators
    b = Building(0, 10, 3)

    # Run elevator 1 to floor 7
    b.run_elevator(1, 7)

    # Run elevator 2 to floor 3
    b.run_elevator(2, 3)

    # Move elevator 1 back to bottom floor
    b.run_elevator(1, 0)