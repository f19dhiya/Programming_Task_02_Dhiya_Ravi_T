print("       EVEN OR ODD ")
try:
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print(f"\n{number} is an Even Number")
    else:
        print(f"\n{number} is an Odd Number")
except ValueError:
    print("⚠  Invalid input. Please enter a whole number.")