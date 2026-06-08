print("     STUDENT GRADE CALCULATOR")
try:
    marks = float(input("Enter your marks (0 - 100): "))

    if marks < 0 or marks > 100:
        print("⚠  Marks must be between 0 and 100.")
    elif marks >= 90:
        grade = "A"
        remark = "Excellent!"
    elif marks >= 80:
        grade = "B"
        remark = "Very Good!"
    elif marks >= 70:
        grade = "C"
        remark = "Good"
    elif marks >= 60:
        grade = "D"
        remark = "Needs Improvement"
    else:
        grade = "F"
        remark = "Failed"

    if 0 <= marks <= 100:
        print(f"\nMarks  : {marks}")
        print(f"Grade  : {grade}")
        print(f"Remark : {remark}")

except ValueError:
    print(" Invalid input. Please enter a numeric value.")