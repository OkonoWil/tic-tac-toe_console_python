from player import Player
from typing import List
import functions
import random

# Choose a ramdon position
def ChooseRandomSquare(positions:int) -> int:
    #Updates the Pc with a new random square becuase no other possible choices where available for a vicotry or defense
    newMove:int = random.choice(positions)
    positions.remove(newMove)
    # UpdateBoard('O',newMove)#DEBUGGING
    return newMove

# Computer turn
def PCTurn(square:List[int], positions:int , playerPos:int) -> int:
    positions.remove(playerPos) #takes the players last move and removes it from the list of possible positions
    '''=================================Offensive moves================================================='''
    '''====================== Seek Bottom Row Victory==========================='''
    if (square[1] == 'O' and square[2] == 'O') or (square[9] == 'O' and square[6] == 'O') or (square[7] == 'O' and square[5]=='O'):
        if 3 in positions:
            newMove = 3
            positions.remove(newMove)#every instance in offensive and  deffensive moves we have to update the list by
            # removing the computers choice
            return newMove
        else:
            return ChooseRandomSquare(positions)
    elif (square[1] == 'O' and square[3]=='O') or (square[8] == 'O' and square[5] == 'O'):
        if 2 in positions:
            newMove = 2
            positions.remove(newMove)
            return newMove
        else:
            return ChooseRandomSquare(positions)
    elif (square[2] == 'O' and square[3] == 'O') or (square[4] == 'O' and square[7] == 'O') or (square[5] == 'O' and square[9] == 'O'):
        if 1 in positions:
            newMove = 1
            positions.remove(newMove)
            return  newMove
        else:
            return ChooseRandomSquare(positions)
        '''===================== Seek Mid Row Victories==================================='''
    elif (square[7] == 'O' and square[1] == 'O') or (square[5] == 'O' and square[6]) == 'O':
        if 4 in positions:
            newMove = 4
            positions.remove(newMove)
            return  newMove
        else:
            return ChooseRandomSquare(positions)
    elif ((square[4] == 'O' and square[6] == 'O') or (square[8] == 'O' and square[2] == 'O') or
        (square[9] == 'O' and square[1] == 'O') or (square[7] == 'O' and square[3] == 'O')):
        if 5 in positions:
            newMove = 5
            positions.remove(newMove)
            return newMove
        else:
            return ChooseRandomSquare(positions)
    elif (square[3] == 'O' and square[9] == 'O') or (square[4] == 'O' and square[5] == 'O'):
        if 6 in positions:
            newMove = 6
            positions.remove(newMove)
            return newMove
        else:
            return ChooseRandomSquare(positions)
        '''===========================Seek Top row Victories==================================='''
    elif (square[1] == 'O' and square[4] == 'O') or (square[8] == 'O' and square[9] == 'O') or (
            square[5] == 'O' and square[3] == 'O'):
        if 7 in positions:
            newMove = 7
            positions.remove(newMove)
            return newMove
        else:
            return ChooseRandomSquare(positions)
    elif (square[2] == 'O' and square[5] == 'O') or (square[7] == 'O' and square[9] == 'O'):
        if 8 in positions:
            newMove = 8
            positions.remove(newMove)
            return newMove
        else:
            return ChooseRandomSquare(positions)
    elif (square[3] == 'O' and square[6] == 'O') or (square[7] == 'O' and square[8] == 'O') or (
            square[5] == 'O' and square[1] == 'O'):
        if 9 in positions:
            newMove = 9
            positions.remove(newMove)
            return newMove
        else:
            return ChooseRandomSquare(positions)




        '''=======================================Defensive Moves ==================================='''
        '''====================== Seek Bottom Row defense==========================='''
    elif (square[1] == 'O' and square[2] == 'X') or (square[9] == 'X' and square[6] == 'X') or (
            square[7] == 'X' and square[5] == 'X'):
        if 3 in positions:
            newMove = 3
            positions.remove(newMove)
            return newMove
        else:
            return ChooseRandomSquare(positions)
    elif (square[1] == 'X' and square[3] == 'X') or (square[8] == 'X' and square[5] == 'X'):
        if 2 in positions:
            newMove = 2
            positions.remove(newMove)
            return newMove
        else:
            return ChooseRandomSquare(positions)
    elif (square[2] == 'X' and square[3] == 'X') or (square[4] == 'X' and square[7] == 'X') or (
            square[5] == 'X' and square[9] == 'X'):
        if 1 in positions:
            newMove = 1
            positions.remove(newMove)
            return newMove
        else:
            return ChooseRandomSquare(positions)
        '''===================== Seek Mid Row Defense ==================================='''
    elif (square[7] == 'X' and square[1] == 'X') or (square[5] == 'X' and square[6]) == 'X':
        if 4 in positions:
            newMove = 4
            positions.remove(newMove)
            return newMove
        else:
            return ChooseRandomSquare(positions)
    elif ((square[4] == 'X' and square[6] == 'X') or (square[8] == 'X' and square[2] == 'X') or
          (square[9] == 'X' and square[1] == 'X') or (square[7] == 'X' and square[3] == 'X')):
        if 5 in positions:
            newMove = 5
            positions.remove(newMove)
            return newMove
        else:
            return ChooseRandomSquare(positions)
    elif (square[3] == 'X' and square[9] == 'X') or (square[4] == 'X' and square[5] == 'X'):
        if 6 in positions:
            newMove = 6
            positions.remove(newMove)
            return newMove
        else:
            return ChooseRandomSquare(positions)
        '''===========================Seek Top row Defense ==================================='''
    elif (square[1] == 'X' and square[4] == 'X') or (square[8] == 'X' and square[9] == 'X') or (
            square[5] == 'X' and square[3] == 'X'):
        if 7 in positions:
            newMove = 7
            positions.remove(newMove)
            return newMove
        else:
            return ChooseRandomSquare(positions)
    elif (square[2] == 'X' and square[5] == 'X') or (square[7] == 'X' and square[9] == 'X'):
        if 8 in positions:
            newMove = 8
            positions.remove(newMove)
            return newMove
        else:
            return ChooseRandomSquare(positions)
    elif (square[3] == 'X' and square[6] == 'X') or (square[7] == 'X' and square[8] == 'X') or (
            square[5] == 'X' and square[1] == 'X'):
        if 9 in positions:
            newMove = 9
            positions.remove(newMove)
            return newMove
        else:
            return ChooseRandomSquare(positions)
        '''===========================default move============================================'''
    else:
        return ChooseRandomSquare(positions)



def game() -> None:

    #Variables
    square:List[int] = []
    square = [" " for x in range(10)] 
    pos:int = 0
    party:int = 0
    isUserTurn:int = 1
    positionsTab = [1,2,3,4,5,6,7,8,9] 
    player_one:Player = Player()
    player_two:Player = Player()

    #Initialisation
    functions.player_ai_creator(player_one, player_two)
    functions.clearscreen()

    print("Tic Tac Toe Game start\n")
    functions.DrawBoard(square)
    while functions.WinningSequences(square, party, player_one, player_two) == True:
        #incrémenter le compteur de partie
        party+=1
        if isUserTurn == 1:
            pos = functions.UserInput(isUserTurn, player_one, player_two)
            if square[pos] == "X" or square[pos] == "O":
                pos = functions.SqaureIsTaken(True, pos, isUserTurn, square, player_one, player_two)
        else:
            pos = PCTurn(square, positionsTab, pos)
        functions.UpdateBoard(functions.XOToggle(isUserTurn, player_one,player_two),pos, square)
        if functions.WinningSequences(square, party, player_one,player_two) == True:
            new_var = isUserTurn
            isUserTurn = functions.CheckTurn(new_var)
            print(functions.nameToggle(isUserTurn, player_one,player_two), "'s turn...")
            continue
        break
    
