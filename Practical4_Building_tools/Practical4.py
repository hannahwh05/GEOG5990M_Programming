#Practical 4 - Building tools
#201284811 Hannah Wheldon
#Commented out sections from previous practical for comparison - can be removed

#import libraries/functions/packages at top of code
import random
import matplotlib.pyplot
import time

#time to run code
start = time.clock()

#define what distance_between is i.e. pythagoras theorum
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5

num_of_agents = 10
num_of_iterations = 100

#set up container for agents
#remember start 0, 1, 2 etc. 
agents = []

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
      
#Generate scatter plot of randomly generated agents
#limit y and x axes to 0-99
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
#for loop to plot all agents generated
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1], agents[i][0])
matplotlib.pyplot.show()

#Pythagoras theorum/euclidean distance
# agents[0]=agents_row_a, agents[1]=agents_row_b
distance = distance_between(agents[0], agents[1])

#distance between agents
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
        print("Distance between 2 coordinates:", distance)

end = time.clock()
print("time = " + str(end - start))