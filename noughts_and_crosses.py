import random as r

turn = 0
game = True
computer_icon = None
def game_start():
    def player_choice():
        global player_icon, board, vertical, horizontal, row1, row2, row3, computer_icon, turn
        if game == True:
            turn += 1
            position = input(f"Where do you want to place the {player_icon}? Press 1 for top row , 2 for second row and 3 for third row. Follow this with 1 for first column, 2 for second colum and 3 for third column. E.g 12 is first row middle column and 31 would be bottom row and first column ")
            horizontal = int((position[0]))
            vertical = int((position[1]))
            if turn > 1:
                if board[horizontal - 1][vertical - 1] == player_icon or board[horizontal - 1][vertical - 1] == computer_icon:
                    print("This place has been taken!")
                    player_choice()
                else:
                    board[horizontal - 1][vertical - 1] = player_icon

            else:
                board[horizontal - 1][vertical - 1] = player_icon
            logic()
            computer_choice()
    
    def computer_choice():
        global board, player_icon, computer_icon, vertical, horizontal,row1, row2, row3
        if game == True:
            computer_icon = "O"
            if player_icon != "X":
                computer_icon = "X"
            computer_vertical = r.randint(0,2)
            computer_horizontal = r.randint(0,2)

            while board[computer_horizontal][computer_vertical] == player_icon or board[computer_horizontal][computer_vertical] == computer_icon :
                    computer_vertical = r.randint(0,2)
                    computer_horizontal = r.randint(0,2)

            board[computer_horizontal][computer_vertical] = computer_icon
            print(f"{row1}\n{row2}\n{row3}")       
            logic()
            player_choice()

    def player_start():
        global player_icon
        print("Welcome to Noughts and Crosses!\n")
        player_icon = input("Noughts or Crosses - X or O: ").upper()
        game_board()

    def game_board():
        global board, row1, row2, row3
        row1 = ["  ","  ","  "]
        row2 = ["  ","  ","  "]
        row3 = ["  ","  ","  "]
        board = [row1, row2, row3]
        print(f"{row1}\n{row2}\n{row3}")
        player_choice()
    
    def logic():
        global board, player_icon, computer_icon, vertical, horizontal, row, row1, row2, row3, game
        if board[0][0] == player_icon and board[0][1] == player_icon and board[0][2] == player_icon or board[1][0] == player_icon and board[1][1] == player_icon and board[1][2] == player_icon or board[2][0] == player_icon and board[2][1] == player_icon and board[2][2] == player_icon or board[0][0] == player_icon and board[1][0] == player_icon and board[2][0] == player_icon or board[0][1] == player_icon and board[1][1] == player_icon and board[2][1] == player_icon or board[0][2] == player_icon and board[1][2] == player_icon and board[2][2] == player_icon or board[0][0] == player_icon and board[1][1] == player_icon and board[2][2] == player_icon or board[0][2] == player_icon and board[1][1] == player_icon and board[2][0] == player_icon:
            print(f"\n{row1}\n{row2}\n{row3}")
            print("\nYou win!")
            game = False
        elif board[0][0] == computer_icon and board[0][1] == computer_icon and board[0][2] == computer_icon or board[1][0] == computer_icon and board[1][1] == computer_icon and board[1][2] == computer_icon or board[2][0] == computer_icon and board[2][1] == computer_icon and board[2][2] == computer_icon or board[0][0] == computer_icon and board[1][0] == computer_icon and board[2][0] == computer_icon or board[0][1] == computer_icon and board[1][1] == computer_icon and board[2][1] == computer_icon or board[0][2] == computer_icon and board[1][2] == computer_icon and board[2][2] == computer_icon or board[0][0] == computer_icon and board[1][1] == computer_icon and board[2][2] == computer_icon or board[0][2] == computer_icon and board[1][1] == computer_icon and board[2][0] == computer_icon:
            print(f"\n{row1}\n{row2}\n{row3}")
            print("\nYou Lose!")
            game = False
        else:
            return
        
    player_start()

game_start()




