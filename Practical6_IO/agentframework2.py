#Practical 6 - I/O - Agent Framework
#201284811 Hannah Wheldon
#Commented out sections from previous practical for comparison - can be removed

import random

class Agent (object):
    def __init__(self,random_seed,environment):
       random.seed(random_seed)
       self.environment = environment
       self.store = 0
       self._x=random.randint(0,99)
       self._y=random.randint(0,99)

    def __str__(self):
        return " x " + str(self._x)+" y "+str(self._y)

    #Move the agent 
    #Agent moves +1 space if less than 0.5 otherwise -1 space
    def move(self):
        #y coordinate
        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100
        #x coordinate
        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100
    
    def eat(self):
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10   
        
#From Practical5 - agentframwork.py
'''
import random

#Make agent
class Agent (object):
    def __init__(self):
        #random.seed(random_seed)
        #Assign random value between 0-99
        self._x=random.randint(0,99)
        self._y=random.randint(0,99)
        
    def __str__(self):
        return " x " + str(self._x)+" y "+str(self._y)
'''