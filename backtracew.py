from collections import deque
def describe_path(grid,destX,destY):
    x_bound=len(grid)
    y_bound=len(grid[1])
    q=deque()
    
    cur_point_x=destX
    cur_point_y=destY
    counter=grid[cur_point_x][cur_point_y]
    #backtrace
    moved=0
    while counter>1:
        if (cur_point_x + 1) < x_bound:
            if(grid[cur_point_x+1][cur_point_y])==counter-1 and moved==0:
                q.append("left")
                cur_point_x+=1
                moved=1
        if (cur_point_y + 1) < y_bound:
            if(grid[cur_point_x][cur_point_y+1])==counter-1 and moved ==0:
                q.append("up")
                cur_point_y+=1
                moved=1
        if (cur_point_x - 1) >= 0:
            if(grid[cur_point_x-1][cur_point_y])==counter-1 and moved ==0:
                q.append("right")
                cur_point_x-=1
                moved=1
        if (cur_point_y - 1) >= 0:
            if(grid[cur_point_x][cur_point_y-1])==counter-1 and moved ==0:
                q.append("down")
                cur_point_y-=1
                moved=1
        counter-=1
        moved=0
    return q
