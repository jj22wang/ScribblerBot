from collections import deque
from bfs3 import *
def describe_path(grid):
    x_bound=len(grid)
    y_bound=len(grid[1])
    q=deque()
    cur_point_x=0
    cur_point_y=0
    #find max value
    max=0
    for i in range(0,x_bound):
        for j in range(0,y_bound):
            if grid[i][j]>max:
                max=grid[i][j]
                cur_point_x=i
                cur_point_y=j

    #backtrace
    moved=0
    while max>1:
        if (cur_point_x + 1) < x_bound:
            if(grid[cur_point_x+1][cur_point_y])==max-1 and moved==0:
                q.append("up")
                cur_point_x+=1
                moved=1
        if (cur_point_y + 1) < y_bound:
            if(grid[cur_point_x][cur_point_y+1])==max-1 and moved ==0:
                q.append("left")
                cur_point_y+=1
                moved=1
        if (cur_point_x - 1) >= 0:
            if(grid[cur_point_x-1][cur_point_y])==max-1 and moved ==0:
                q.append("down")
                cur_point_x-=1
                moved=1
        if (cur_point_y - 1) >= 0:
            if(grid[cur_point_x][cur_point_y-1])==max-1 and moved ==0:
                q.append("right")
                cur_point_y-=1
                moved=1
        max-=1
        moved=0
    return q
            
grid1=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]];
shortest_path(grid1,0,0,1,3)
a=describe_path(grid1)
i=0
while i<len(a):
    x=a.pop()
    print x
