import random
import os


CELLS = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
         (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
         (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
         (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
         (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_locations():
    return random.sample(CELLS, 3)


def move_player(player, move):
    x, y = player
    if move == "A":
        x -= 1
    if move == "D":
        x += 1
    if move == "W":
        y -= 1
    if move == "S":
        y += 1
    return x, y


def get_moves(player):
    moves = {"A": "\u2b05", 
             "D": "\u27a1", 
             "W": "\u2b06",
             "S": "\u2b07"}
    x, y = player
    
    if x == 0:
        moves.pop("A")
    if x == 4:
        moves.pop("D")
    if y == 0:
        moves.pop("W")
    if y == 4:
        moves.pop("S")
    
    return list(moves.values()), list(moves.keys())

def draw_map(actor, simbol):
    print(" -" * 5)
    tile = "{}"
    for cell in CELLS:
        x, y = cell
        if x < 4:
            end_line = ""
            output = look_for_actor(actor, cell, tile, simbol)
        else:
            end_line = "\n"
            output = look_for_actor(actor, cell, tile, simbol)

        print(output, end = end_line)
    print(" -" * 5)      
            
def look_for_actor(actor, cell, tile, simbol):
    if cell == actor:
        output = tile.format("{}".format(simbol))
    else:
        output = tile.format("\U0001F3E2")
        
    return output

def playing_again():
    answer = None
    while answer != "y":
        answer = input("Would you like to playin again? [y]es/[n]o\n> ")
        answer = answer.lower()
        if answer == 'n':
            print(" \U0001F44B  See you next GAME!!  \U0001F44B")
            return
        
    game_loop()



def game_loop():
    monster, door, player = get_locations()
    playing = True
    while playing:
        clear_screen()
        draw_map(player, "\U0001f47e")
        available_moves, controls = get_moves(player)
        print("You're currently in room {}".format(player))
        print("You can move {}".format(", ".join(available_moves)))
        print("Enter QUIT to quit")
        
        move = input("> ")
        move = move.upper()
        
        if move == 'QUIT':
            print(" \U0001F44B  See you next GAME!!  \U0001F44B")
            break
            
        if move in controls:
            player = move_player(player, move)
        else:
            input("\n ** Walls are hard! don't run into them")
            continue
            
        if player == door:
            clear_screen()
            draw_map(door, "\u2B50")
            print("\n  ** You WIN! **\n")
            playing = False
            
        if player == monster:
            clear_screen()
            draw_map(monster, "\U0001f47b")
            print("\n ** You LOSE! **\n")
            playing = False
    
    playing_again()
    
    
print("Welcome to the dungeon!")
print("Controls: \u2b06 (W), \u2b05 (A), \u2b07 (S), \u27a1 (D)")
input("Press Enter to start!")
game_loop()
    