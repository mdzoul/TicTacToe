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

def replace_spot():
    for list in board:
        list_idx = board.index(list)
        for value in list:
            if value == player1:
                value_idx = list.index(value)
                board[list_idx][value_idx] = 'X'

board = [
    ['1','2','3'],
    ['4','5','6'],
    ['7','8','9'],
]    

display_board()

player1 = input("Your turn, player 1: ")

replace_spot()
display_board()