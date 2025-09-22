while True:
    inches = float(input("Enter length in inches (negative to stop): "))

    if inches < 0:
        print("Program stopped.")
        break

    centimeters = inches * 2.54
    print(f"{inches} inches = {centimeters:.2f} cm")