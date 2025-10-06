airports = {}

while True:
    print("\nChoose an option:")
    print("1 - Enter a new airport")
    print("2 - Fetch existing airport")
    print("3 - Quit")

    choice = input("Your choice: ")

    if choice == "1":
        icao = input("Enter the ICAO code: ").upper()
        name = input("Enter the airport name: ")
        airports[icao] = name
        print("Airport saved!")

    elif choice == "2":
        icao = input("Enter the ICAO code: ").upper()
        if icao in airports:
            print(airports[icao])
        else:
            print("Airport not found.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")