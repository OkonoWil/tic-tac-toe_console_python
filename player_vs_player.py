from player import Player
from typing import List
import functions

#Variables

#functions

def game() -> None:

    #Variables
    square:List[int] = []
    square = [" " for x in range(10)] 
    pos:int = 0
    party:int = 0
    isUserTurn:int = 1
    player_one:Player = Player()
    player_two:Player = Player()

    #Initialisation
    functions.player_creator(player_one, player_two)
    functions.clearscreen()

    print("Tic Tac Toe Game start\n")
    functions.DrawBoard(square)
    while functions.WinningSequences(square, party, player_one, player_two) == True:
        #incremente le compteur de partie
        party+=1
        pos = functions.UserInput(isUserTurn, player_one, player_two)
        if square[pos] == "X" or square[pos] == "O":
            pos = functions.SqaureIsTaken(True, pos, isUserTurn, square, player_one, player_two)
        functions.UpdateBoard(functions.XOToggle(isUserTurn, player_one,player_two),pos, square)
        if functions.WinningSequences(square, party, player_one,player_two) == True:
            new_var = isUserTurn
            isUserTurn = functions.CheckTurn(new_var)
            print(functions.nameToggle(isUserTurn, player_one,player_two), "'s turn...")
            continue
        break
    
