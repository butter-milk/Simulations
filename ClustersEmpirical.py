from random import random,randint
import numpy as np
import matplotlib.pyplot as plt

cluster1 = [(90+40*np.cos(random()),90+40*np.sin(random())) for _ in range(1000)]
cluster2 = [(10+6*np.cos(random()),10+6*np.sin(random())) for _ in range(1000)]

noise = [(x*random()*20,x*random()*20) for x in range(10)]
DATA = list()
DATA.extend(cluster1)
DATA.extend(cluster2)
DATA.extend(noise)


def sample(percentage,data):
    #Sample uniformly
    Sample = []
    for d in data:
        if len(Sample) < int(percentage* float(len(data))):
            Sample.append(d)
        else:
            if random() < float(len(Sample))/(float(data.index(d))):
                Sample[randint(0,len(Sample)-1)] = d
    return Sample


def distance(x,y):
    #Euclidean distance
    return np.sqrt((x[0]-y[0])**2+(x[1]-y[1])**2)


def dMatrix(sample:list) -> list:
    #Make distance matrix
    d=[[0 for _ in range(len(sample)) ] for _ in range(len(sample))] 
    for i in range(len(sample)):
        for j in range(int(len(sample)/2) + 1):
            x = distance(sample[i],sample[j])
            d[i][j] = x
            d[j][i] = x
    return d

def Pdistribution(dist: list) -> tuple:
    #returns probabilistic distribution
    max = np.amax([np.amax(x) for x in dist])
    
    return list(map(lambda x: max - np.mean(x), dist)),max


def analyze(dataPoint: tuple, sample: list, Pdist:list, alpha:float, max:float):
    #Returns whether dataPoint is outlier, with confidence 1-alpha
    distances = list(map(lambda x: distance(dataPoint, x), sample))
    
    if max - np.amax(distances) <0:
        return 1
    s = sum(list(map(lambda x: max - np.mean(distances) > x, Pdist )))
    if float(s)/float(len(sample)) < alpha:
        return 1
    return 0


sampleset = sample(0.01, DATA)
distanceMatrix = dMatrix(sampleset)
probDist, MAX = Pdistribution(distanceMatrix)
outliers = [dataP for dataP in DATA if analyze(dataP,sampleset, probDist,0.05,MAX)]
           

plt.figure()
plt.plot(list(map(lambda x: x[0], noise)),list(map(lambda x: x[1], noise)), ".", c="red")
plt.plot(list(map(lambda x: x[0], cluster1)),list(map(lambda x: x[1], cluster1)), ".", c="blue")
plt.plot(list(map(lambda x: x[0], cluster2)),list(map(lambda x: x[1], cluster2)), ".", c="blue")
plt.plot(list(map(lambda x: x[0], outliers)),list(map(lambda x: x[1], outliers)), ".", c="green")
plt.show()


