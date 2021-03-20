#!/usr/bin/env python
# coding: utf-8

# # Monty Hall simulation for *n* doors

# Suppose you're on a game show, and you're given the choice of n doors: Behind one door is a car; behind the others, goats. 
# You pick a door, say No. k, and the host, who knows what's behind the doors, opens opens *n-2* losing doors and then offers the player 
# the opportunity to switch. Is it to your advantage to switch your choice?

# In[1]:


# Import packages
import matplotlib.pyplot as plt
import numpy as np
import random


# In[2]:


N = 100000                                            # Number of simulations
n = 3                                                 # Total number of doors


# In[3]:


def montyHall(N,n):
    
    count1 = 0                                        # Set count for not switching
    count2 = 0                                        # Set count for switching

    for i in range(N):                                # For N simulations

        doors       = list(range(1,n+1))              # Create list of n doors
        car         = random.choice(doors)            # Door with the car
        choice1     = random.choice(doors)            # First guess of participant

        # Switch doors out of remaining two doors
        if car == choice1:
            doors.remove(car)
            choice2 = random.choice(doors)
        else:
            choice2 = car    

        if car == choice1:                            # Check whether correct door is chosen when not switching
            count1 += 1  
        elif car == choice2:                          # Check whether correct door is chosen when switching
            count2 += 1

    return count1/N, count2/N 


# In[4]:


print('Experimental probability of winning the car when not switching doors is', montyHall(N,n)[0])
print('Theoretical probability of winning the car when not switching doors is', 1/n, '\n')

print('Experimental probability of winning the car when switching doors is', montyHall(N,n)[1])
print('Theoretical probability of winning the car when switching doors is', (n-1)/n)


# In[5]:


N = 10000                                             # Number of simulations
n = 50                                                # Total number of doors

# Create empty arrays for storing probabilities
prob_switching    = np.zeros(n-2)
prob_no_switching = np.zeros(n-2)

# Fill arrays with probabillities
for i in range(2,n):
    prob_no_switching[i-2] = montyHall(N,i)[0]
    prob_switching[i-2]    = montyHall(N,i)[1]

totalDoors = np.linspace(2,n,n-2)    


# In[6]:


# Plot
fig = plt.figure(figsize = (9,4))
plt.plot(totalDoors, prob_switching, label='Switching', color='r');
plt.plot(totalDoors, prob_no_switching,label='No switching', color='b');
plt.xlim([2, n]);
plt.ylim([-0.05, 1.05]);
plt.ylabel('Probability of winning', fontsize = 14);
plt.xlabel('Number of doors', fontsize = 14);
plt.legend(fontsize = 10);
plt.hlines(1,2,50, linestyle = 'dashed');
plt.hlines(0,2,50, linestyle = 'dashed');


# In[ ]:




