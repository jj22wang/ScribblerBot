from collections import deque
from backtrace import describe_path

def shortest_path(grid,start_x,start_y,end_x,end_y):
    q=deque()
    x_bound=len(grid)
    y_bound=len(grid[1])
    counter=1
    grid[start_x][start_y]=counter
    done=0
    q.append(start_x)
    q.append(start_y)
    q.append(counter)
    while done == 0:
        cur_point_x=q.popleft()
        cur_point_y=q.popleft()
        counter=q.popleft()
        #print '%s %s' %(cur_point_x,cur_point_y)
        counter+=1
        if(cur_point_x == end_x):
            if(cur_point_y == end_y):
                grid[cur_point_x][cur_point_y]=counter-1
                done=1
                break
        if (cur_point_x + 1) < x_bound:
            if grid[cur_point_x+1][cur_point_y] ==0:
                q.append(cur_point_x+1)
                q.append(cur_point_y)
                q.append(counter)
                #print '%s %s' %(cur_point_x+1,cur_point_y)
                #print "right"
                
                grid[cur_point_x+1][cur_point_y]=counter
        if (cur_point_y + 1) < y_bound:
            if grid[cur_point_x][cur_point_y+1] == 0:
                q.append(cur_point_x)
                q.append(cur_point_y+1)
                q.append(counter)
                #print "up"
                grid[cur_point_x][cur_point_y+1]=counter
        if (cur_point_x - 1) >= 0:
            if grid[cur_point_x-1][cur_point_y] == 0:
                q.append(cur_point_x-1)
                q.append(cur_point_y)
                q.append(counter)
                #print "left"
                grid[cur_point_x-1][cur_point_y]=counter
        if (cur_point_y - 1) >= 0:
            if grid[cur_point_x][cur_point_y-1] ==0:
                q.append(cur_point_x)
                q.append(cur_point_y-1)
                q.append(counter)
                #print "down"
                grid[cur_point_x][cur_point_y-1]=counter
        

    for i in range (0,x_bound):
        print '%s %s %s' %(grid[i][0],grid[i][1],grid[i][2])

    return grid

grid1=[[0,0,0],[0,-1,0],[0,-1,0],[0,0,0]]
a=shortest_path(grid1,0,0,2,2)
q2=describe_path(a)
i=0
while i<len(q2):
    x=q2.pop()
    print x
