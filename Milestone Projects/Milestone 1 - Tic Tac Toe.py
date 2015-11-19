# Create a two player tic tac toe game.

import os

print ("Welcome to tic tac toe!")
print ("Please use the numpad for symbol placement")
print ("Player 1 (x) will go first. Enjoy!")

player = ['x','o']

grid = [7 ,8 ,9 ,4 ,5 ,6 ,1 ,2 ,3 ]

def pos_shift(position):
    if position == '7':
        return 0
    elif position == '8':
        return 1
    elif position == '9':
        return 2
    elif position == '4':
        return 3
    elif position == '5':
        return 4
    elif position == '6':
        return 5
    elif position == '1':
        return 6
    elif position == '2':
        return 7
    elif position == '3':
        return 8

def print_grid():
    i = 0
    start = 0
    end = 3
    while i < 3:
        print(grid[start:end])
        start += 3
        end += 3
        i+=1

def grid_place(position, player):
    pos = pos_shift(position)
    grid[pos] = player

def win_check():
    # top row check
    if grid[0] == 'x' and grid[1] == 'x' and grid[2] == 'x':
        return True
    elif grid[0] == 'o' and grid[1] == 'o' and grid[2] == 'o':
        return True
    # mid row check
    elif grid[3] == 'x' and grid[4] == 'x' and grid[5] == 'x':
        return True
    elif grid[3] == 'o' and grid[4] == 'o' and grid[5] == 'o':
        return True
    # bot row check
    elif grid[6] == 'x' and grid[7] == 'x' and grid[8] == 'x':
        return True
    elif grid[6] == 'o' and grid[7] == 'o' and grid[8] == 'o':
        return True
    # left vert check
    elif grid[0] == 'x' and grid[3] == 'x' and grid[6] == 'x':
        return True
    elif grid[0] == 'o' and grid[3] == 'o' and grid[6] == 'o':
        return True
    # mid vert check
    elif grid[1] == 'x' and grid[4] == 'x' and grid[7] == 'x':
        return True
    elif grid[1] == 'o' and grid[4] == 'o' and grid[7] == 'o':
        return True
    # right vert check
    elif grid[2] == 'x' and grid[5] == 'x' and grid[8] == 'x':
        return True
    elif grid[2] == 'o' and grid[5] == 'o' and grid[8] == 'o':
        return True
    # diag1 check
    elif grid[0] == 'x' and grid[4] == 'x' and grid[8] == 'x':
        return True
    elif grid[0] == 'o' and grid[4] == 'o' and grid[8] == 'o':
        return True
    # diag2 check  
    elif grid[2] == 'x' and grid[4] == 'x' and grid[6] == 'x':
        return True
    elif grid[2] == 'o' and grid[4] == 'o' and grid[6] == 'o':
        return True

def occupied(position):
    pos = pos_shift(position)
    if grid[pos] == 'x' or grid[pos] == 'o':
        return True
    return False 


player_token = player[0]

# For win checking, starting from mid[1] will cover a vast majority of the win cases. The only things that will need
# to be checked afterward are across the top and bot lists, and down the left and right side of all lists.

slots = 9

# Main game loop. Game will end when slots = 0 if no one has won by that point.
while slots > 0:
    print_grid()
    spot = raw_input("What position do you want to play? :")
    
    while occupied(spot): # Check to see if spot is already occupied by a player. Loop is only entered if this is true.
        spot = raw_input("Spot already occupied. Please choose another :")

    grid_place(spot, player_token)  
    os.system('cls' if os.name == 'nt' else 'clear')  

    if win_check(): # Another shorthand for True or False. Take a look at the actual function works for a refresher on why.
        print "You win, %r!" %(player_token)
        break # Breaks out of the main game loop, as the win condition for the game has been met.
    if player_token == player[0]:
        player_token = player[1]
    else:
        player_token = player[0]
    
    slots -= 1

print "No one wins! You're both terrible."
print_grid() # Prints out the layout of the final board, win lose or draw.