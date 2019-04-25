import random
import os

def create_cells(number):
    cube = list(range(number))
    cells = []
    for row in cube:
        for column in cube:
            point = column, row
            cells.append(point)
    
    return cells


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_locations(cells):
    return random.sample(cells, 5)


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


def get_moves(player, limit):
    moves = {"A": "\u2b05", 
             "D": "\u27a1", 
             "W": "\u2b06",
             "S": "\u2b07"}
    x, y = player
    
    if x == 0:
        moves.pop("A")
    if x == limit:
        moves.pop("D")
    if y == 0:
        moves.pop("W")
    if y == limit:
        moves.pop("S")
    
    return list(moves.values()), list(moves.keys())

def draw_map(cells, size, actor, simbol):
    print("  -" * size)
    tile = "{}"
    for cell in cells:
        x, y = cell
        if x < (size - 1):
            end_line = ""
            output = look_for_actor(actor, cell, tile, simbol)
        else:
            end_line = "\n"
            output = look_for_actor(actor, cell, tile, simbol)

        print(output, end = end_line)
    print("  -" * size)      
            
def look_for_actor(actor, cell, tile, simbol):
    if cell == actor:
        output = tile.format(" {} ".format(simbol))
    else:
        output = tile.format(" \U0001F3E2 ")
        
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

def find_monster(cells, size, monster, form):
    clear_screen()
    draw_map(cells, size, monster, form)
    print("\n ** You LOSE! **\n")
    return False


def game_loop():
    size = 6
    cells = create_cells(size)
    monster1, monster2, monster3, door, player = get_locations(cells)
    playing = True
    while playing:
        clear_screen()
        draw_map(cells, size, player, "\U0001f47e")
        available_moves, controls = get_moves(player, size - 1)
        print("You're currently in room {}".format(player))
        print("You can move {}".format(", ".join(available_moves)))
        print("Enter QUIT to quit")
        
        move = input("> ")
        move = move.upper()
        
        if move == 'QUIT':
            print(" \U0001F44B  See you next GAME!!  \U0001F44B")
            return
            
        if move in controls:
            player = move_player(player, move)
        else:
            input("\n ** Walls are hard! don't run into them")
            continue
            
        if player == door:
            clear_screen()
            draw_map(cells, size, door, "\u2B50")
            print("\n  ** You WIN! **\n")
            playing = False
            
        if player == monster1:
            playing = find_monster(cells, size, monster1, "\U0001F4A9")
        
        if player == monster2:
            playing = find_monster(cells, size, monster2, "\U0001F47B")
        
        if player == monster3:
            playing = find_monster(cells, size, monster3, "\U0001F47D")
    
    playing_again()
    

print("Welcome to the dungeon!")
print("Controls: \u2b06 (W), \u2b05 (A), \u2b07 (S), \u27a1 (D)")
input("Press Enter to start!")
game_loop()