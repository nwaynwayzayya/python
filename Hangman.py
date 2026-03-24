import random

# create a greeting
print("Welcome to Hangman!")

# create your word list
# words = ["pyramid", "of", "pain", "ttps", "tools", "network", "host artifacts", "domain names", "ip addresses", "hash values"]
words = ["cat", "eat", "chair", "hair"]

# randomly choose a word from the list you have created
random_word = random.choice(words)

# create an empty list
empty_list = []
# for each letter in the secret_word, add a "_" that will be printed to the console
# Example if the word is Hacker "_","_","_","_","_","_"
for letter in random_word:
    empty_list += "_"

print("The random word is " + random_word)    # will show the random word here first for testing purposes
print(f"\nThe random word is: {empty_list}")

# ask the user to guess a letter


# bonus: make the program take the input from the user and make it lowercase

# loop through each of the letters in the chosen word 
# if the letter is in the word, replace the "_" with the letter
# it should look like this "_", "a", "c", "_", "_", "r"

# use a while loop so the game keeps going until the word has been guessed

# create a variable as an int starting at 0 and when it gets to the number 5, the game ends
# add a print statement to tell the user they get 5 guesses
num = 0

print("This is your guess below.\n")

game_over = False

while not game_over:
    guess = input("\n\nGuess a letter: ").lower()
    for position in range(len(random_word)):
        letter = random_word[position]
        if letter == guess:
            empty_list[position] = letter
        else:
            continue

    if guess not in random_word:
        num += 1
        guesses_left = 5 - num
        print(f"You have {guesses_left} guesses left.")
        if num >= 5:
            print("You loser!")
            game_over = True

    print(empty_list)

    if "_" not in empty_list:
        print("You win.")
        game_over = True

