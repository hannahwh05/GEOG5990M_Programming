#Practical 7 - Communication
#201284811 Hannah Wheldon
#Commented out sections from previous practical for comparison - can be removed

#import libraries/functions/packages at top of code
import matplotlib.pyplot
import time
import random
#import agent from separate file
import agentframework3

import csv

#time to run code
start = time.clock()

num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20

#set up container for agents
#remember start 0, 1, 2 etc. 
agents = []

#############################################
########## Import environment #########
#############################################
#read in raster data
f = open('in.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

environment = []
for row in reader:	
	
    rowlist = []		
    for value in row:
        rowlist.append(value)
    
    environment.append(rowlist)

#Close the reader    				
f.close()

# Plot environment alone
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()

#############################################

print ("List of original Agent coordinates:")
for i in range(num_of_agents):
    agents.append(agentframework3.Agent(i, environment, agents))
    #print all agents coordinates
    print(agents[i])

# print(len(agents)) - test to see number of agents

for j in range(num_of_iterations):
    #for a in agents:
    #print("Before shuffle:", a) # test to see if agents are shuffling
    random.shuffle(agents)
    #for a in agents:
    #print("After shuffle:",a)  # test to see if agents are shuffling
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)    
            
#Make agents using agentframework file to assign random x and y coordinates between 0-99
print("List of Agent coordinates after move:")
for i in range(num_of_agents):
    agents.append(agentframework3.Agent(i, environment, agents))
    #print all agents coordinates
    print(agents[i])

#Move the agents
#use the agentframework 
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        #print(agents[i])
        agents[i].move()
        #print(agents[i]) #Test to check move.
        agents[i].eat()
        
   
#Generate scatter plot of randomly generated agents
#limit y and x axes to 0-99
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.imshow(environment)
#for loop to plot all agents generated
for i in range(num_of_agents):
    #matplotlib.pyplot.scatter(agents[i][1], agents[i][0])
    matplotlib.pyplot.scatter(agents[i]._x, agents[i]._y)
matplotlib.pyplot.show()

#Pythagoras theorum/euclidean distance
#distance = distance_between(agents[0], agents[1])

'''
#distance between agents
print("Every distance between each set of coordinates")
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
        #print(distance) #test to check distances
        a = agentframework3.Agent(i, environment, agents)
#print(a._y, a._x)
'''
#end clock
end = time.clock()
print("time = " + str(end - start))