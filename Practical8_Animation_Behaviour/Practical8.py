#Practical 8 - Animation / Behaviour
#201284811 Hannah Wheldon
#Commented out sections from previous practical for comparison - can be removed

#import libraries/functions/packages at top of code
import matplotlib.pyplot
import matplotlib.animation 
import time
import random
#import agent from separate file
import agentframework4

import csv

#time to run code
start = time.clock()

num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20

#set up container for agents
#remember start 0, 1, 2 etc. 
agents = []

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

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
    agents.append(agentframework4.Agent(i, environment, agents))
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
    agents.append(agentframework4.Agent(i, environment, agents))
    #print all agents coordinates
    print(agents[i])

#Move the agents
#use the agentframework 

carry_on = True
        
def update(frame_number):
    
    # clear previous display           
    fig.clear()
    global carry_on
    
    # for each agent - move and eat
    for i in range(num_of_agents):
        #print(agents[i])
        agents[i].move()
        #print(agents[i]) #Test to check move.
        agents[i].eat()
    
    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")
    
    # for each agent - plot it
    #Generate scatter plot of randomly generated agents
    #limit y and x axes to 0-99
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.imshow(environment)
    #for loop to plot all agents generated
    for i in range(num_of_agents):
        #matplotlib.pyplot.scatter(agents[i][1], agents[i][0])
        matplotlib.pyplot.scatter(agents[i]._x, agents[i]._y)

def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1


#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1,repeat=False, frames=num_of_iterations)
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)

matplotlib.pyplot.show()

#end clock
end = time.clock()
print("time = " + str(end - start))