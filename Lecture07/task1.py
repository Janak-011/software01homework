import random


def roll_dice():
    return random.randint(1, 6)

# Main program
def main():
    roll = 0
    while roll != 6:
        roll = roll_dice()
        print("You rolled:", roll)

# Run the main program
main()