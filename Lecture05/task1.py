
import random


num_dice = int(input("How many dice do you want to roll? "))

total = 0

# Roll each die
for i in range(num_dice):
    roll = random.randint(1, 6)
    total += roll

# Print the result
print("The total sum of the dice is:", total)

