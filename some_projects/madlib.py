# print(f"Computer programming is so {input()}! \nAnd I wanna be a {input()}")


# guess number
import random

limit = int(input("Enter the number limit: "))
num = random.randint(0,limit)
ans = 0
for i in range(3):
    res = int(input("Enter your guess:"))
    if (res == num):
        print("yes")
        ans = 1
        break
    else:
        print("no")

print("not able to guess the number") if (ans==0) else print("able")
print(num)

