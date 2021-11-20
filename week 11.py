#OR

########################################################################
##
## CS 101 Lab
## Name: Tyler Faust
## Email: tefqhg@umsystem.edu
##
## PROBLEM : make a clock
##      
## ALGORITHM : 
##      1. take 4 user inputs
##      2. inputs go into a class
##      3. print clock class every second
## 
## ERROR HANDLING:
##
## OTHER COMMENTS:
##
########################################################################

import time

class Clock:
    def __init__(self, hour, minute, second, type):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.type = 0
        self.ampm = ""
        self.tempHour = 0

    def hour(self):
        return self.hour
    
    def setHour(self, input):
        self.hour = input
    
    def minute(self):
        return self.minute

    def setMinute(self, input):
        self.minute = input

    def second(self):
        return self.second

    def setSecond(self, input):
        self.second = input

    def set_clock_type(self, input):
        self.type = input

    def __str__(self):
        if self.type == 0:
            return "{:02}:{:02}:{:02}".format(self.hour, self.minute, self.second)
        
        elif self.type == 1:
            self.tempHour = self.hour
            if self.hour > 12:
                self.tempHour = self.hour - 12
                self.ampm = "pm"
            else:
                self.ampm = "am"
            return "{:02}:{:02}:{:02} {}".format(self.tempHour, self.minute, self.second, self.ampm)

    def tick(self):
        self.second += 1
        if self.second > 59:
            self.second = 0
            self.minute += 1
        if self.minute > 59:
            self.minute = 0
            self.hour += 1
        if self.hour > 23:
            self.hour = 0

if __name__ == "__main__":

    clock = Clock(0, 0, 0, 0)

    clock.setHour(int(input("What is the current hour ==> ")))
    clock.setMinute(int(input("What is the current minute ==> ")))
    clock.setSecond(int(input("What is the current second ==> ")))
    clock.set_clock_type(int(input("Clock type (0 = 24, 1 = 12) ==> ")))

    while True:
        print(clock)
        clock.tick()
        time.sleep(1)