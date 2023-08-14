import player_vs_computer
from player import Player
import functions
import player_vs_player

def display_logo() -> None:
    print("___________.____________   ________________  _________   ___________________  ___________")
    print("\__    ___/|   \_   ___ \  \__    ___/  _  \ \_   ___ \  \__    ___/\_____  \ \_   _____/")
    print("  |    |   |   /    \  \/    |    | /  /_\  \/    \  \/    |    |    /   |   \ |    __)_")
    print("  |    |   |   \     \____   |    |/    |    \     \____   |    |   /    |    \|        \\")
    print("  |____|   |___|\______  /   |____|\____|__  /\______  /   |____|   \_______  /_______  /")
    print("                       \/                  \/        \/                     \/        \/ ")

def display_menu() -> None:
    print("========= Menu ======== ")
    print("  1. Play (player vs ai)")
    print("  2. Play (player vs player)")
    print("  3. Game rules")
    print("  4. Show our Hall of Frame")
    print("  5. Quit")

def get_choice() -> int:
    while True:
        try:
            choice : int = int(input("Enter your choice (1-5) : "))
            if 0 < choice < 6:
                return choice
            else:
                print("Please enter a valid option (1-5)!")
        except ValueError:
            print("Please enter a valid option (1-5)!")

def main() -> None:
    functions.clearscreen()
    display_logo()
    while True:
        display_menu()
        choice = get_choice()

        if choice == 1:
            player_vs_computer.game()
        elif choice == 2:
            player_vs_player.game()
        elif choice == 3:
            functions.show_rules()
        elif choice == 4:
            functions.readHallOfFame()
        elif choice == 5:
            print("\t\t\t\t     Goodbye!")
            break
    display_logo()
    

if __name__ == "__main__":
    main()
