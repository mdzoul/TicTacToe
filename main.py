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
                if p1_vs == '1':
                    if pla_com == p1:
                        board[list_idx][value_idx] = '\33[1;31mX\33[0m'
                    elif pla_com == com:
                        board[list_idx][value_idx] = '\33[1;34mO\33[0m'
                elif p1_vs == '2':
                    if pla_com == p1:
                        board[list_idx][value_idx] = '\33[1;31mX\33[0m'
                    elif pla_com == p2:
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
    #Draw
    if list_num == []:
        return True

def refresh():
    clear()
    logo()

def loading(a):
    if a == "Start":
        b = "2"
    elif a == "Exit":
        b = "1"
    clear()
    logo()
    print(f"\33[3{b}m{a}ing game.\33[0m")
    time.sleep(0.5)
    clear()
    logo()
    print(f"\33[3{b}m{a}ing game..\33[0m")
    time.sleep(0.5)
    clear()
    logo()
    print(f"\33[3{b}m{a}ing game...\33[0m")
    time.sleep(0.5)
    clear()
    logo()

should_end = False
while not should_end:
    board = [
    ['1','2','3'],
    ['4','5','6'],
    ['7','8','9'],
    ]    
    
    list_num = ['1','2','3','4','5','6','7','8','9']

    loading("Start")
    
    p1_vs = input("How many players?: ")
    
    clear()
    if p1_vs == '1':
        logo()
        display_board()
        
        end_game = False
        while not end_game:
            if check_board() == True:
                end_game = True
                print("\33[31mGame Over\33[0m")
                time.sleep(1)
                break
        
            while check_board() != True:
                if list_num != []:
                    p1 = input("Your turn: ")
                    list_num.remove(p1)
                    replace_spot(p1)
                    
                    refresh()
                    
                    display_board()
                    check_board()
            
                    time.sleep(1)
            
                    if check_board() != True:
                        if list_num != []:
                            com = str(random.choice(list_num))
                            list_num.remove(com)
                            replace_spot(com)
                            
                            refresh()
                            print("Computer's turn:")
                            time.sleep(0.5)
                            
                            display_board()
                            check_board()
                
                            time.sleep(1)
                        else:
                            break
                    else:
                        break
                else:
                    break
            
    elif p1_vs == '2':
        logo()
        display_board()
        
        end_game = False
        while not end_game:
            if check_board() == True:
                end_game = True
                print("\33[31mGame Over\33[0m")
                break
        
            while check_board() != True:
                if list_num != []:
                    p1 = input("Player 1's turn: ")
                    list_num.remove(p1)
                    replace_spot(p1)
                    
                    refresh()
                    
                    display_board()
                    check_board()
            
                    time.sleep(1)
            
                    if check_board() != True:
                        if list_num != []:
                            p2 = input("Player 2's turn: ")
                            list_num.remove(p2)
                            replace_spot(p2)
                            
                            refresh()
                            
                            display_board()
                            check_board()
                    
                            time.sleep(1)
                        else:
                            break
                    else:
                        break
                else:
                    break

    restart = input("\nRestart match? \33[32mY\33[0m/\33[31mN\33[0m\n").lower()
    if restart == 'n':
        should_end = True
        loading("Exit")
    elif restart == 'y':
        clear()
        continue