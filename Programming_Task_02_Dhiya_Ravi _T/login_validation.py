STORED_USERNAME = "Dhiya"
STORED_PASSWORD = "0307"

print("=" * 40)
print("          LOGIN PORTAL")
print("=" * 40)

username = input("Username : ")
password = input("Password : ")

print("-" * 40)

if username == STORED_USERNAME and password == STORED_PASSWORD:
    print("✔  Login Successful!")
    print(f"   Welcome, {username}!")
else:
    print("✘  Invalid Credentials")
    print("   Please check your username and password.")