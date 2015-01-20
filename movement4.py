from myro import *
from collections import deque

#This class defines "standard" robot movement.
#Its purpose is to provide easier movement method calls for the myro bot.
class Movement:
    #Directional constants
    DOWN = "down"
    RIGHT = "right"
    UP = "up"
    LEFT = "left"
    #Obstacle detection constant
    DETECT = 750

    #This initalization assumes that the bot is facing foward at (0,0)
    def __init__(self, turn_spd, turn_time, trans_spd, trans_time):
        self.turn_spd = turn_spd
        self.turn_time = turn_time
        self.trans_spd = trans_spd
        self.trans_time = trans_time
        self.direction = "right"
        
        #Setting (0,0) to be upper-left corner of the grid
        self.x = 0
        self.y = 0

    #Sets turn values for the speed and time
    def set_turn_values(self, spd, time):
        self.turn_spd = spd
        if time >= 0:
            self.turn_time = time

        print self.turn_spd
        print self.turn_time
        print "\n"

    #Sets translation values for the speed and time 
    def set_trans_values(self, spd, time):
        self.trans_spd = spd
        if time >= 0:
            self.trans_time = time

        print self.trans_spd
        print self.trans_time
        print "\n"

    #For testing purposes...
    def print_coordinates(self):
        print self.x
        print self.y
        print self.direction
        print "\n"

    #Move the bot up by one square
    #(The square is defined by the speed and time set)
    def move_up(self):
        if self.direction == self.DOWN:
            turnLeft(self.turn_spd, self.turn_time)
            self.direction = self.RIGHT
            turnLeft(self.turn_spd, self.turn_time)
            self.direction = self.UP     
        elif self.direction == self.RIGHT:
            turnLeft(self.turn_spd, self.turn_time)
            self.direction = self.UP
        elif self.direction == self.LEFT:
            turnRight(self.turn_spd, self.turn_time)
            self.direction = self.UP

        #The bot steps four times per square, checking for obstacles within each steps    
        i = 0
        not_safe_pass = 0
        while i < 4 and not_safe_pass == 0:
            #First checking if an object blocks its path
            not_safe_pass = self.check_obstacle()
            j = 0
            #Checking to see if the obstacle is considered "permanent"
            while j < 5 and not_safe_pass == 1:
                j += 1
                wait(1)
                not_safe_pass = self.check_obstacle()

            if not_safe_pass == 1: #If object is permanent
                print "Not safe to pass..."
                backward(self.trans_spd, self.trans_time * i / 4)
                #backward(self.trans_spd, self.trans_time / 4)
            else:
                forward(self.trans_spd, self.trans_time / 4)
                i += 1

        #If the bot has moved one square
        if i == 4:
            self.y -= 1
        return not_safe_pass

    #Move the bot down by one square
    #(The square is defined by the speed and time set)
    def move_down(self):
        if self.direction == self.UP:
            turnLeft(self.turn_spd, self.turn_time)
            self.direction = self.LEFT
            turnLeft(self.turn_spd, self.turn_time)
            self.direction = self.DOWN
        elif self.direction == self.LEFT:
            turnLeft(self.turn_spd, self.turn_time)
            self.direction = self.DOWN
        elif self.direction == self.RIGHT:
            turnRight(self.turn_spd, self.turn_time)
            self.direction = self.DOWN

        #The bot steps four times per square, checking for obstacles within each steps    
        i = 0
        not_safe_pass = 0
        while i < 4 and not_safe_pass == 0:
            #First checking if an object blocks its path
            not_safe_pass = self.check_obstacle()
            j = 0
            #Checking to see if the obstacle is considered "permanent"
            while j < 5 and not_safe_pass == 1:
                j += 1
                wait(1)
                not_safe_pass = self.check_obstacle()

            if not_safe_pass == 1: #If object is permanent
                print "Not safe to pass..."
                backward(self.trans_spd, self.trans_time * i / 4)
                #backward(self.trans_spd, self.trans_time / 4)
            else:
                forward(self.trans_spd, self.trans_time / 4)
                i += 1

        #If the bot has moved one square
        if i == 4:          
            self.y += 1
        return not_safe_pass

    #Move the bot right by one square
    #(The square is defined by the speed and time set)
    def move_right(self):
        if self.direction == self.LEFT:
            turnLeft(self.turn_spd, self.turn_time)
            self.direction = self.DOWN
            turnLeft(self.turn_spd, self.turn_time)
            self.direction = self.RIGHT
        elif self.direction == self.DOWN:
            turnLeft(self.turn_spd, self.turn_time)
            self.direction = self.RIGHT
        elif self.direction == self.UP:
            turnRight(self.turn_spd, self.turn_time)
            self.direction = self.RIGHT
        
        #The bot steps four times per square, checking for obstacles within each steps    
        i = 0
        not_safe_pass = 0
        while i < 4 and not_safe_pass == 0:
            #First checking if an object blocks its path
            not_safe_pass = self.check_obstacle()
            j = 0
            #Checking to see if the obstacle is considered "permanent"
            while j < 5 and not_safe_pass == 1:
                j += 1
                wait(1)
                not_safe_pass = self.check_obstacle()

            if not_safe_pass == 1: #If object is permanent
                print "Not safe to pass..."
                backward(self.trans_spd, self.trans_time * i / 4)
                #backward(self.trans_spd, self.trans_time / 4)
            else:
                forward(self.trans_spd, self.trans_time / 4)
                i += 1

        #If the bot has moved one square
        if i == 4:       
            self.x += 1
        return not_safe_pass

    #Move the bot left by one square
    #(The square is defined by the speed and time set)
    def move_left(self):
        if self.direction == self.RIGHT:
            turnLeft(self.turn_spd, self.turn_time)
            self.direction = self.UP
            turnLeft(self.turn_spd, self.turn_time)
            self.direction = self.LEFT
        elif self.direction == self.UP:
            turnLeft(self.turn_spd, self.turn_time)
            self.direction = self.LEFT
        elif self.direction == self.DOWN:
            turnRight(self.turn_spd, self.turn_time)
            self.direction = self.LEFT
        
        #The bot steps four times per square, checking for obstacles within each steps    
        i = 0
        not_safe_pass = 0
        while i < 4 and not_safe_pass == 0:
            #First checking if an object blocks its path
            not_safe_pass = self.check_obstacle()
            j = 0
            #Checking to see if the obstacle is considered "permanent"
            while j < 5 and not_safe_pass == 1:
                j += 1
                wait(1)
                not_safe_pass = self.check_obstacle()

            if not_safe_pass == 1: #If object is permanent
                print "Not safe to pass..."
                backward(self.trans_spd, self.trans_time * i / 4)
                #backward(self.trans_spd, self.trans_time / 4)
            else:
                forward(self.trans_spd, self.trans_time / 4)
                i += 1

        #If the bot has moved one square
        if i == 4:          
            self.x -= 1
        return not_safe_pass

    #This function is called from every move function; checks three times to see if an obstacle exists
    #returns 1 if so, 0 otherwise
    def check_obstacle(self):
        blocked = 0
        max_range = 0
        temp = 0
        for x in range(0, 3):
            temp = getObstacle("center")
            if temp > max_range:
                max_range = temp
        if max_range >= self.DETECT:
            blocked = 1
        return blocked

    #Takes in a String of commands and corresponds the movements on the map
    '''def move_path(self, deque):
        invalid = 0 #Checks for # of invalid commands; for testing purposes
        while len(deque) > 0:
            command = deque.pop()
            if command == self.UP:
                self.move_up()
            elif command == self.DOWN:
                self.move_down()
            elif command == self.RIGHT:
                self.move_right()
            elif command == self.LEFT:
                self.move_left()
            else:
                invalid += 1
            self.print_coordinates() #Testing purposes...
        #For testing purposes, printing out the number of invalid commands
        if invalid > 0:
            print "This path had " + invalid + " commands."'''
