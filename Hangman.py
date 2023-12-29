import random

print("Welcome to Hangman")
print("----------------------------------")

wordDictionary = ["sunflower", "house", "diamond", "memes", "yeet", "hello",
                  "howdy", "like", "subscribe"]

randomWord = random.choice(wordDictionary)

for x in randomWord:
    print("_", end=" ")

def print_hangman(wrong):
    if(wrong == 0):
        print("\n+---+")
        print("     |")
        print("     |")
        print("     |")
        print("    ===")
    elif(wrong == 1):
        print("\n+---+")
        print("O    |")
        print("     |")
        print("     |")
        print("    ===")
    elif(wrong == 2):
        print("\n+---+")
        print("O    |")
        print("|    |")
        print("     |")
        print("    ===")
    elif(wrong == 3):
        print("\n+---+")
        print(" O   |")
        print("/|   |")
        print("     |")
        print("    ===")
    elif(wrong == 4):
        print("\n+---+")
        print(" O   |")
        print("/|\  |")
        print("     |")
        print("    ===")
    elif(wrong == 5):
        print("\n+---+")
        print(" O   |")
        print("/|\  |")
        print("/    |")
        print("    ===")
    elif(wrong == 6):
        print("\n+---+")
        print(" O   |")
        print("/|\  |")
        print("/ \  |")
        print("    ===")

def printWord(guessedLetters):
    counter=0
    rightLetters=0
    for char in randomWord:
        if(char in guessedLetters):
            print(randomWord[counter], end=" ")
        else:
            print(" ", end=" ")
            counter+=1
            return rightLetters

def printLines():
    print("\r")
    for char in randomWord:
        print("\u203E", end=" ")

lenght_of_word_to_guess = len(randomWord)
amount_of_times_wrong = 0
current_guess_index = 0
current_letters_guessed = []
current_letters_right = 0

# ... (previous code)

while amount_of_times_wrong != 6 and current_letters_right != lenght_of_word_to_guess:
    print("\nLetters guessed so far: ")
    for letter in current_letters_guessed:
        print(letter, end=" ")
    letterGuessed = input("\nGuess a Letter: ")
    if randomWord[current_guess_index] == letterGuessed:
        print_hangman(amount_of_times_wrong)
        current_guess_index += 1
        current_letters_guessed.append(letterGuessed)
        current_letters_right = printWord(current_letters_guessed)
        printLines()
    else:
        amount_of_times_wrong += 1
        current_letters_guessed.append(letterGuessed)
        print_hangman(amount_of_times_wrong)
        current_letters_right = printWord(current_letters_guessed)
        printLines()

print("Game is over. Thank you for playing")
