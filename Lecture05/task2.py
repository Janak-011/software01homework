numbers = []

while True:
    user_input = input("Enter a number (or press Enter to quit): ")

    if user_input == "":
        break

    number = int(user_input)
    numbers.append(number)

numbers.sort(reverse=True)

top_five = numbers[:5]

print("The five greatest numbers are:", top_five)