'''
Agent Based Model

201284811 Hannah Wheldon
GitHub username: hannahwh05

Version 1.0.0

This model is run from tkinter GUI. 
When this code is run, a window will will appear on the computer screen called
Agent Based Model. To run the model, click "Run model" from the menu bar in 
this window.

In Spyder set Tools > Preferences > Ipython console > Graphics > Set backend 
to inline

use agentframework.py for agent parameters
'''

###############################################################################
################################# Import ######################################
#import libraries/functions/packages at top of code
#import tkinter libraries first
import tkinter
#2D plotting library
import matplotlib
#framework to build tkinter graphics interface
matplotlib.use('TkAgg')
#tkinter backend
import matplotlib.backends.backend_tkagg
import matplotlib.pyplot
import matplotlib.animation 
#pseudo-random number generator
import random
#import agent from separate file
import agentframework
#import raster data from csv file
import csv
import requests
import bs4
###############################################################################


# assign value to variables
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20

###############################################################################
############################ Import environment ###############################
###############################################################################
#read in raster data from csv
f = open('in.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

#set up environment container ti read data into
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
#matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.show()
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
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
#print(td_ys) #test to see all y coordinates
#print(td_xs) #test to see all x coordinates

###############################################################################


#set up container for agents
agents = []

for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, agents, y, x))
    #n.b. to run model with random coordinates instead of scraping from webpage,
    # remove 3rd and 4th arguements above i.e. y, x
    
#set up figure size and axes
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

carry_on = True

# animation function        
def update(frame_number):
    
    # clear previous display           
    fig.clear()
    global carry_on
    
    matplotlib.pyplot.ylim(0, 300)
    matplotlib.pyplot.xlim(0, 300)
    
    # plot environemnt 
    matplotlib.pyplot.imshow(environment)
    
    
    # for each agent - move and eat
    for i in range(num_of_agents):
        
        random.shuffle(agents)
        
        #print(agents[i])
        agents[i].move()
        #print(agents[i]) #Test to check move.
        agents[i].eat()
        
        agents[i].share_with_neighbours(neighbourhood)  
  
    
    #for loop to plot all agents generated
    for i in range(num_of_agents):
        #matplotlib.pyplot.scatter(agents[i][1], agents[i][0])
        matplotlib.pyplot.scatter(agents[i]._x, agents[i]._y)
        
        
        
    if random.random() < 0.01:
        carry_on = False
        print("stopping condition")
    
    # for each agent - plot it
    #Generate scatter plot of randomly generated agents
    #limit y and x axes to 0-99
    

#set condition for when to stop 
def gen_function(b = [0]):
    a = 0
    global carry_on
    while (a < 100) & (carry_on) :
        # Returns control and waits next call.
        yield a			
        a = a + 1

#define run to animate plot for GUI interface
def run():
    global animation
    animation = matplotlib.animation.FuncAnimation(fig, update, 
                frames=gen_function, repeat=False)
    canvas.show()
    #matplotlib.pyplot.show()
    
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
menu_bar.add_cascade(label="Menu", menu=model_menu)
model_menu.add_command(label="Run model", command=run)

tkinter.mainloop()
###############################################################################

print("Thank you for running the Model")