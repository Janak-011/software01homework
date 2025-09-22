numbers = []

while True:
    user_input = input("Enter a number (or press Enter to stop): ")

    if user_input == "":
        break

    number = float(user_input)
    numbers.append(number)


if len(numbers) > 0:
    smallest = min(numbers)
    largest = max(numbers)
    print("Smallest number:", smallest)
    print("Largest number:", largest)
else:
    print("No numbers were entered.")
