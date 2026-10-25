#Q1
correct_pin =1234
balance = 10000
attempt = 3
history = []
while attempt>0:
    user_pin = int(input("entre your pin"))
    if user_pin == correct_pin:
        print("login sucesssful")
        break
    else:
        if attempt>0:
            print("you entre the wrong pin",attempt)
            attempt-=1
        else:
            print("invaild attempt")
        print("Card blocked")
if attempt>0:
    while True:
        print("------atm menu-----")
        print("1.BALANCE")
        print("2.DEPOSIT")
        print("3.WITHDRAW")
        print("4.EXIT")
        CHOICE = input("entre your choice")
        if CHOICE == "1":
            print("your cureent balance is :",balance)
        elif CHOICE == "2":
            deposit_amount = float(input("entre your deposit amount:"))
            balance +=deposit_amount
            history.append(f"you deposit amount:{deposit_amount}")
            print("your current balance:",balance)
        elif CHOICE == "3":
            withdraw_amount = float(input("entre your withdraw amount:"))
            balance -=deposit_amount
            history.append(f"you withdraw amount: {withdraw_amount}")
            print("your current balance:",balance)
        elif CHOICE == 4:
            print("Thank you")
            break
        else:
            print("invalid attempt")
print(history)
        
#Q2
students = {"Aman": [85, 90, 78], "Riya": [92, 88, 95], "Zoya": [70, 65, 80]}

while True:
    print("\n1. Add student")
    print("2. View all")
    print("3. Show topper")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        if name in students:
            print("Student already exists.")
        else:
            marks = []
            while len(marks) < 3:
                mark = float(input("Enter mark: "))
                if mark >= 0 and mark <= 100:
                    marks.append(mark)
                else:
                    print("Invalid mark, try again.")
            students[name] = marks

    elif choice == "2":
        for name, marks in students.items():
            average = sum(marks) / len(marks)
            if average >= 85:
                print(name, round(average, 2), "A")
            elif average >= 70:
                print(name, round(average, 2), "B")
            elif average >= 50:
                print(name, round(average, 2), "C")
            else:
                print(name, round(average, 2), "F")

    elif choice == "3":
        highest = 0
        topper_name = ""
        for name, marks in students.items():
            average = sum(marks) / len(marks)
            if average > highest:
                highest = average
                topper_name = name
        print("Topper:", topper_name)

    elif choice == "4":
        print("Goodbye!")
        break
