#Imports modules needed for Agent class.
import random 
import time 


#Sets up run time check for agentsframework.py.
start=time.time()


#Functions for agents to access data, move, eat and workout distances between eachother.
class Agent():
    
    def __init__ (self,environment,agents,y,x):
        
            self.y = y
            self.x = x
            self.environment = environment
            self.store = 0
            self.agents = agents
            
    def move (self):
        if random.random() < 0.5:
           self.y = (self.y + 1) % 100
        else:
           self.y = (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
        
    
    def eat (self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10

#Calculates distance to each of the other agents, and if they fall within neighbourhood distance,
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent) 
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
                #print("sharing " + str(dist) + " " + str(ave)) #To check that its working.

    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
end=time.time()

total = end-start
print("agentframework.py run time: ", total, "seconds")

