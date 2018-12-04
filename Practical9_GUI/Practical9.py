#Practical 9 - GUI/Web Scraping
#201284811 Hannah Wheldon

#Commented out sections from previous practical for comparison - can be removed

#In Spyder set Tools > Preferences > Ipython console > Graphics > Set backend 
# to inline

####################################################
#import libraries/functions/packages at top of code
#import tkinter libraries first
import time
import tkinter
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.backends.backend_tkagg
import matplotlib.pyplot
import matplotlib.animation 
import random
#import agent from separate file
import agentframework5
#import raster data from csv file
import csv
import requests
import bs4
###################################################

#time to run code
#start = time.process_time()

# assign value to variables
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20

#set up container for agents
#remember lists start 0, 1, 2 etc. 


###############################################################################
########## Import environment #########
###############################################################################
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

len(environment)

# Plot environment alone
#matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.show()
###############################################################################



###############################################################################
### Create agents using coordinates from webpage
###############################################################################
#scrape a web page to get the agent starting locations...
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
#print(td_ys)
#print(td_xs)

agents = []
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework5.Agent(environment, agents, y, x))
    
##############################################################################
    
    
    
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])



    '''
    print ("List of original Agent coordinates:")
    agents.append(agentframework5.Agent(i, environment, agents))
    #print all agents coordinates
    print(agents[i])
    '''
# print(len(agents)) - test to see number of agents

#for j in range(num_of_iterations):
#    #for a in agents:
#    #print("Before shuffle:", a) # test to see if agents are shuffling
#    
#    #for a in agents:
#    #print("After shuffle:",a)  # test to see if agents are shuffling
#    for i in range(num_of_agents):
#        agents[i].move()
#        agents[i].eat()
#        agents[i].share_with_neighbours(neighbourhood)    
            
#Make agents using agentframework file to assign random x and y coordinates 
# between 0-99
#print("List of Agent coordinates after move:")
#for i in range(num_of_agents):
#    agents.append(agentframework5.Agent(i, environment, agents))
#    #print all agents coordinates
#    print(agents[i])

#Move the agents
#use the agentframework 

carry_on = True



# animation function        
def update(frame_number):
    
    # clear previous display           
    fig.clear()
    global carry_on
    
    matplotlib.pyplot.ylim(0, 299)
    matplotlib.pyplot.xlim(0, 299)
    
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
    
    
    
    
#condition for when to stop 
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 100) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

#define run to animate plot for GUI interface
def run():
    global animation
    #animation = matplotlib.animation.FuncAnimation(fig, update, interval=1,repeat=False, frames=num_of_iterations)
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.show()
    #matplotlib.pyplot.show()
    
####################################
########## GUI Interface ###########
#use tkinter
    
root = tkinter.Tk() 
root.wm_title("Model")


canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)

########## GUI Interface ###########
####################################

tkinter.mainloop()

#end clock
end = time.process_time()
print("time = " + str(end - start))