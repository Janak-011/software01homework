
def remove_odds(numbers):
    even_numbers = []
    for n in numbers:
        if n % 2 == 0:
            even_numbers.append(n)
    return even_numbers

# Main program
def main():
    # Example list of integers
    nums = [3, 8, 5, 12, 7, 10, 1, 6]
    evens = remove_odds(nums)
    print("Original list:", nums)
    print("Even numbers only:", evens)


main()