
num_guesses = 7
word = "education"
word_lst = ['e', 'd', 'u', 'c', 'a', 't', 'i', 'o', 'n']
guessed_letters = ['e']
current_progress = []
have_won = False

class Game:
    pass

def progress():
    current_progress.clear()
    for letter in word_lst:
        if letter in guessed_letters:
            current_progress.append(letter)
        else:
            current_progress.append("_")
    print(" ".join(current_progress))

def is_game_over():
    if word_lst.sort() == current_progress.sort():
        have_won = True

while(num_guesses > 0 and haveWon == False):
    round_guess = input("What is your guess: ")
    print('round guess', round_guess)
    if round_guess in guessed_letters:
        print("You have already guessed that letter")
        progress()
    elif round_guess not in guessed_letters and round_guess in word_lst:
        guessed_letters.append(round_guess)
        progress()
    elif round_guess not in guessed_letters and round_guess not in word_lst:
        print("That letter is incorrect")
        num_guesses -= 1
        progress()


if num_guesses == 0:
    print("YOU RAN OUT OF GUESSES")
elif is_game_over == True:
    print("YOU HAVE WON THE GAME")
