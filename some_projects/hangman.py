import random

words = ["facebook", "amazon", "flipkart", "youtube", "linkedin"]

def hangman():
    idx = random.randint(0, len(words)-1)
    guessed = False
    print("Hangman Begins")
    print("\nA word has been selected from the list")

    word = words[idx]
    guessed_letters = []
    for i in range(0, len(word)):
        guessed_letters.append('_')

    while guessed == False:
        letter = input("\n\nGuess a letter: ")
        for i in range(0, len(word)):
            if word[i] == letter:
                guessed_letters[i] = word[i]
        

        
        guessed = True

        for ch in guessed_letters:
            if ch=='_':
                guessed = False

        for ch in guessed_letters:
            print(ch)



hangman()