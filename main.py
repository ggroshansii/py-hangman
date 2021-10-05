


class Game:
    def __init__(self, word):
        self.num_guesses = 7
        self.word = word
        self.word_lst = []
        self.guessed_letters = []
        self.current_progress = []
        self.have_won = False

    def split_word(self):
        self.word_lst = list(self.word)

    def progress(self):
        self.current_progress.clear()
        for letter in self.word_lst:
            if letter in self.guessed_letters:
                self.current_progress.append(letter)
            else:
                self.current_progress.append("_")
        print(" ".join(self.current_progress))

    def is_game_over(self):
        if self.num_guesses == 0:
            print("YOU RAN OUT OF GUESSES")
        elif sorted(self.word_lst) == sorted(self.current_progress):
            print("You have won!!!! Congratulations")
            self.have_won = True

    def play(self):
        self.split_word()
        while(self.num_guesses > 0 and self.have_won == False):
            round_guess = input("What is your guess: ")
            print('round guess', round_guess)
            if round_guess in self.guessed_letters:
                print("You have already guessed that letter")
                self.progress()
                self.is_game_over()
            elif round_guess not in self.guessed_letters and round_guess in self.word_lst:
                self.guessed_letters.append(round_guess)
                self.progress()
                self.is_game_over()
            elif round_guess not in self.guessed_letters and round_guess not in self.word_lst:
                print("That letter is incorrect")
                self.num_guesses -= 1
                self.progress()
                self.is_game_over()


game = Game("code")
game.play()




# elif is_game_over == True:
#     print("YOU HAVE WON THE GAME")
