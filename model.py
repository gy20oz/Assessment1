# Imports modules required for the ABM Model.
import matplotlib
import tkinter
matplotlib.use('TkAgg')
import time 
import matplotlib.pyplot
import agentframework
import csv
import random
import matplotlib.animation
import requests
import bs4

#Sets up time for web scraping time checks.
T1=time.time()

#Downloads data from website a produces X and Y Lists.
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})

#To check web scraping has been completed.
#print(td_ys)
#print(td_xs)


#Close time for web scraping time checks.
T2=time.time()

#Web Scraping time checks.
Webtime = T2-T1
print("Web scraping run time: ", Webtime, "seconds")


#Model run function to link to GUI menu.
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()


#Sets up model figure.
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


#Produces Model GUI window using Tkinter and links model menu to run command set up previously.
root = tkinter.Tk() 
root.wm_title("Model")
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


#Sets up time for model running time checks.
T3=time.time()


#Sets up model parameters with user input for integers only otherwise error will show.
num_of_agents = int(input("How many agents would you like?"))
num_of_iterations = 100
neighbourhood = 20

#Creates new empty lists for environment and agents.
environment = []
agents = []

#Model stop function.
carry_on = True	
ax.set_autoscale_on(True)

# Sets up animation.
def update(frame_number):
    

    fig.clear()  
    global carry_on
    
    
    #Reads in the data file with environment data.
    f = open("in.txt",newline='') # Opens file in.txt.
    reader=csv.reader(f,quoting=csv.QUOTE_NONNUMERIC) #Reader
    for row in reader: #list of rows
        rowlist = []
        environment.append(rowlist)
        for value in row: #list of values.
            rowlist.append(value)
    #f.close() #Closes in.txt file after processing.
    
    # Sets up agents with environment data,y and x.
    for i in range(num_of_agents):
         y = int(td_ys[i].text)
         x = int(td_xs[i].text)
         agents.append(agentframework.Agent(environment,agents,y,x))
          
    
    #Agent random walk,eat,share using loop.
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
                random.shuffle(agents)
                agents[i].move()
                agents[i].eat()
                agents[i].share_with_neighbours(neighbourhood)
            
    
    #Random stop model for model.         
    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")        
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
       matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        
#Agent storage stop (non-functional)
def gen_function(b = [0]):
    a = environment.store
    global carry_on
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1


# Shows animation plot produced from above code.
matplotlib.pyplot.show()


T4=time.time()


#Model time checks.
Modeltime = T4-T3
print("Model run time: ", Modeltime, "seconds")


tkinter.mainloop()



