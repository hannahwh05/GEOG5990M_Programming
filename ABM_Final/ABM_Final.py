'''
Agent Based Model

201284811 Hannah Wheldon
GitHub username: hannahwh05

Version 1.0.0

This model is run from tkinter GUI. 
When this code is run, a window will will appear on the computer screen called
Agent Based Model. To run the model, click "Run model" from the menu bar in 
this window.

***Link to point below
    #n.b. to run model with random coordinates instead of scraping from webpage,
    # remove 3rd and 4th arguements above i.e. y, x

In Spyder set Tools > Preferences > Ipython console > Graphics > Set backend 
to inline

use agentframework.py for agent parameters
'''

###############################################################################
################################# Import ######################################

'''import libraries/functions/packages at top of code'''

#2D plotting library
import matplotlib
import matplotlib.pyplot
#animate plot
import matplotlib.animation
#framework to build tkinter graphics interface
import tkinter
matplotlib.use('TkAgg')
#tkinter backend
import matplotlib.backends.backend_tkagg
#pseudo-random number generator
import random
#imports agent from separate coded file to prevent repetition
import agentframework
#imports raster data from csv file
import csv
#request information from HTML
import requests
#pulls data from HTML (beautiful soup 4)
import bs4
from PIL import ImageGrab
###############################################################################

'''assign value to variables'''

num_of_agents = 25
neighbourhood = 75

###############################################################################
############################ Import environment ###############################
###############################################################################

'''read in raster data from csv'''

f = open('in.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

#set up environment container to read data into
environment = []
for row in reader:
    #set up row container	
    rowlist = []		
    for value in row:
        #append values from rows in csv file to rowlist
        rowlist.append(value)
    #append rowlist values from for loop into environment container
    environment.append(rowlist)

#Close the reader    				
f.close()

#len(environment) # test to see size of environment based on csv file

#test to see environment alone
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()
###############################################################################




###############################################################################
############### Create agents using coordinates from webpage ##################
###############################################################################
#scrape a web page to get the agent starting locations
# beautiful soup 4 pulls data from html
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/'
                 'python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
#read in y and x classes
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
#print(td_ys) #test to see y coordinates are read in
#print(td_xs) #test to see x coordinates are read in

###############################################################################

#set up container for agents
agents = []

'''for loop to append y and x classes read in above to each agents 
y and x coordinates'''

for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, agents))
    #n.b. to run model with random coordinates instead of scraping from webpage,
    # remove 3rd and 4th arguements above i.e. y, x
    
#set up figure size and axes
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

carry_on = True

def update(frame_number):
    """ hkm
    
    """
    
    #clear previous display           
    fig.clear()
    #create global variable to modify local variable outside of function
    global carry_on
    
    #make plot 300 x 300 due to size of environment
    matplotlib.pyplot.ylim(300, 0)
    matplotlib.pyplot.xlim(0, 300)
    

    #random.shuffle(agents)

    #for each agent - move, eat and share with neighbours 
    for i in range(num_of_agents):
        #agents randomly move around environment
        agents[i].move()
        #print(agents[i]) #test to check they have moved
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        agents[i].vomit()
        #for loop to plot all agents generated
        
    #plot environment and set minimum and maximum limits
    matplotlib.pyplot.imshow(environment, vmin = 0, vmax= 300)
        
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i]._x, agents[i]._y)
    
    #if random move is less than 0.01 stopping condition is met     
    if random.random() < 0.01:
        carry_on = False
        print("stopping condition")    
    
#generator function to set condition for when to stop 
def gen_function(b = [0]):
    a = 0
    global carry_on
    #a = number of iterations
    while (a < 100) & (carry_on) :
        #function returns generator
        yield a			
        a = a + 1

#define run for model to animate plot for GUI interface
def run():
    global animation
    animation = matplotlib.animation.FuncAnimation(fig, update, 
                frames=gen_function, repeat=False)
    canvas.show()
    
###############################################################################
########################## GUI Interface ######################################

#use tkinter to make GUI interface and widgets
root = tkinter.Tk() 
root.wm_title("Agent Based Model")

canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model Menu", menu=model_menu)
model_menu.add_command(label="Run model", command=run)
model_menu.add_command(label="Close", command=root.destroy)

#model_menu.add_command(label="Save as...", command=ImageGrab.grab.save('ABM.jpg'))

tkinter.mainloop()


###############################################################################

print("***Thank you for running the model***")

