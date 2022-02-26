#!/usr/bin/env python
# coding: utf-8

# ## PYTHON PROGRAM TO RUN TIC-TAC-TOE GAME by KONARK P.
# ### RUN ALL CELLS TO PLAY GAME.

# In[1]:


#FUNCTION TO DISPLAY BOARD:


def display_board(board):
    
    print(board[1]+" | "+board[2]+" | "+board[3])
    print("---------") 
    print(board[4]+" | "+board[5]+" | "+board[6])
    print("---------") 
    print(board[7]+" | "+board[8]+" | "+board[9])
    
    


# In[2]:


#FUNCTION TO ASSIGN PLAYER MARKERS (X or O):

def player_input():

    
    #OUTPUT = tuple of form (Pl marker, P2 marker)
       
    marker = ''    
    valid_input = ['X','O']
    
    while marker not in valid_input: 
        
        marker = input("Player 1: Do you want to be X or O? ").upper()
        
        if marker not in valid_input:
            print("Sorry, invalid choice. Choose again: ")
            
    if marker == 'X':
        return ('X','O')
        
    else:
        return ('O','X')


# In[3]:


#FUNCTION TO PLACE MARKER ON BOARD:

def place_marker(board, marker, position):
    
    board[position] = marker


# In[4]:


#FUNCTION TO CHECK IF WIN: 

def win_check(board, mark):
    
    #WIN SITUATION:
    
    # for 3 ROWS, CHECK IF SAME MARK
    
    return ((board[1]==board[2]==board[3]==mark) or (board[4]==board[5]==board[6]==mark) 
    or (board[7]==board[8]==board[9]==mark) or 
    
    
    # for 3 COLUMS, CHECK IF SAME MARK
    
    (board[1]==board[4]==board[7]==mark) or (board[2]==board[5]==board[8]==mark) 
    or (board[3]==board[6]==board[9]==mark)or 
    
    
    # for 2 DIAGONALS, CHECK IF SAME MARK
    
    (board[1]==mark and board [5] == mark and board [9] == mark) or 
    (board[3] ==board[5]==board[7]==mark))


# In[5]:


#FUNCTION TO CHECK WHICH PLAYER GOES FIRST:

import random

def choose_first():
    toss = random.randint(0,1)
    
    if(toss==0):
        return 'Player 1'    
    else:
        return 'Player 2'
    


# In[6]:


#FUNCTION TO CHECK IF BOARD POSITION IS AVAILABLE: 

def space_check(board, position):
    
    return board[position]==' '


# In[7]:


#FUNC TO CHECK IF BOARD IS FULL:

def full_board_check(board):
    
    
    for i in range(1,10):
        if space_check(board, i):
            return False
    
    #Board is full:
    return True 


# In[8]:


#FUNC TO READ POSITION FOR MARKER FROM PLAYER:

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position


# In[9]:


#FUNC TO ASK IF PLAYER WANTS TO REPLAY

def replay():
    
    play_again = "WRONG"
    valid_input = ['y','n']
    
    while play_again not in valid_input:
        
        play_again = input("Play again: Yes or No? ").lower()
        
        if play_again not in valid_input:
            print("Sorry, invalid choice. Choose again: ")
            
    return play_again[0] == 'y'
        


# In[10]:


#FUNC TO DISPLAY GAME INSTRUCTIONS

def instructions():

    print('INSTRUCTIONS:')
    print("These are the board positions: Choose positions accordingly when playing.")
    print("1" + " | " + "2" +" | " + "3")
    print("---------") 
    print("4" + " | " + "5" +" | " + "6")
    print("---------") 
    print("7" + " | " + "8" +" | " + "9")


# In[11]:


#FUNC TO RUN TICTACTOE GAME:

def tictactoe():

    print('Welcome to Tic Tac Toe!')

    print("Enter 'I' for instructions.")
    print("Otherwise, enter to start game.")
    initial_input = input("Enter input:").upper()

    if(initial_input)=='I':
        instructions()

    else:
        pass


    while True:
        # Reset the board
        theBoard = [' '] * 10
        player1_marker, player2_marker = player_input()
        turn = choose_first()
        print(turn + ' will go first.')

        play_game = input('Are you ready to play? Enter Yes or No.')

        if play_game.lower()[0] == 'y':
            game_on = True
        else:
            game_on = False

        while game_on:
            if turn == 'Player 1':
                # Player1's turn.

                display_board(theBoard)
                position = player_choice(theBoard)
                place_marker(theBoard, player1_marker, position)

                if win_check(theBoard, player1_marker):
                    display_board(theBoard)
                    print('Player 1 wins!')
                    game_on = False
                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Player 2'

            else:
                # Player2's turn.

                display_board(theBoard)
                position = player_choice(theBoard)
                place_marker(theBoard, player2_marker, position)

                if win_check(theBoard, player2_marker):
                    display_board(theBoard)
                    print('Player 2 wins!')
                    game_on = False
                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Player 1'

        if not replay():
            break
            print("Thanks for playing!")


# In[13]:


#CALL FUNCTION TO PLAY GAME:

tictactoe()