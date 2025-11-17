class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor
        print(f"Elevator is initialized at floor {self.current_floor}.")

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator moved up to floor {self.current_floor}.")
        else:
            print("Elevator is already at the top floor.")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator moved down to floor {self.current_floor}.")
        else:
            print("Elevator is already at the bottom floor.")

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print("Target floor is out of range!")
            return
        print(f"Going to floor {target_floor}...")
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()
        print(f"Elevator has arrived at floor {self.current_floor}.")


# --- Main Program ---
if __name__ == "__main__":
    # Create an elevator from floor 0 to 10
    h = Elevator(0, 10)

    # Move to floor 5
    h.go_to_floor(5)

    # Move back to the bottom floor
    h.go_to_floor(0)