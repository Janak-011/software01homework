import math


# Function to calculate the unit price (€/m²) of a pizza
def pizza_unit_price(diameter_cm, price_eur):
    radius_m = (diameter_cm / 100) / 2  # convert diameter to meters and get radius
    area_m2 = math.pi * radius_m ** 2  # area of the pizza in square meters
    unit_price = price_eur / area_m2  # euros per square meter
    return unit_price


# Main program
def main():
    print("Enter details for the first pizza:")
    diameter1 = float(input("Diameter (cm): "))
    price1 = float(input("Price (€): "))

    print("\nEnter details for the second pizza:")
    diameter2 = float(input("Diameter (cm): "))
    price2 = float(input("Price (€): "))

    unit_price1 = pizza_unit_price(diameter1, price1)
    unit_price2 = pizza_unit_price(diameter2, price2)

    print(f"\nPizza 1 unit price: {unit_price1:.2f} €/m²")
    print(f"Pizza 2 unit price: {unit_price2:.2f} €/m²")

    if unit_price1 < unit_price2:
        print("\nPizza 1 provides better value for money.")
    elif unit_price2 < unit_price1:
        print("\nPizza 2 provides better value for money.")
    else:
        print("\nBoth pizzas offer the same value for money.")


# Run the main program
main()