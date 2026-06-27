questions = [
    ['Biggest mammal on earth alive', 'Elephant', 'Polar bear', 'None', 'Killer Whale', 3],
    ['In logic, what is the next number in the sequence: 2, 6, 12, 20, ?', '30', '28', '24', '26', 2],
    ['Which is not one of the seven wonders of the world?', 'Petra', 'Colosseum', 'Easter Island Statues', 'Machu Picchu', 3],
    ['Which planet is known as the “Red Planet”?', 'Jupiter', 'Venus', 'Mars', 'Mercury', 3],
    ['Who is the current Prime Minister of the United Kingdom? (as of 2025)', 'Keir Starmer', 'Rishi Sunak', 'Boris Johnson', 'Theresa May', 1],
    ['Which country recently became the 31st member of NATO? (as of 2024)', 'Finland', 'Sweden', 'Ukraine', 'Georgia', 2],
    ['What is the currency of Argentina?', 'Peso', 'Real', 'Lira', 'Bolivar', 1],
    ['Which gas is primarily responsible for the greenhouse effect?', 'Oxygen', 'Methane', 'Carbon Dioxide', 'Nitrogen', 3],
    ['Which tech company launched the “Gemini” AI model in competition with OpenAI’s GPT?', 'Meta', 'Amazon', 'Google', 'Apple', 3],
    ['Which country has the most time zones?', 'USA', 'Russia', 'France', 'China', 3],
    ['Which structure in the human brain is primarily responsible for forming new memories?', 'Amygdala', 'Hippocampus', 'Thalamus', 'Cerebellum', 2],
    ['What is the main difference between RNA and DNA?', 'RNA is single-stranded, DNA is double-stranded', 'RNA has thymine, DNA has uracil', 'RNA is found only in the nucleus', 'DNA is not made of nucleotides', 1],
    ['Which philosopher said, “I think, therefore I am”?', 'Socrates', 'Plato', 'Descartes', 'Nietzsche', 3],
    ['Which African country is currently constructing a new capital called “Wakanda City” as a smart-tech hub? (as of 2025)', 'Ghana', 'Nigeria', 'Kenya', 'Rwanda', 1],
    ['What does the term “polycrisis” refer to in global political-economic discussions?', 'Multiple viruses spreading at once', 'The rise of multipolar nuclear threats', 'Simultaneous and interconnected global crises', 'Economic bubbles in multiple countries', 3],
    ['Which island nation is predicted to be the first fully submerged due to rising sea levels?', 'Maldives', 'Marshall Islands', 'Fiji', 'Bahamas', 2],
    ['Which of the following statements about Gödel’s incompleteness theorems is true?', 'They prove that all mathematical truths can be proven', 'They only apply to non-Euclidean geometry', 'They demonstrate that in any sufficiently powerful formal system, there are true statements that cannot be proven within the system', 'They contradict the axioms of arithmetic', 3]
    
]

advance = [
    ['According to evolutionary psychology, why are humans generally more afraid of snakes than flowers?', 'Snakes have more toxins', 'We learn it through media', 'It’s genetically hardwired from survival instincts', 'Snakes are faster', 3],
    ['Which country recently legalized euthanasia, becoming the first in Asia to do so?', 'Japan', 'South Korea', 'India', 'Thailand', 4]
]

levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,7500000,10000000,70000000]
money = 0
for i in range(0,len(questions)):
    question = questions[i]
    print(f"\n\nThe question for ₹{levels[i]} is: ")
    print(question[0])
    print(f"a.{question[1]:20}          b.{question[2]:20}")
    print(f"c.{question[3]:20}          d.{question[4]:20}")
    answer = int(input("Enter your answer(1-4), '0' to quit or '5' to use a lifeline: \n"))
    if answer == question[-1] and i != 16:
        print(f"Correct answer! You have won ₹{levels[i]}")
    elif i == 5:
        money = 10000
    elif i == 10:
        money = 320000
    elif i == 15:
        money = 75000000
    elif i == 16:
        if answer == question[-1]:
            print(f"Congratulations! That's my boy/girl/ni***. You have successfully completed the game.\nThe total amount of ₹{levels[-1]} have been credited to your bank account.")
    elif answer>0 and answer<5 and answer!=0 and answer != question[-1]:
        if i == 0:
            print("I don't have words to rate your intelligence.")
        elif i ==1 or i == 2:
            print("This is what happens when you are mentally impared.")
        else:
            print(f"Wrong answer! \n")
            print(f"Thank you for taging along with us, all this time. ₹{money} have been succesfully credited to your bank account.")
        break
    elif answer == 0:
        if i == 0:
            print("The developer should do something of you idiots. You are exceptionally unqualified.")
        elif i ==1:
            print(f"I bet you are a dumba** when it comes to money. ₹{levels[i-1]} have been succesfully credited to your bank account.")
        else:
            print(f"Thank you for taging along with us, all this time. ₹{levels[i-1]} have been succesfully credited to your bank account.")
        break
    elif answer == 5:
        lifeline_uses = {
            1: 1,  # Ask the expert
            2: 1   # Flip the question
        }
        while True:
            print("-"*15, 'Lifelines', '-'*15)
            print("1. Ask the expert")
            print("2. Flip the question")
            
            try:
                lifeline = int(input("Enter the lifeline you want to use(1,2): \n"))
                
                if lifeline in [1, 2] and lifeline_uses[lifeline] > 0:
                    match lifeline:
                        case 1:
                            print("\nAsk the expert has been activated successfully.")
                            print("The answer is being entered by our AI......")
                            print(f"\nCorrect answer! You have won ₹{levels[i]}")
                            break
                            
                        case 2:
                            print("\nFlip the question has been activated successfully.")
                            print(f"\nThe question for ₹{levels[i]} is: ")
                            print(advance[1][0])
                            print(f"a.{advance[1][1]:20}          b.{advance[1][2]:20}")
                            print(f"c.{advance[1][3]:20}          d.{advance[1][4]:20}")
                            
                            reply = int(input("Enter your answer(1-4), '0' to quit or '5' to use a lifeline: \n"))
                            
                            if reply == advance[1][-1]:
                                print(f"Correct answer! You have won ₹{levels[i]}")
                                break
                            elif reply in [1, 2, 3, 4] and reply != advance[1][-1]:
                                print("Wrong answer!")
                                print(f"Thank you for taging along with us, all this time. ₹{money} have been succesfully credited to your bank account.")
                                break
                            elif reply == 0:
                                if i == 0:
                                    print("Thank you for showing up to the game. You are exceptionally unqualified.")
                                else:
                                    print(f"Thank you for taging along with us, all this time. ₹{levels[i-1]} have been succesfully credited to your bank account.")
                                break
                            else:
                                print("Please enter a valid input.")
                                break
                elif lifeline_uses[lifeline] == 0:
                    print("Come on, don't be such an idiot to think you can use it again.")
                else:
                    print("Enter a valid input.")

            except ValueError:
                print("Please enter a number.")
        # print("1. Ask the expert")
        # print("2. Flip the question")
        # lifeline = int(input("\nEnter the lifeline you want to use: \n"))
        
        # if lifeline<3 and lifeline>0:
        #     match lifeline:
        #         case 1:
        #             print("Ask the expert has been activated successfully.")
        #         case 2:
        #             print("Flip the question has been activated successfully.")
        #             print(f"\n\nThe question for ₹{levels[i]} is: ")
        #             print(advance[1][0])
        #             print(f"a.{advance[1][1]:20}          b.{advance[1][2]:20}")
        #             print(f"c.{advance[1][3]:20}          d.{advance[1][4]:20}")
        #             reply = int(input("Enter your answer(1-4), '0' to quit or '5' to use a lifeline: \n"))
        #             if reply == advance[1][-1]:
        #                 print(f"Correct answer! You have won ₹{levels[i]}")
        #                 break
        #             elif reply>0 and reply<5 and reply!=0 and reply != advance[1][-1]:
        #                 print(f"Wrong answer! \n")
        #                 print(f"Thank you for taging along with us, all this time. ₹{money} have been succesfully credited to your bank account.")
        #                 break
        #             elif reply == 0:
        #                 if i == 0:
        #                     print("Thank you for showing up to the game. You are exceptionally unqualified.")
        #                 else:
        #                     print(f"Thank you for taging along with us, all this time. ₹{levels[i-1]} have been succesfully credited to your bank account.")
        #                 break
        #             else:
        #                 print("Please enter a valid input.")
        #                 break      
        # else:
        #     print("Enter a valid input")


    else:
        print("Please enter a valid input.")
        break




