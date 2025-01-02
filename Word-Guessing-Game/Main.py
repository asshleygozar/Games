import random

class Main:

    def __init__(self):

        self.words = ['androids','solar','tree','calculator','python']
        self.word = random.choice(self.words)
        self.guessed = ''
        self.turns = len(self.word)

    def user_input(self):

        name = input("Enter your name: ")

        print(f"Good luck! {name}")
        print("Guess the characters")

        while self.turns > 0:
            
            for char in self.word:

                if char in self.guessed:
                    print(char, end="\n")
                
                else:
                    print("_")
                    
            if self.guessed == self.word:

                print("You win!")
                print(f"The word is: {self.word}")
                break

            guess = input("guess a character: ")

            if guess not in self.word:

                self.turns -= 1
                print("Wrong!")
                print(f"Remaining guesses: {self.turns}")

            else:
                self.guessed += guess
                self.turns -=1

main = Main()
main.user_input()