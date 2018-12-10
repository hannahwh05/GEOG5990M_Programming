'''
Agent Framework for ABM_Final

201284811 Hannah Wheldon
Version 1.0.0
'''

#pseudo-random number generator
import random

'''Create a new type of object with attributes attached
    Create own functions, using 'def'''
class Agent (object):
    #Constructor to pass agruments into to create Agent
    #Number of arguments must be 4 so y and x must = None
    def __init__(self, environment, agents, y = None, x = None):
        self.environment = environment
        #Make Agent aware of the other agents
        self.agents = agents
        self.store = 0
        if (x == None):
           self._x = random.randint(0,300)
        else:
            self._x = x   
        if (y == None):
            self._y = random.randint(0,300)
        else:
            self._y = y
    
    #Move the agent 
    #Agent moves +1 space if less than 0.5 otherwise -1 space
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
    
    #Agent eats from environment
    #Agents eat what is left
    def eat(self):
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10   
    
    #Loop through the agents in self.agents
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            #Calculate the distance between self and the current other agent:
            dist = self.distance_between(agent) 
            #If distance is less than or equal to the neighbourhood
            if dist <= neighbourhood:
                #Sum is self.store plus agent.store
                sum = self.store + agent.store
                #Divide sum by two to calculate average
                ave = sum /2
                self.store = ave
                agent.store = ave
                #print("sharing " + str(dist) + " " + str(ave)) #test it is working
                #print(self.store)
    
    
    #this function finds the distance between row a and row b using 
    #pythadoras theorum while using the agent class
    def distance_between(self, agents_row_b):
        return (((self._x - agents_row_b._x)**2) +
                ((self._y - agents_row_b._y)**2))**0.5