#assign some secret word that the user must guess
# example: ["_", "_", "_"]

# have some variable which tells us if the game keeps going and to continue the while loop

# ask user to guess a letter
# if user's guess is in the word, fill in the list according to where the letter is in the word

# if user's guess is NOT in the word, ask again. Do not update the list.
all_guesses = []
guesses = ['_']
tries = 8
fails = 0
the_word = list("secret")
print(the_word) 
guesses = guesses * len(the_word)
print(guesses)

while fails < tries:
    guess = input("guess a letter: ")
    all_guesses.append(guess)
    if (guess in the_word):
        print("Correct! That letter was in the word.")
        for i in range(0, len(the_word)):
            if guess == the_word[i]:
                guesses[i] = guess
        print(guesses)
    else:
        print("That was not in the word!")
        print(all_guesses)
