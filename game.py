print("Welcome to Hangman")

# Part 1
# We need computer to pick random word
import random

# We need computer to pick from a List of words
words = ["mascara", "powder", "necklace", "bangles", "bracelets"]

# store the randomly selected word in a variable for reference
secret_word = random.choice(words)

#print(secret_word)

# Part 2
# We need to display the secret word without letters for people to guess
display = []
guessed_letter =[]

# for each letter in our secret word append an _ in our display
for letter in secret_word:
    display.append("_")

# print(secret_word)
# print(display)

# We need to create a way for people to guess
# while the game is not complete and game is not complete, we get to prompted for a new guess

game_over = False
lives = 4
while not game_over:

    guess= input("Guess a letter:").lower().strip()
    if(len(guess)) != 1:
        print("Please enetr only one character")
        continue

    if guess in guessed_letter:
        print("Duh, you already choose this one! Try again")
        continue

    guessed_letter.append(guess)
    print("You tried:", guessed_letter)

    if guess not in secret_word:
        lives -= 1
        print("Wrong guess! try again")
        print("lives left:", lives)

        if lives ==0:
            game_over = True
            print("You lose!")
            print("The secret word was:", secret_word)
            break

# We need to create a way to check if letter player used in secret word
# for each position in our secret word, if the letter the player picks is in that secret word then 
# find the position in our display and replace it
    for position in range(len(secret_word)):
        secret_word_letter = secret_word[position]

        if secret_word_letter == guess:
            display[position] = guess

    print(display)

    if "_" not in display:
        game_over = True
        print("you smart cookie - YOU WIN! and yes the secret word is:", secret_word)




