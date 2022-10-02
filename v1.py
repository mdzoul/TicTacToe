def display_board():
    x_o1 = '1'
    x_o2 = '2'
    x_o3 = '3'
    x_o4 = '4'
    x_o5 = '5'
    x_o6 = '6'
    x_o7 = '7'
    x_o8 = '8'
    x_o9 = '9'
    board = print(f"""
         |     |     
      {x_o1}  |  {x_o2}  |  {x_o3}  
    _____|_____|_____
         |     |     
      {x_o4}  |  {x_o5}  |  {x_o6}  
    _____|_____|_____
         |     |     
      {x_o7}  |  {x_o8}  |  {x_o9}  
         |     |     
    """)
    print(board)

display_board()

x_o1 = ''
x_o2 = ''
x_o3 = ''
x_o4 = ''
x_o5 = ''
x_o6 = ''
x_o7 = ''
x_o8 = ''
x_o9 = ''
player1_input = input("Your turn: ")
if player1_input == '1':
    answer = f"x_o{player1_input}"
    answer = 'X'
    
    board = print(f"""
         |     |     
      {x_o1}  |  {x_o2}  |  {x_o3}  
    _____|_____|_____
         |     |     
      {x_o4}  |  {x_o5}  |  {x_o6}  
    _____|_____|_____
         |     |     
      {x_o7}  |  {x_o8}  |  {x_o9}  
         |     |     
    """)
    print(board)