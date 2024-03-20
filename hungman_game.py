import random

class Hangman:
    def __init__(self):
        self.words = {
            "animals": ["elephant", "tiger", "giraffe", "zebra", "monkey"],
            "countries": ["india", "usa", "canada", "australia", "france"],
            "movies": ["avatar", "titanic", "inception", "joker", "forrest gump"]
        }
        self.hangman_graphics = [
            """
               ____
              |    |
                   |
                   |
                   |
                   |
            _______|""",
            """
               ____
              |    |
              O    |
                   |
                   |
                   |
            _______|""",
            """
               ____
              |    |
              O    |
              |    |
                   |
                   |
            _______|""",
            """
               ____
              |    |
              O    |
             /|    |
                   |
                   |
            _______|""",
            """
               ____
              |    |
              O    |
             /|\\   |
                   |
                   |
            _______|""",
            """
               ____
              |    |
              O    |
             /|\\   |
             /     |
                   |
            _______|""",
            """
               ____
              |    |
              O    |
             /|\\   |
             / \\   |
                   |
            _______|"""
        ]
        self.max_attempts = len(self.hangman_graphics) - 1
        self.category = ""
        self.word = ""
        self.guessed_letters = set()
        self.remaining_attempts = 0
        self.game_over = False

    def select_category(self):
        print("Select a category:")
        for idx, category in enumerate(self.words.keys()):
            print(f"{idx + 1}. {category.capitalize()}")
        choice = input("Enter the number of the category: ")
        if choice.isdigit() and 1 <= int(choice) <= len(self.words):
            self.category = list(self.words.keys())[int(choice) - 1]
            self.word = random.choice(self.words[self.category])
            self.remaining_attempts = self.max_attempts
        else:
            print("Invalid choice. Please enter a number between 1 and", len(self.words))

    def display_word(self):
        displayed_word = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                displayed_word += letter
            else:
                displayed_word += "_"
        return displayed_word

    def guess_letter(self):
        letter = input("Guess a letter: ").lower()
        if letter.isalpha() and len(letter) == 1:
            if letter in self.guessed_letters:
                print("You already guessed that letter!")
            else:
                self.guessed_letters.add(letter)
                if letter not in self.word:
                    self.remaining_attempts -= 1
                if self.remaining_attempts == 0 or set(self.word) == self.guessed_letters:
                    self.game_over = True
        else:
            print("Invalid input. Please enter a single letter.")

    def play(self):
        print("Welcome to Hangman!")
        self.select_category()
        while not self.game_over:
            print(self.hangman_graphics[self.max_attempts - self.remaining_attempts])
            print("Word:", self.display_word())
            print("Remaining Attempts:", self.remaining_attempts)
            self.guess_letter()
        if self.remaining_attempts == 0:
            print("You lost! The word was:", self.word)
        else:
            print("Congratulations! You guessed the word:", self.word)

if __name__ == "__main__":
    game = Hangman()
    game.play()
