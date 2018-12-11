'''
Agent Framework for ABM_Final

This file contains the code for the Agent class. This is imported into the
ABM_Final code. 

201284811 Hannah Wheldon
Version 1.0.0
'''

# pseudo-random number generator
import random

# Defining Agent class through movement, eating, sharing and vomiting 
# in the environment

# Create a new type of object with attributes attached
    # Create own functions, using 'def'
    
class Agent (object):
    # Constructor to pass arguments into to create Agent
    def __init__(self, environment, agents, neighbourhood, y = None, x = None):
        self.environment = environment
        #Make Agent aware of the other agents
        self.agents = agents
        self.store = 0
        self.neighbourhood = neighbourhood
        if (x == None):
           self._x = random.randint(0,300)
        else:
            self._x = x   
        if (y == None):
            self._y = random.randint(0,300)
        else:
            self._y = y
    
    # Move the agent within the environment
    
    # Agent moves +1 space if less than 0.5 otherwise -1 space
    # % keeps the agents within the environment (300x300)
    
    def move(self):
        #y coordinate
        if random.random() < 0.5:
            self._y = (self._y + 1) % 300
        else:
            self._y = (self._y - 1) % 300
        #x coordinate
        if random.random() < 0.5:
            self._x = (self._x + 1) % 300
        else:
            self._x = (self._x - 1) % 300
    
    # Agent eats from environment if it has more than 10 stores 
    # Agents eat what is left
    
    def eat(self):
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10   
    
    # Agents have neighbours which they share their food stores with if they
    # are in the distance of the neighbourhood. In this case, Agents average
    # out their stores.
    
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            # Calculate the distance between self and the current other agent:
            dist = self.distance_between(agent) 
            if dist <= neighbourhood:
                sum = self.store + agent.store
                # Divide sum by two to calculate average
                ave = sum /2
                self.store = ave
                agent.store = ave
                # print("sharing " + str(dist) + " " + str(ave)) #test
                # print(self.store)
    
    # If Agent reaches store capacity of more than 1000, Agent will vomit 1000
    # of stores
    
    def vomit(self):
        if self.store >=1000:
            self.environment[self.y][self.x] +=1000
            self.store = self.store-1000
    
    # This function finds the distance between row a and row b using 
    # pythagoras theorum while using the agent class
    
    def distance_between(self, agents_row_b):
        return (((self._x - agents_row_b._x)**2) +
                ((self._y - agents_row_b._y)**2))**0.5