student = []

while True:
    stu1 = []
    num = input("Enter 'C' to start or 'Q' to quit\n")
    if num == "C":
        print("Enter the student details: ")
        name = input("Name: ")
        roll_no = int(input("Roll no: "))
        prn = int(input('PRN: '))
        mob = int(input('Mob: '))
        stu1.append(name)
        stu1.append(roll_no)
        stu1.append(prn)
        stu1.append(mob)
        student.append(stu1)
    else:
        print("Thanks")
        break

while True:
    enter = input("What you want to search?('Q' to quit)\n")
    if enter == 'name':
        Name = input("Enter the name: ")
        for i in student:
            if i[0] == Name:
                print(f"Name: {i[0]}")
                print(f"Roll no: {i[1]}")
                print(f"PRN: {i[2]}")
                print(f"Mobile: {i[3]}")
                break

    elif enter == 'roll':
        Roll = int(input("Enter the roll: "))
        for i in student:
            if i[1] == Roll:
                print(f"Name: {i[0]}")
                print(f"Roll no: {i[1]}")
                print(f"PRN: {i[2]}")
                print(f"Mobile: {i[3]}")
                break

    elif enter == 'prn':
        PRN = int(input("Enter the PRN: "))
        for i in student:
            if i[2] == PRN:
                print(f"Name: {i[0]}")
                print(f"Roll no: {i[1]}")
                print(f"PRN: {i[2]}")
                print(f"Mobile: {i[3]}")
                break

    elif enter == 'mob':
        Mob = int(input("Enter the Mobile: "))
        for i in student:
            if i[3] == Mob:
                print(f"Name: {i[0]}")
                print(f"Roll no: {i[1]}")
                print(f"PRN: {i[2]}")
                print(f"Mobile: {i[3]}")
                break

    elif enter == 'Q':
        print("Thanks")
        break
    else:
        raise ValueError("Invalid Input!!!")

