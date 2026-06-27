import random
# def game(x,y):
#     global score
#     score = 0
#     if x==y:
#         print("Its's a draw")
#         return score
#     elif (x==1 and y==2) or (x==2 and y==3) or (x==3 and y==1):
#         print("You won")
#         score +=1
#         return score
#     else:
#         print("You lose")
#         score-=1
#         return score
    
score = 0  
while True:
    print("Enter 's' to start the game or 'e' to end it:")
    star = input()
    if star == 's':
        print('-'*15 + 'MENU' + '-'*15)
        print("1 -- Snake")
        print("2 -- Water")
        print("3 -- Gun")
        user_input = int(input("Enter your choice(1-3): \n"))
        choices = [1,2,3]
        computer_choice = random.choice(choices)
        print("Your choice    : ", user_input)
        print('Computer choice: ', computer_choice)
        # print("Your score: ",game(user_input,computer_choice))


        if user_input==computer_choice:
            print("Its's a draw")
            print(f"Your current score is {score}\n")
        elif (user_input==1 and computer_choice==2) or (user_input==2 and computer_choice==3) or (user_input==3 and computer_choice==1):
            print("You won")
            score +=1
            print(f"Your current score is {score}\n")
        else:
            print("You lose")
            score-=1
            print(f"Your current score is {score}\n")


    elif star == 'e':
        if score>0:
            print("\nYou nailed the rally")
            print("Your final score: ",score)
        elif score<0:
            print("\nYou lost! Good luck next time")
            print("Your final score: ",score)
        else:
            print("\nIt's a draw")
            print("Your final score: ",score)
        print("Thanks for playing with us")
        break
    else:
        raise ValueError("Invalid input! \nPlease enter a correct input")







