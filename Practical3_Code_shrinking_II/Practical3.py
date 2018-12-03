#Practical 3 - Code shrinking II
#201284811 Hannah Wheldon
#Commented out sections from previous practical for comparison - can be removed

#import libraries/functions/packages at top of code
import random
import matplotlib.pyplot

num_of_agents = 10
num_of_iterations = 100

#set up container for agents
#remember start 0, 1, 2 etc. 
agents = []
#add agents 1 (y0, x0) and 2 (y1, x1) to container
# random number between 0-99 assigned to each agent on both x and y
'''
agents.append([random.randint(0,99),random.randint(0,99)])
agents.append([random.randint(0,99),random.randint(0,99)])
'''
#Give each agent (num_of_agents = 10) y and x coordinates between 0 and 100
print("List of Agent Coordinates:")
for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])
    #print all agents coordinates
    print(agents[i])

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        #y coordinate
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100
        #x coordinate
        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100


#torus - to allow agents leaving the top of area to come in at the bottom 
# and leaving left to come in on right
if random.random() < 0.5:
    agents[i][0] = (agents[i][0] + 1) % 100
else:
    agents[i][0] = (agents[i][0] - 1) % 100
#print new set of coordinates
print("New List of Agent Coordinates:")
for i in range(num_of_agents):   
    print(agents[i])
     
'''
print ("Agent 1 Coordinates =", agents[0],",", "Agent 2 Coordinates =", agents[1])

#print the agent that is furthest east (larger x number)
print("Agent coordinates furthest to the east =", max(agents, key=operator.itemgetter(1)))

# 2 Agents set up to move 2 spaces

#Agent 1

# Depending on random number agent moves by 1 step up or down on y axis
# if random number is less than 0.5
# either +1 or -1 

#step 1
if random.random() < 0.5:
    agents[0][0] +=1
else:
    agents[0][0] -=1
# Depending on random number agent moves by 1 step left or right on x axis
if random.random() < 0.5:
    agents[0][1] +=1
else:
    agents[0][1] -=1
#step 2
if random.random() < 0.5:
    agents[0][0] +=1
else:
    agents[0][0] -=1
    
if random.random() < 0.5:
    agents[0][1] +=1
else:
    agents[0][1] -=1

print("Agents move 2 steps")

print ("Agent 1 is now = ", agents[0])

#Agent 2
    
#step 1
if random.random() < 0.5:
    agents[1][0] +=1
else:
    agents[1][0] -=1

if random.random() < 0.5:
    agents[1][1] +=1
else:
    agents[1][1] -=1

#step 2
if random.random() < 0.5:
    agents[1][0] +=1
else:
    agents[1][0] -=1
if random.random() < 0.5:
    agents[1][1] +=1
else:
    agents[1][1] -=1
    
print ("Agent 2 is now = ", agents[1])

print("Agent 1=", agents[0], ",", "Agent 2=", agents[1])
'''

# Calculate distance between Agent 1 (y0, x0) and Agent 2 (y1, x1)
#Pythagoras theorum/euclidean distance

#distance = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
#print("The distance between Agent 1 and 2 =", distance)

#Generate scatter plot of randomly generated agents
#limit y and x axes to 0-99
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
#for loop to plot all agents generated
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1], agents[i][0])
matplotlib.pyplot.show()

#Colour agent 1 red
#matplotlib.pyplot.scatter(agents[0][1],agents[0][0], color='red')
#matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
