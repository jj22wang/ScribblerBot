from collections import deque

#This function updates the grid whenever a new obstacle has been detected
def update_grid(grid, command, cur_x, cur_y, obs_deque):
    #Setting new permanent obstacle
    if command == "up":
        grid[cur_x][cur_y - 1] = -1
        obs_deque.append([cur_x, cur_y - 1])
    elif command == "down":
        grid[cur_x][cur_y + 1] = -1
        obs_deque.append([cur_x, cur_y + 1])
    elif command == "left":
        grid[cur_x - 1][cur_y] = -1
        obs_deque.append([cur_x - 1, cur_y])
    elif command == "right":
        grid[cur_x + 1][cur_y] = -1
        obs_deque.append([cur_x + 1, cur_y])
    for i in range (0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] != -1:
                grid[i][j] = 0

#This function is to be called after a path has been moved; resets the grid to a clear state
def clear_grid(grid, temp_objects):
    #temp_objects is should be a deque that stores co-ordinates
    print temp_objects
    while len(temp_objects) > 0: #Clearing temporary objects
        #temp_coor is an array of size 2, the first element being the x co-ordinate
        temp_coor = temp_objects.popleft()
        grid[temp_coor[0]][temp_coor[1]] = 0
    #Clears all other objects except for the permanent objects, denoted as -1
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] != -1:
                grid[i][j] = 0 
        
grid = [[0,0,0,0], [0,0,0,0], [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]]
o_deque = deque()
update_grid(grid,"up",2,2,o_deque)
for i in range (0,4):
    print '%s %s %s %s %s' %(grid[0][i],grid[1][i],grid[2][i],grid[3][i],grid[4][i])
