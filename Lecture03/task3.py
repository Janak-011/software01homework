gender = input("Enter your biological gender (female/male): ").lower()


try:
    hemoglobin = float(input("Enter your hemoglobin level (g/L): "))

    if gender == "female":
        if hemoglobin < 117:
            print("Your hemoglobin level is low.")
        elif hemoglobin <= 155:
            print("Your hemoglobin level is normal.")
        else:
            print("Your hemoglobin level is high.")

    elif gender == "male":
        if hemoglobin < 134:
            print("Your hemoglobin level is low.")
        elif hemoglobin <= 167:
            print("Your hemoglobin level is normal.")
        else:
            print("Your hemoglobin level is high.")

    else:
        print("Invalid input for gender.")

except ValueError:
    print("Invalid input for hemoglobin level. Please enter a number.")
