print("PASSWORD STRENGTH CHECKER")
password = input("Enter Password: ")

has_length   = len(password) >= 8
has_number   = any(ch.isdigit()   for ch in password)
has_upper    = any(ch.isupper()   for ch in password)
has_lower    = any(ch.islower()   for ch in password)
has_special  = any(ch in "!@#$%^&*()_+-=[]{}|;':\",./<>?" for ch in password)

score = sum([has_length, has_number, has_upper, has_lower, has_special])

print("\n── Checks ──────────────────────────────")
print(f"  Length ≥ 8 chars     : {'✔' if has_length  else '✘'}")
print(f"  Contains number      : {'✔' if has_number  else '✘'}")
print(f"  Contains uppercase   : {'✔' if has_upper   else '✘'}")
print(f"  Contains lowercase   : {'✔' if has_lower   else '✘'}")
print(f"  Contains special char: {'✔' if has_special else '✘'}")
print("─" * 45)

if score <= 2:
    strength = "Weak Password"
elif score <= 3:
    strength = "Moderate Password"
else:
    strength = "Strong Password"

print(f"\nResult: {strength}")