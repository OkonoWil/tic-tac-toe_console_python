import os
import csv
from typing import List
from player import Player

# Enregistre 2 joueur
def player_creator(player_one:Player, player_two:Player) -> None:
    tokens: List[str] = ["X", "O"]

    name_one: str = input("Player 1, what is your name?: ")
    while True:
        token_one: str = input("Player 1, Choose a token (Either X or O)\nEnter here: ")
        if token_one.upper() in tokens:
            tokens.remove(token_one.upper())
            break
        print("Please choose either X or O\n")
    name_two: str = input("Player 2, what is your name?: ")
    token_two: str = tokens[0]
    print(f"Player 2 token: {token_two}")

    player_one.name = name_one
    player_one.num = 1
    player_one.token = token_one

    player_two.name = name_two
    player_two.num = 2
    player_two.token = token_two
    clearscreen()
    player_one.print_welcome_statement()
    player_two.print_welcome_statement()
    input("Press enter to continue: ")

# Enregistre 1 joueur
def player_ai_creator(player_one:Player, player_two:Player) -> None:
    tokens: List[str] = ["X", "O"]

    name_one: str = input("Player 1, what is your name?: ")
    while True:
        token_one: str = input("Player 1, Choose a token (Either X or O)\nEnter here: ")
        if token_one.upper() in tokens:
            tokens.remove(token_one.upper())
            break
        print("Please choose either X or O\n")
    #Player 2 est Computer
    name_two: str = "Computer"
    token_two: str = tokens[0]
    print(f"Computer token: {token_two}")

    player_one.name = name_one
    player_one.num = 1
    player_one.token = token_one

    player_two.name = name_two
    player_two.num = 2
    player_two.token = token_two
    clearscreen()
    player_one.print_welcome_statement()
    player_two.print_welcome_statement()
    input("Press enter to continue: ")

# Afficher tic tac toe Les régles tic tac toe
def show_rules():
    clearscreen()
    print(" ______________________________________________________________________________________ ")
    print("|                           The Rules of the game                                      |")                                    
    print("|--------------------------------------------------------------------------------------|")
    print("|Two players compete in a turn-based game on a 3x3 board (3 rows and 3 columns).       |")
    print("|Player 1 will have the symbol 'X' while Player 2 will have the symbol 'O'             |")
    print("|Players must place their symbols on an empty cell of the board by entering the corres-|")
    print("|   ponding coordinates for the cell (Example: 9)                                      |")
    print("|Players take turns placing a symbol in each round. The goal of the game is to align   |")
    print("|   three identical symbols horizontally, vertically,                                  |")
    print("|If neither player is able to align 3 identical symbols when the board is filled, the  |")
    print("|   game ends in a draw                                                                |")
    print("|At the end of the game, our winners will be recorded in our \"Hall of Fame\"!           |")
    print("|______________________________________________________________________________________|")


# Effacer la console
def clearscreen(numlines: int = 100) -> None:
    if os.name == "posix":  # Pour Unix/Linux/MacOS/BSD/etc
        os.system("clear")
    elif os.name in ("nt", "dos", "ce"):  # Pour DOS/Windows
        os.system("CLS")
    else:  
        print("\n" * numlines) # Autre OS

# Enregistre le résultat d'une partie dans le fichier Hall of fame
def writeHallOfFame(winner:str,loser:str, party:int) -> None:
    try:
        # Open the file in write mode ('a')
        with open('hall_of_fame.csv', mode='a', newline='') as csvfil:
            #Create instance of CSV reader
            writer = csv.writer(csvfil)
            writer.writerow([f"Winner: {winner} - Loser: {loser} - Number of games: {party}"])

    except FileNotFoundError:
        print("The specified file was not found.")
    except PermissionError:
        print("You don't have permission to write to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    else:
        print("Party save !!!!!!!!!")


#Afficher le resultat précédant
def readHallOfFame() -> None:
    try:
        # Open the file in write mode ('r')
        with open('hall_of_fame.csv', newline='') as csvfil:
            content:str = csv.reader(csvfil)
            print("\nHALL OF GAME:")
            if content:
                for ligne in content:
                    print(ligne[0])
            else:
                print('The file is empty') 
    except FileNotFoundError:
        print("The specified file was not found.")
    except PermissionError:
        print("You don't have permission to write to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}") 

#Afficher le tableau
def DrawBoard(square:List[int]) -> None:
    print(' ','7' if square[7] == " " else square[7],'  |  ','8' if square[8] == " " else square[8],'  |  ','9' if square[9] == " " else square[9],' ')
    print("------|-------|------")
    print(' ','4' if square[4] == " " else square[4],'  |  ','5' if square[5] == " " else square[5],'  |  ' ,'6' if square[6] == " " else square[6],' ')
    print("------|-------|------")
    print(' ','1' if square[1] == " " else square[1],'  |  ','2' if square[2] == " " else square[2],'  |  ' ,'3' if square[3] == " " else square[3],' ')

#Mettre à jour le tableau
def UpdateBoard(typeChar:str,pos:int,square:List[int]) -> None:
    square[int(pos)] = typeChar
    DrawBoard(square)

#take de use position
def UserInput(userTurn:int, one:Player, two:Player) -> int:
    pos=0
    while True:
        try:
            while not int(pos) in range(1,10):
                if userTurn == 1:
                    pos = int(input(f"{one.name} Enter a position value 1-9: "))
                else:
                    pos = int(input(f"{two.name} Enter a position value 1-9: "))                
        except ValueError:
            print("Not an integer between 1-9. Try again.")
            continue
        else:
            return pos

def CheckTurn(UserTurn:int) -> int:
	#Determines whos turn it is
    if UserTurn == 1:
        UserTurn = 2
    else:
        UserTurn = 1
    return UserTurn

#Token du joueur actuel
def XOToggle(userTurn:int, one:Player, two:Player) -> str:
    if userTurn == 1:
        return one.token
    else:
        return two.token

# nom tu joueur actuel
def nameToggle(userTurn:int, one:Player, two:Player) -> str:
    if userTurn == 1:
        return one.name
    else:
        return two.name

# Vérifié sur le tableau est plien
def isBoardFull(square:List[int]) -> bool:
    if square.count(" ") <= 1:
        return True
    return False
    
#Vérifier l'état du jeux
def WinningSequences(square:List[int], count:int, one:Player, two:Player) -> bool:
    winner = ""
    loser = ""
    gameInSession = True
    # Victoire du joueur avec le token X
    if square[1] == one.token and square[5] == one.token and square[9] == one.token : winner = one.name; loser = two.name
    elif square[3] == one.token and square[5] == one.token and square[7] == one.token: winner = one.name; loser = two.name
    
    elif square[1] == one.token and square[2] == one.token and square[3] == one.token: winner = one.name; loser = two.name
    elif square[4] == one.token and square[5] == one.token and square[6] == one.token: winner = one.name; loser = two.name
    elif square[7] == one.token and square[8] == one.token and square[9] == one.token: winner = one.name; loser = two.name
    
    elif square[1] == one.token and square[4] == one.token and square[7] == one.token: winner = one.name; loser = two.name
    elif square[2] == one.token and square[5] == one.token and square[8] == one.token: winner = one.name; loser = two.name
    elif square[3] == one.token and square[6] == one.token and square[9] == one.token: winner = one.name; loser = two.name
    #Victoire du joueur avec le token O
    elif square[1] == two.token and square[5] == two.token and square[9] == two.token: winner = two.name; loser = one.name
    elif square[3] == two.token and square[5] == two.token and square[7] == two.token: winner = two.name; loser = one.name
    
    elif square[1] == two.token and square[2] == two.token and square[3] == two.token: winner = two.name; loser = one.name
    elif square[4] == two.token and square[5] == two.token and square[6] == two.token: winner = two.name; loser = one.name
    elif square[7] == two.token and square[8] == two.token and square[9] == two.token: winner = two.name; loser = one.name
    
    elif square[1] == two.token and square[4] == two.token and square[7] == two.token: winner = two.name; loser = one.name
    elif square[2] == two.token and square[5] == two.token and square[8] == two.token: winner = two.name; loser = one.name
    elif square[3] == two.token and square[6] == two.token and square[9] == two.token: winner = two.name; loser = one.name
    
    elif isBoardFull(square) == True:
        print("Draw! Game over")
        gameInSession = False
        return gameInSession
    #Aucun joueur n'est gagnant
    if winner == "":
        gameInSession = True
        return gameInSession
    #Un joueur est gagnant
    else:
        print(f"{winner} Wins!!")
        writeHallOfFame(winner, loser, count)
        gameInSession = False
        return gameInSession

#Vérifier si un emplacement est pris
def SqaureIsTaken (chk:bool, posi:int, userTurn, square:List[int], one:Player, two:Player) -> int:
    location = posi 
    newPos = 0 
    if chk == True:
        while square[location] == "X" or square[location] == "O":
            print ("This square was already taken. Please choose a different square.") 
            newPos = UserInput (userTurn, one, two) 
            if square[newPos] == " ":
                chk = False 
                break
    return newPos

