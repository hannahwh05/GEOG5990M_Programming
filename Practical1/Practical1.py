#Practical 1 - Agent Based Modelling
#201284811 Hannah Wheldon

#print("hello world")

#import random library
import random

#set up agents
y0, x0, y1, x1 = 50, 50, 50, 50
print("Origin of y0 = ",y0,",", "Origin of x0 = ", x0)
print("Origin of y1 = ",y0,",", "Origin of x1 = ", x0)

# 2 Agents set up to move 2 spaces

#Agent 1

# Depending on random number agent moves by 1 step up or down on y axis
# if random number is less than 0.5
# either +1 or -1 

#step 1
if random.random() < 0.5:
    y0 = y0 + 1
else:
    y0 = y0 - 1

# Depending on random number agent moves by 1 step left or right on x axis
if random.random() < 0.5:
    x0 = x0 + 1
else:
    x0 = x0 - 1

#step 2
if random.random() < 0.5:
    y0 = y0 + 1
else:
    y0 = y0 - 1

if random.random() < 0.5:
    x0 = x0 + 1
else:
    x0 = x0 - 1
print ("y0 is now =", y0,",", "x0 is now =", x0)

#Agent 2
    
#step 1
if random.random() < 0.5:
    y1 = y1 + 1
else:
    y1 = y1 - 1

if random.random() < 0.5:
    x1 = x1 + 1
else:
    x1 = x1 - 1

#step 2
if random.random() < 0.5:
    y1 = y1 + 1
else:
    y1 = y1 - 1

if random.random() < 0.5:
    x1 = x1 + 1
else:
    x1 = x1 - 1
print ("y1 is now =", y1,",", "x1 is now =", x1)

# Calculate distance between Agent 1 (y0, x0) and Agent 2 (y1, x1)
#Pythagoras theorum/euclidean distance
distance = (((y0 - y1)**2) + ((x0 - x1)**2))**0.5
print("The distance between Agent 1 and 2 =", distance)
