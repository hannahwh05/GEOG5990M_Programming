'''
GEOG5990M Programming for Geographical Information Analysis: Core Skills
Agent Based Model

201284811 Hannah Wheldon
GitHub username: hannahwh05

Version 1.0.0

This model is run from tkinter GUI. 
When this code is run, a window will will appear on the computer screen called
Agent Based Model. To run the model, click "Run" from the "Menu" in this 
window. When the model has met the "stopping condition", close the window and
the figure will be printed to the console. 

n.b. to run model with random coordinates instead of scraping from webpage, 
remove 3rd and 4th arguements i.e. y, x in Step 4.

In Spyder set Tools > Preferences > Ipython console > Graphics > Set backend 
to inline

Use agentframework.py for agent class
'''

###############################################################################
################################# Import ######################################
###############################################################################
'''import libraries/functions/packages at top of code'''

#2D plotting library
import matplotlib
import matplotlib.pyplot as plot
#animate plot
import matplotlib.animation as ani
#framework to build tkinter graphics interface
import tkinter
matplotlib.use('TkAgg')
#tkinter backend
import matplotlib.backends.backend_tkagg
#imports agent from separate coded file to prevent repetition
import agentframework
#imports raster data from csv file
import csv
#request information from HTML
import requests
#pulls data from HTML (beautiful soup 4)
import bs4

###############################################################################
####################'''Step 1: Assign value to variables'''####################
###############################################################################

num_of_agents = 25
neighbourhood = 75

###############################################################################
#######################'''Step 2: Import environment'''########################
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

#len(env) # test to see size of environment based on csv file

#test to see environment alone
plot.imshow(environment)
plot.show()

###############################################################################
###########'''Step 3: Create agents using coordinates from webpage'''##########
###############################################################################
'''scrape a web page to get the agent starting locations'''

# beautiful soup 4 pulls data from html
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/'
                 'python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
#read in y and x classes
td_xs = soup.find_all(attrs={"class" : "x"})
td_ys = soup.find_all(attrs={"class" : "y"})
#print(td_xs) #test to see x coordinates are read in
#print(td_ys) #test to see y coordinates are read in

###############################################################################
##########################'''Step 4: Plot agents'''############################
###############################################################################

# set up container for agents
agents = []

# for loop to append x and y classes, read in above, to each agent
for i in range(num_of_agents):
    x = int(td_xs[i].text)
    y = int(td_ys[i].text)
    agents.append(agentframework.Agent(environment, agents, x, y))
    #n.b. to run model with random coordinates, instead of scraping from 
    # webpage, remove 3rd and 4th arguements above i.e. x, y
    
# set up figure size and axes
fig = matplotlib.pyplot.figure(figsize=(8, 8))
ax = fig.add_axes([0, 0, 1, 1])

carry_on = True

def update(frame_number):
    """
    Updates the display in the animation:
    Plot axes based on size of environment.
    Agents move, eat, share with neighbours and vomit.
    """
    #clear previous display           
    fig.clear()
    #create global variable to modify local variable outside of function
    global carry_on
    
    #make plot based on size of environment
    plot.xlim(0, len(environment))
    plot.ylim(0, len(environment[0]))

    #for each agent - move, eat, share with neighbours and vomit 
    for i in range(num_of_agents):
        #agents randomly move around environment
        agents[i].move()
        #print(agents[i]) #test to check they have moved
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        agents[i].vomit()
        #for loop to plot all agents generated
        
    #plot environment and set minimum and maximum limits based on environment
    # values to prevent scaling of colour when model runs
    plot.imshow(environment, vmin = 92, vmax= 255)
        
    for i in range(num_of_agents):
        plot.scatter(agents[i]._x, agents[i]._y)
  
###############################################################################
######################'''Step 4: Stopping condition'''#########################
###############################################################################

# generator function to set condition for when to stop 
def gen_function(b = [0]):
    """A stopping function for the animation"""
    a = 0
    global carry_on
    while (a < 100) & (carry_on):
        #function returns generator
        yield a			
        a = a + 1
    print("stopping condition")
    
###############################################################################
#########################'''Step 5: Run the model'''###########################
############################################################################### 

def run():
    """ Run model to animate plot for GUI interface"""
    global animation
    animation = ani.FuncAnimation(fig, update, 
                frames=gen_function, repeat=False)
    canvas.show()
    
###############################################################################
#########################'''Step 6: GUI Interface'''###########################
###############################################################################
'''use tkinter to make GUI interface and widgets'''

root = tkinter.Tk() 
root.wm_title("Agent Based Model")

canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Menu", menu=model_menu)
model_menu.add_command(label="Run", command=run)
model_menu.add_command(label="Close", command=root.destroy)

tkinter.mainloop()

###############################################################################

print("***Thank you for running the model***")
