
num = int(input("Enter an integer: "))

is_prime = True

# Numbers less than 2 are not prime
if num < 2:
    is_prime = False
else:
    # Check for divisors from 2 up to num-1
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")