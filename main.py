import random
import time
from replit import clear
from art import logo

def display_board():
    print(f"""
     |     |     
  {board[0][0]}  |  {board[0][1]}  |  {board[0][2]}  
_____|_____|_____
     |     |     
  {board[1][0]}  |  {board[1][1]}  |  {board[1][2]}  
_____|_____|_____
     |     |     
  {board[2][0]}  |  {board[2][1]}  |  {board[2][2]}  
     |     |     
    """)
    
def replace_spot(pla_com):
    for list in board:
        list_idx = board.index(list)
        for value in list:
            if value == pla_com:
                value_idx = list.index(value)
                if pla_com == p1:
                    board[list_idx][value_idx] = '\33[1;31mX\33[0m'
                elif pla_com == com:
                    board[list_idx][value_idx] = '\33[1;34mO\33[0m'

def check_board():
    # Horizontal
    if board[0] == ['\33[1;31mX\33[0m','\33[1;31mX\33[0m','\33[1;31mX\33[0m'] or board[1] == ['\33[1;31mX\33[0m','\33[1;31mX\33[0m','\33[1;31mX\33[0m'] or board[2] == ['\33[1;31mX\33[0m','\33[1;31mX\33[0m','\33[1;31mX\33[0m']:
        return True
    if board[0] == ['\33[1;34mO\33[0m','\33[1;34mO\33[0m','\33[1;34mO\33[0m'] or board[1] == ['\33[1;34mO\33[0m','\33[1;34mO\33[0m','\33[1;34mO\33[0m'] or board[2] == ['\33[1;34mO\33[0m','\33[1;34mO\33[0m','\33[1;34mO\33[0m']:
        return True
    #Diagonal
    if board[0][0] == '\33[1;31mX\33[0m' and board[1][1] == '\33[1;31mX\33[0m' and board[2][2] == '\33[1;31mX\33[0m':
        return True
    if board[0][0] == '\33[1;34mO\33[0m' and board[1][1] == '\33[1;34mO\33[0m' and board[2][2] == '\33[1;34mO\33[0m':
        return True
    if board[0][2] == '\33[1;31mX\33[0m' and board[1][1] == '\33[1;31mX\33[0m' and board[2][0] == '\33[1;31mX\33[0m':
        return True
    if board[0][2] == '\33[1;34mO\33[0m' and board[1][1] == '\33[1;34mO\33[0m' and board[2][0] == '\33[1;34mO\33[0m':
        return True
    #Vertical
    if board[0][0] == '\33[1;31mX\33[0m' and board[1][0] == '\33[1;31mX\33[0m' and board[2][0] == '\33[1;31mX\33[0m':
        return True
    if board[0][0] == '\33[1;34mO\33[0m' and board[1][0] == '\33[1;34mO\33[0m' and board[2][0] == '\33[1;34mO\33[0m':
        return True
    if board[0][1] == '\33[1;31mX\33[0m' and board[1][1] == '\33[1;31mX\33[0m' and board[2][1] == '\33[1;31mX\33[0m':
        return True
    if board[0][1] == '\33[1;34mO\33[0m' and board[1][1] == '\33[1;34mO\33[0m' and board[2][1] == '\33[1;34mO\33[0m':
        return True
    if board[0][2] == '\33[1;31mX\33[0m' and board[1][2] == '\33[1;31mX\33[0m' and board[2][2] == '\33[1;31mX\33[0m':
        return True
    if board[0][2] == '\33[1;34mO\33[0m' and board[1][2] == '\33[1;34mO\33[0m' and board[2][2] == '\33[1;34mO\33[0m':
        return True

board = [
    ['1','2','3'],
    ['4','5','6'],
    ['7','8','9'],
]    

list_num = ['1','2','3','4','5','6','7','8','9']

logo()
display_board()

end_game = False
while not end_game:
    if check_board() == True:
        end_game = True
        print("\33[31mGame Over\33[0m")
        break

    while check_board() != True:
        p1 = input("Your turn, player 1: ")
        list_num.remove(p1)
        replace_spot(p1)
        
        clear()
        logo()
        display_board()
        check_board()

        time.sleep(1.5)

        if check_board() != True:
            com = str(random.choice(list_num))
            list_num.remove(com)
            replace_spot(com)
            
            clear()
            logo()
            print("Computer's turn:")
            time.sleep(1)
            display_board()
            check_board()

            time.sleep(1.5)
        else:
            break
        
