LEGAL_SIZE = 42
length = int(input("Enter the length of the zander in centimeters: "))


if length < LEGAL_SIZE:
    short_by = LEGAL_SIZE - length
    print(f"The zander is too small and must be released back into the lake.")
    print(f"It is {short_by} cm shorter than the legal limit.")
else:
    print("The zander meets the size requirement and can be kept.")