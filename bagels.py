import random


class Game:
    def __init__(self):
        self.menu_running = True
        self.running = True
        self.number = ['5', '5', '5']
        self.words = ['', '', '']
        self.attempts = 0
        self.menu()

    def gen_number(self):
        self.number[0] = str(random.randint(1, 9))
        for i in range(1, 3):
            self.number[i] = str(random.randint(0, 9))

    def get_input(self):
        while True:
            print()
            self.player_input = input("Enter number\n")
            if self.check_input(self.player_input):
                return self.player_input
            else:
                print("Try again!")

    def check_input(self, line):
        if line.isdigit() and len(line) == 3:
            return True
        else:
            return False

    def check(self):
        if self.words == ['Fermi', 'Fermi', 'Fermi']:
            print()
            print("You win!")
            self.running = False
            self.menu()
        elif self.attempts == 15:
            print()
            print("You lose!")
            self.running = False
            self.menu()
        self.words = ['', '', '']

    def output(self):
        for i in range(0, 3):
            for j in range(0, 3):
                if self.player_input[i] != self.number[j]:
                    self.words.pop(i)
                    self.words.insert(i, 'Bagels')

        for i in range(0, 3):
            for j in range(0, 3):
                if self.player_input[i] == self.number[j] and i != j:
                    self.words.pop(i)
                    self.words.insert(i, 'Pico')

        for i in range(0, 3):
            for j in range(0, 3):
                if self.player_input[i] == self.number[j] and i == j:
                    self.words.pop(i)
                    self.words.insert(i, 'Fermi')

        if self.words == ['Bagels', 'Bagels', 'Bagels']:
            print("Bagels")
        else:
            print()
            random.shuffle(self.words)
            for i in range(0, 3):
                if self.words[i] != 'Bagels':
                    print(self.words[i], end=" ")

        self.attempts += 1

    def run(self):
        self.gen_number()
        while self.running:
            # print(self.number)
            self.player_input = self.get_input()
            self.output()
            self.check()

    def menu(self):
        while self.menu_running:
            print()
            print("Hi, this is 'Bagels.'")
            print("In this game you need to guess a three-digit numer.")
            print("Here is the rules:")
            print("You have 15 attempts.")
            print("After each guess, the computer gives you \nthree types of clues: ")
            print("Bagels - none of the three digits guessed is in the secret number.")
            print("Pico - one of the digits is in the secret number, but the guess has the digit in the wrong place.")
            print("Fermi - the guess has a correct digit in the correct place.")
            print()
            player_input = input(
                'Enter "1" to start the game or "0" to exit\n')
            if player_input == '1':
                self.running = True
                self.run()
            else:
                self.menu_running = False


if __name__ == '__main__':
    Game()
