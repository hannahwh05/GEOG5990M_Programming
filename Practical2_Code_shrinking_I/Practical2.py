#Practical 2 - Code shrinking I 
#201284811 Hannah Wheldon
#Commented out sections from previous practical for comparison - can be removed

#import libraries/functions/packages at top of code
import random
import operator
import matplotlib.pyplot

#set up container for agents
#remember start 0, 1, 2 etc. 
agents = []
#add agents 1 (y0, x0) and 2 (y1, x1) to container
# random number between 0-99 assigned to each agent on both x and y
agents.append([random.randint(0,99),random.randint(0,99)])
agents.append([random.randint(0,99),random.randint(0,99)])
print ("Agent 1 Coordinates =", agents[0],",", "Agent 2 Coordinates =", agents[1])

#print the agent that is furthest east (larger x number)
print("Agent coordinates furthest to the east =", max(agents, key=operator.itemgetter(1)))

'''
# random number between 0-99 assigned to each agent on both x and y
y0 = random.randint(0,99)
x0 = random.randint(0,99)
y1 = random.randint(0,99)
x1 = random.randint(0,99)

print("Origin of y0 = ",y0,",", "Origin of x0 = ", x0)
print("Origin of y1 = ",y0,",", "Origin of x1 = ", x0)
'''
# 2 Agents set up to move 2 spaces

#Agent 1

# Depending on random number agent moves by 1 step up or down on y axis
# if random number is less than 0.5
# either +1 or -1 

#step 1
#y0 replaced by agents[0][0] and x0 by agents[0][1] below
if random.random() < 0.5:
    #y0 = y0 + 1
    agents[0][0] +=1
else:
    #y0 = y0 - 1
    agents[0][0] -=1
# Depending on random number agent moves by 1 step left or right on x axis
if random.random() < 0.5:
    #x0 = x0 + 1
    agents[0][1] +=1
else:
    #x0 = x0 - 1
    agents[0][1] -=1
#step 2
if random.random() < 0.5:
    #y0 = y0 + 1
    agents[0][0] +=1
else:
    #y0 = y0 - 1
    agents[0][0] -=1
    
if random.random() < 0.5:
    #x0 = x0 + 1
    agents[0][1] +=1
else:
    #x0 = x0 - 1
    agents[0][1] -=1

print("Agents move 2 steps")

#print ("y0 is now =", agents[0][0],",", "x0 is now =", agents[0][1])
print ("Agent 1 is now = ", agents[0])
# add agent 1 to container
#agents.append ([y0, x0])

#Agent 2
    
#step 1
if random.random() < 0.5:
    #y1 = y1 + 1
    agents[1][0] +=1
else:
    #y1 = y1 - 1
    agents[1][0] -=1

if random.random() < 0.5:
    #x1 = x1 + 1
    agents[1][1] +=1
else:
    #x1 = x1 - 1
    agents[1][1] -=1

#step 2
if random.random() < 0.5:
    #y1 = y1 + 1
    agents[1][0] +=1
else:
    #y1 = y1 - 1
    agents[1][0] -=1
if random.random() < 0.5:
    #x1 = x1 + 1
    agents[1][1] +=1
else:
    #x1 = x1 - 1
    agents[1][1] -=1
    
#print ("y1 is now =", agents[1][0],",", "x1 is now =", agents[1][1])
print ("Agent 2 is now = ", agents[1])

'''
#add agent 2 to container
#agents.append ([y1, x1])
'''
print("Agent 1=", agents[0], ",", "Agent 2=", agents[1])

# Calculate distance between Agent 1 (y0, x0) and Agent 2 (y1, x1)
#Pythagoras theorum/euclidean distance
'''
distance = (((y0 - y1)**2) + ((x0 - x1)**2))**0.5
print("The distance between Agent 1 and 2 =", distance)
'''
distance = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
print("The distance between Agent 1 and 2 =", distance)

#Generate scatter plot of randomly generated agents
#limit y and x axes to 0-99
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
#Colour agent 1 red
matplotlib.pyplot.scatter(agents[0][1],agents[0][0], color='red')
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
matplotlib.pyplot.show()
