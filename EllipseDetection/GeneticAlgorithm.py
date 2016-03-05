import numpy as np
import math
import random
import Bin2Dec

def initialize_population(size):
    population = np.random.rand( *(size,29))
    for i in range(population.shape[0]):
        for j in range(population.shape[1]):
            population[i,j]=round(population[i,j])
    return population

def getEllipse(individual):
    a = Bin2Dec.bin2dec( individual[0:5] ) + 5
    b = Bin2Dec.bin2dec( individual[5:10] ) + 5
    x0 = Bin2Dec.bin2dec( individual[10:16] ) + 19
    y0 = Bin2Dec.bin2dec( individual[16:22] ) + 19
    theta = Bin2Dec.bin2dec(individual[22:29])
    theta *= 179/127
    theta *= 3*math.pi/180

    # Create the representation of ellipse
    ellipse = []
    alpha=0
    while alpha <=  2 * math.pi:
        x = round((a*math.cos(alpha)*math.cos(theta) - b*math.sin(alpha)*math.sin(theta)))+x0
        y = round((a*math.cos(alpha)*math.sin(theta) + b*math.sin(alpha)*math.cos(theta)))+y0
        x = x if (x>-1 and x<=99) else 0
        y = y if (y>-1 and y<=99) else 0
        ellipse.append([x,y])
        alpha+=0.1

    bestEllipse = []
    bestEllipse.append([ellipse[0][0],ellipse[0][1]])
    for i in range(1,len(ellipse)):
        if (ellipse[i][0] != ellipse[i-1][0] and ellipse[i][1] != ellipse[i-1][1]):
            bestEllipse.append([ellipse[i][0],ellipse[i][1]])
    return bestEllipse,ellipse,len(ellipse)

def fitness(population,image):
    fitnessValues = np.zeros(population.shape[0])
    for i in range(population.shape[0]):
        ellipse,ellipse2,nPoints = getEllipse(population[i])
        # Matching with image
        for j in range(len(ellipse)):
            if image[ellipse[j][0],ellipse[j][1]] < 50:
                fitnessValues[i] += 1
        fitnessValues[i] /= nPoints
    return fitnessValues

def selection(population, numberOfSelectedIndividuals=50):
    population = population[0:numberOfSelectedIndividuals,:]
    return population

def crossover(population, populationSize):
    newPopulation = np.zeros((populationSize,29))
    newPopulation[0] = population[0]
    newPopulation[1] = population[1]

    for i in xrange(2,populationSize,2):
        father = population[random.randint(0, len(population)-1)]
        mother = population[random.randint(0, len(population)-1)]
        cut1 = random.randint(0, 28)
        cut2 = random.randint(0, 28)
        if (cut1<cut2): smallindex=cut1; biggerindex=cut2
        else: smallindex=cut2; biggerindex=cut1;

        #Crossover
        newPopulation[i,0:smallindex]=father[0:smallindex]
        newPopulation[i,smallindex:biggerindex]=mother[smallindex:biggerindex]
        newPopulation[i,biggerindex:28]=father[biggerindex:28]
        newPopulation[i+1,0:smallindex]=mother[0:smallindex]
        newPopulation[i+1,smallindex:biggerindex]=father[smallindex:biggerindex]
        newPopulation[i+1,biggerindex:28]=mother[biggerindex:28]

    return newPopulation

def mutation(population, mutationPercentage=5):
    for i in range(2,len(population)):
        if (random.randint(0, 100) <= mutationPercentage):
            gene = random.randint(0, 28)
            value = population[i,gene]
            population[i,gene] = 0 if value==1 else 0

    return population