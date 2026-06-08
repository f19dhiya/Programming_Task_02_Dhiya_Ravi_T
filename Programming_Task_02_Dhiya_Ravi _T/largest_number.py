print("     LARGEST OF THREE NUMBERS")

try:
    a = float(input("Enter First Number  : "))
    b = float(input("Enter Second Number : "))
    c = float(input("Enter Third Number  : "))

    if a >= b and a >= c:
        largest = a
    elif b >= a and b >= c:
        largest = b
    else:
        largest = c
    fmt = lambda n: int(n) if n == int(n) else n
    print(f"\nLargest Number = {fmt(largest)}")

except ValueError:
    print("⚠  Invalid input. Please enter numeric values only.")