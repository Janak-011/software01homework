cities = []


for i in range(5):
    city = input("Enter the name of city #" + str(i + 1) + ": ")
    cities.append(city)


print("\nThe cities you entered are:")
for city in cities:
    print(city)