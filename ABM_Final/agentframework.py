'''
GEOG5990M Programming for Geographical Information Analysis: Core Skills
Agent Framework for ABM_Final

This file contains the code for the Agent class. This is imported into the
ABM_Final code. 

201284811 Hannah Wheldon
GitHub username: hannahwh05

Version 1.0.0
'''

# pseudo-random number generator
import random

# Defining Agent class through movement, eating, sharing and vomiting 
# in the environment

# Create a new type of object with attributes attached
    # Create own functions, using 'def'
    
class Agent():
    """
    Agent class:
    A class to show the behaviour of an abstract agent, e.g. a sheep, 
    interacting with an environment.
    Agent characteristics:
        - store
        - x-coordinate
        - y-coordinate
    Agent behaviours include:
        - move
        - eat
        - share with neighbours
        - vomit
    """
    # Constructor to pass arguments into to create Agent
    def __init__(self, env, agents, x=None, y=None):
        """
        Constructor takes arguments:
        env -- a list (environment) of lists (rowlists), imported from a csv 
               file, creating the 2D landscape in which the agent exists.
        agents -- all the agents in the environment.
        x -- the x axis coordinate.
        y -- the y axis coordinate.
        """
        self.environment = env
        #Make Agent aware of the other agents
        self.agents = agents
        self.store = 0
        self._envWidth = len(env) 
        self._envHeight = len(env[0])
        self._x = random.randint(0, self._envWidth)
        self._y = random.randint(0, self._envHeight)


    def move(self):
        """
        Movement of agent within the environment.
        Agent moves along x and y axis dependent on a random number generated.
        Moves +1 space if random number is less than 0.5, otherwise -1 
        space if more than 0.5 (random number is between 0.0-1.0).
        "%" operator keeps the agents within the environment.       
        """
        # Move x
        if random.random() < 0.5:
            self._x = (self._x + 1) % self._envWidth
        else:
            self._x = (self._x - 1) % self._envWidth
        # Move y
        if random.random() < 0.5:
            self._y = (self._y + 1) % self._envHeight
        else:
            self._y = (self._y - 1) % self._envHeight
        
     
    def eat(self):
        """
        Eating habit of agent.
        Agent eats 10 "stores" from environment if it has more than 10.
        """
        if self.environment[self._x][self._y] > 10:
            self.environment[self._x][self._y] -= 10
            self.store += 10   
    
    
    def share_with_neighbours(self, neighbourhood):
        """
        Agents have neighbours which they share their food stores with if they
        are in the distance of the neighbourhood. In this case, agents average
        out their stores.
        neighbourhood -- the distance at which an agent will share with another
        """
        for agent in self.agents:
            # Calculate the distance between self and the current other agent:
            dist = self.distance_between(agent) 
            if dist <= neighbourhood:
                sum = self.store + agent.store
                # Divide sum by two to calculate average
                ave = sum /2
                self.store = ave
                agent.store = ave
                #print("sharing " + str(dist) + " " + str(ave)) #test
                #print(self.store)
    
    
    def vomit(self):
        """
        Agent vomits if it reaches store capacity of 255 (maximum value of the 
        environment.
        """
        if self.store >=255:
            self.environment[self._x][self._y] +=255
            self.store -=255
            #print("vomited here") # test to see if vomited
    
    
    def distance_between(self, agents_row_b):
        """
        Returns the distance between row a and row b using Pythagoras theorum.
        """
        return (((self._x - agents_row_b._x)**2) +
                ((self._y - agents_row_b._y)**2))**0.5