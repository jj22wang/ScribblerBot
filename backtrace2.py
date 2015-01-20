from collections import deque
#from bfs3 import shortest_path
def describe_path(grid, dest_x, dest_y):
    x_bound=len(grid)
    y_bound=len(grid[1])
    q=deque()
    cur_point_x=dest_x
    cur_point_y=dest_y
    max = grid[dest_x][dest_y]
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
a=describe_path(grid1,1,3)
i=0
while i<len(a):
    x=a.pop()
    print x
