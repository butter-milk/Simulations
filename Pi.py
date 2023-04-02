from random import random
import numpy as np
import matplotlib.pyplot as plt

def simulate(n:int)->None:
    #Collect data to approximate pi and plot visualization.
    correct = 0
    data= np.empty((n,2),float)
    circ = np.empty((n,2),float)
    for i in range(n):
        x=random()
        y=random()
        if x**2+y**2 <=1:
            correct +=1
            circ[i,:] = [x,y]
        else:
            data[i,:] = [x,y]
    plt.figure()
    plt.title("Estimate of pi:"+ str(4*correct/n))
    plt.plot(circ[:,0],circ[:,1], '.', color="red")
    plt.plot(data[:,0],data[:,1], '.', color="blue")
    plt.show()

simulate(10000)