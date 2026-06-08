Python Task 02 — Decision Making & Logic Building
Internship: Cyber Security Summer Internship
Task: 02 — Conditional Statements & Logical Thinking
Name: Dhiya Ravi T
College: XYZ College | Branch: CSE

Folder Structure
Programming_Task_02_Dhiya_Ravi_T/
├── even_odd.py
├── largest_number.py
├── grade_calculator.py
├── login_validation.py
├── password_checker.py
├── screenshot_even_odd.png
├── screenshot_largest_number.png
├── screenshot_grade_calculator.png
├── screenshot_login_validation.png
├── screenshot_password_checker.png
└── README.md
How to Run
python even_odd.py
python largest_number.py
python grade_calculator.py
python login_validation.py
python password_checker.py
Part A — even_odd.py
What it does
Takes a number from the user and checks whether it is Even or Odd using the modulo operator.

Logic
if number % 2 == 0  →  Even
else                →  Odd
Concepts Used
Concept	How it's used
input()	Reading the number from the user
int()	Converting string input to integer
Modulo %	Remainder of division by 2
if / else	Branching on even or odd result
try / except	Handling non-integer input gracefully
Sample Output
========================================
       EVEN OR ODD CHECKER
========================================
Enter a number: 15

15 is an Odd Number
========================================
Part B — largest_number.py
What it does
Accepts three numbers from the user and finds the largest using chained if / elif / else comparisons.

Logic
if a >= b and a >= c   →  largest = a
elif b >= a and b >= c →  largest = b
else                   →  largest = c
Concepts Used
Concept	How it's used
float()	Supports both integers and decimals
if / elif / else	Multi-branch comparison
Logical and	Both conditions must be true
Comparison >=	Checking which value is greater
Sample Output
========================================
     LARGEST OF THREE NUMBERS
========================================
Enter First Number  : 10
Enter Second Number : 25
Enter Third Number  : 18

Largest Number = 25
========================================
Part C — grade_calculator.py
What it does
Takes a marks value (0–100) and maps it to a letter grade with a remark using an elif ladder.

Grading Criteria
Marks	Grade	Remark
90–100	A	Excellent!
80–89	B	Very Good!
70–79	C	Good
60–69	D	Needs Improvement
Below 60	F	Failed
Concepts Used
Concept	How it's used
elif ladder	Maps mark ranges to grades
Range validation	Rejects marks outside 0–100
Comparison operators	>= checks for each range boundary
try / except	Catches non-numeric input
Sample Output
========================================
     STUDENT GRADE CALCULATOR
========================================
Enter your marks (0 - 100): 85

Marks  : 90
Grade  : A
Remark : Excellent!
========================================
Part D — login_validation.py
What it does
Stores a hardcoded username and password, takes input from the user, and validates the credentials using string comparison.

Logic
if username == "admin" and password == "password123"
    → Login Successful
else
    → Invalid Credentials
Concepts Used
Concept	How it's used
String variables	Storing predefined credentials
== string comparison	Checking if input matches stored value
Logical and	Both username AND password must match
if / else	Showing success or failure message
Cyber Security Note: Real systems never store plain-text passwords. They use hashing algorithms like bcrypt or SHA-256 to protect credentials.

Sample Output
========================================
          LOGIN PORTAL
========================================
Username : Dhiya
Password : 0307
----------------------------------------
✔  Login Successful!
   Welcome, admin!
========================================
Part E — password_checker.py
What it does
Analyses a password against 5 security checks and rates it as Weak, Moderate, or Strong. This mirrors real-world password policy enforcement used in security tools and web apps.

Strength Criteria
Check	Requirement
Length	At least 8 characters
Number	Contains at least one digit (0–9)
Uppercase	Contains at least one A–Z letter
Lowercase	Contains at least one a–z letter
Special char	Contains !@#$%^&* etc.
Scoring
Score (out of 5)	Strength
0 – 2	Weak Password
3	Moderate Password
4 – 5	Strong Password
Concepts Used
Concept	How it's used
len()	Checking password length
any() + generator	Scanning all characters efficiently
str.isdigit()	Checking for numeric characters
str.isupper() / islower()	Checking letter case
in operator	Checking for special characters
Accumulator variable score	Counting how many checks passed
Sample Output
=============================================
       PASSWORD STRENGTH CHECKER
=============================================
Enter Password: Cyber123

── Checks ──────────────────────────────
  Length ≥ 8 chars     : ✔
  Contains number      : ✔
  Contains uppercase   : ✔
  Contains lowercase   : ✔
  Contains special char: ✘
─────────────────────────────────────────

Result: Strong Password
=============================================
Concepts Summary
Concept	Parts
if / elif / else	A, B, C, D, E
Comparison operators == != > < >= <=	All
Logical operators and / or	B, D, E
try / except error handling	A, C
String methods (isdigit, isupper, etc.)	E
any() with generator expressions	E
Modulo operator %	A
Cyber Security Connections
Part D → Authentication & login systems, session security
Part E → Password policy enforcement, security hardening
Strong Python skills in conditionals and string handling are essential for writing security scripts, log analysers, and penetration testing tools.
