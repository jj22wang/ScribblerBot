#Testing for path algorithm
from myro import *
from collections import deque
from bfsw import *
from backtracew import *
from movement4 import *
from change_grid import *

#Takes in a String of commands and corresponds the movements on the map
def move_path(grid, a, init_x, init_y, dest_x, dest_y):
    shortest_path(grid, init_x, init_y, dest_x, dest_y)
    print grid
    commands = describe_path(grid, dest_x, dest_y)
    print commands
    obstacles = deque()

    
    while len(commands) > 0:
        command = commands.pop()
        obs_blocked = 0
        if command == a.UP:
            obs_blocked = a.move_up()
        elif command == a.DOWN:
            obs_blocked = a.move_down()
        elif command == a.RIGHT:
            obs_blocked = a.move_right()
        elif command == a.LEFT:
            obs_blocked = a.move_left()

        a.print_coordinates() #Testing purposes...

        #If the bot detects a permanent obstacle        
        if obs_blocked == 1:
            #If so, update grid, find new path
            update_grid(grid, command, a.x, a.y, obstacles)
            print grid
            print obstacles
            shortest_path(grid, a.x, a.y, dest_x, dest_y)
            commands = describe_path(grid, dest_x, dest_y)
            print commands
    clear_grid(grid, obstacles)
