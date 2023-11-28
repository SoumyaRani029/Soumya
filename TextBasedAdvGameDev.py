class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100

class Game:
    def __init__(self):
        self.player = None

    def start(self):
        print("Welcome to the Adventure Game!")
        player_name = input("Enter your name: ")
        self.player = Player(player_name)
        self.intro()

    def intro(self):
        print(f"Hello, {self.player.name}! You find yourself in a mysterious land.")

        #Player choose to either left or right
        choice = input("Do you want to go left or right? ").lower()

        if choice == "left":
            self.left_path()
        elif choice == "right":
            self.right_path()
        else:
            print("Invalid choice. Try again.")
            self.intro()

    def left_path(self):
        print("You encounter a friendly merchant. He offers you a health potion.")
        choice = input("Do you accept the potion? (yes/no) ").lower()

        if choice == "yes":
            print("You feel stronger with the health potion.")
            self.player.health += 20
        elif choice == "no":
            print("You thank the merchant and continue on your journey.")
        else:
            print("Invalid choice. Try again.")
            self.left_path()

        self.end_game()

    def right_path(self):
        print("You stumble upon a dark cave.")
        choice = input("Do you enter the cave? (yes/no) ").lower()

        if choice == "yes":
            print("Inside the cave, you find a treasure chest.")
            print("Congratulations! You have completed the adventure and found treasure!")
        elif choice == "no":
            print("You decide not to enter the cave and continue exploring.")
        else:
            print("Invalid choice. Try again.")
            self.right_path()

        self.end_game()

    # Display final information about the player's health
    def end_game(self):
        print(f"Game Over. {self.player.name}, your final health is {self.player.health}.")

if __name__ == "__main__":
    game = Game()
    game.start()
