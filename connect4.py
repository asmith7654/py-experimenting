import numpy as np

#CREATE BOARD
#0 means empty, 1 means player1, 2 means player2
board = np.zeros((6, 7))

#CURRENT TURN TEAM
current = 0

#DISPLAY BOARD FUNCTION
def display(board) -> None:
    for row in range(0,6):
        print("")
        for col in range(0,7):
            print(f"- {int(board[row,col])} -", end="")

    print("")
    print("")

#WIN CONDITION FUNCTION
def win(board) -> bool:
    #Check horizontal wins
    for i in range(0,6):
        for j in range (0,4):
            if (board[i,j]==board[i,j+1]==board[i,j+2]==board[i,j+3] and board[i,j]!=0):
                return True
    
    #Check vertical wins
    for i in range(0,3):
        for j in range (0,7):
            if (board[i,j]==board[i+1,j]==board[i+2,j]==board[i+3,j] and board[i,j]!=0):
                return True
            
    #Check right diagonal wins
    for i in range(0,3):
        for j in range (0,4):
            if (board[i,j]==board[i+1,j+1]==board[i+2,j+2]==board[i+3,j+3] and board[i,j]!=0):
                return True
            
    #Check left diagonal wins
    for i in range(0,3):
        for j in range (6,2,-1):
            if (board[i,j]==board[i+1,j-1]==board[i+2,j-2]==board[i+3,j-3] and board[i,j]!=0):
                return True

#DROP PIECE FUNCTION
def drop(col: int) -> None:
    row = emptyRow(col)
    if row==-1:
        newCol = input("Column is full, please choose another column: ")
        drop(int(newCol)-1)
    else:
        board[row,col] = current
    

#EMPTY ROW FINDER FUNCTION FOR DROPPING PIECES
def emptyRow(col: int) -> int:
    for i in range(5,-1,-1):
        if board[i,col]==0:
            return i
    
    return -1

#MAIN GAMEPLAY LOOP
def play():
    global current
    global board
    board = np.zeros((6, 7))
    print("Welcome to Connect4! Each slot in the board will be filled with a 0, 1, or 2. \nA 0 means it is empty, a 1 means Player 1 dropped a disk there, and a 2 means Player 2 dropped a disk there. Good luck!")
    display(board)

    while True:
        current = 1
        dropCol = input("Player 1, choose a column 1-7 to drop a piece: ")
        drop(int(dropCol)-1)
        display(board)
        if win(board): 
            print("Player 1 wins!")
            break

        current = 2
        dropCol = input("Player 2, choose a column 1-7 to drop a piece: ")
        drop(int(dropCol)-1)
        display(board)
        if win(board): 
            print("Player 2 wins!")
            break

    playAgain = input("Would you like to play again? Type 'yes' or 'no': ")
    if playAgain=="yes":
        play()
    else:
        print("Thanks for playing!")



#TEST RUN
play()
