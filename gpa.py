# Ryan Pendergraff
# gpa_qualification_dean_honor.py
#This app accepts student names and GPAs and checks if the student qualifies for the Dean's List or the Honor Roll. If ZZZ is entered it will stop.
while True:
    last_name = input("Enter the student's last name (or 'ZZZ' to quit): ")
    if last_name == 'ZZZ':
        break
    first_name = input("Enter the student's first name: ")
    try:
        gpa = float(input("Enter the student's GPA: "))
    except ValueError:
        print("Invalid GPA entered. Please enter a valid number.")
        continue
    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List.")
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll.")
    else:
        print(f"{first_name} {last_name} does not qualify for the Dean's List or Honor Roll.")