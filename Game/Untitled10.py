#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(" " + board[7] + " | " + " " + board[8] + " | " + " " + board[9] + " | ")
    print("______________")
    print(" " + board[4] + " | " + " " + board[5] + " | " + " " + board[6] + " | ")
    print("______________")
    print(" " + board[1] + " | " + " " + board[2] + " | " + " " + board[3] + " | ")


# In[2]:


board = [" "]*10


# In[3]:


display_board(board)


# In[4]:


def player_input():
    marker = ''
    
    while not (marker == "X" or marker == "O"):
        marker = input("Player 1: Do you want to be X or O? ").upper()
    
    if marker == "X":
        return ("X", "O")
    else:
        return ("O", "X")
    


# In[5]:


player_input()


# In[6]:


def place_marker(board, marker, position):
    board[position] = marker


# In[7]:


place_marker(board, "o", 8)
display_board(board)


# In[8]:


def win_check(board, mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[7] == mark and board[4] == mark and board[1] == mark) or 
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    (board[9] == mark and board[5] == mark and board[1] == mark))


# In[9]:


import random

def choose_first():
    if random.randint(0,1) == 0:
        return "Player 1"
    else:
        return "Player 2"


# In[10]:


def space_check(board, position):
    
    return board[position] == " "


# In[11]:


def full_board(board):
    
    for i in range(1,10):
        if space_check(board, i):
            return False

    return True


# In[12]:


full_board(board)


# In[13]:


def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input("Choose your next position 1-9 "))
        
    return position


# In[14]:


def replay():
    
    choice = input("Do you want to play again? Enter Yes or No: ").lower()
    
    return choice == "yes"


# In[ ]:


print("Welcome to TTT! ")

while True:
    board = [" "]*10  
    player1_marker, player2_marker = player_input()
    
    turn = choose_first()
    print(turn + " your turn! ")
    
    play_game = input("Ready to play? y or n? ")
    
    if play_game == "y":
        game_on = True
    else:
        game_on = False
        
    while game_on:
            
        if turn =="Player 1":
            
            display_board(board)
            position = player_choice(board)
            place_marker(board, player1_marker, position)
            
            if win_check(board,player1_marker):
                display_board(board)
                print("Player 1 has won!")
                game_on = False
            else:
                if full_board(board):
                    display_board(board)
                    print("Tie Game!")
                    game_on = False
                else:
                    turn = "Player 2"
        else:
            display_board(board)
            position = player_choice(board)
            place_marker(board, player2_marker, position)
            
            if win_check(board,player2_marker):
                display_board(board)
                print("Player 2 has won!")
                game_on = False
            else:
                if full_board(board):
                    display_board(board)
                    print("Tie Game!")
                    game_on = False
                else:
                    turn = "Player 1"
    if not replay():
        break


# In[ ]:




