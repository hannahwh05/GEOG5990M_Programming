#Practical 9 - GUI - Agent Framework
#201284811 Hannah Wheldon
#Commented out sections from previous practical for comparison - can be removed

import random

class Agent (object):
    def __init__(self,random_seed,environment, agents):
       random.seed(random_seed)
       self.environment = environment
       #Make Agent aware of the other agents
       self.agents = agents
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
    
    #Agent eats from environment
    #Agents eat what is left
    def eat(self):
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10   
    
    # Loop through the agents in self.agents
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            # Calculate the distance between self and the current other agent:
            dist = self.distance_between(agent) 
            # If distance is less than or equal to the neighbourhood
            if dist <= neighbourhood:
                # Sum self.store and agent.store
                sum = self.store + agent.store
                # Divide sum by two to calculate average.
                ave = sum /2
                self.store = ave
                agent.store = ave
                #print("sharing " + str(dist) + " " + str(ave)) #test it is working
                #print(self.store)
    
    #define what distance_between is i.e. pythagoras theorum
    def distance_between(self, agents_row_b):
        return (((self._x - agents_row_b._x)**2) +
                ((self._y - agents_row_b._y)**2))**0.5

