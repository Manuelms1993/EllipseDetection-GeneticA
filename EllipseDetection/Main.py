import ImageFunction as I
import numpy as np
import Ordenation
import GeneticAlgorithm as GA
import matplotlib.pyplot as plt

def printBestFitness(pop):
    e,ellipse,p = GA.getEllipse(pop)
    r = np.zeros((100,100))
    for i in range (m.shape[0]):
        for j in range (m.shape[1]):
            r[i][j]=m[i][j]
    for j in range(len(ellipse)):
        r[ellipse[j][0],ellipse[j][1]]=150
    I.Matrix2Image(r)

def printGraphic(a, b, e):
    plt.figure(num=None, figsize=(40, 8), dpi=60, facecolor='w', edgecolor='k')
    plt.xlabel("Generations")
    plt.ylabel("Fitness")
    plt.title("Fitness Evolution")
    plt.plot(a,'r-',label='Best Fitness',linewidth=2.0)
    plt.plot(b,'b-',label='Fitness Average',linewidth=2.0)
    plt.legend(loc="upper left")
    plt.axis([0,e,0,1])
    plt.show()

mutationPercentage = 15
populationSize = 200
numberOfSelectedIndividuals = 125
generations=100
pltBestFitness = []
pltFitnessAverage = []

I.transformSquareImage('1.png')
m = I.image2Matrix('sample.png')
population = GA.initialize_population(populationSize)
for i in range(generations):
    print "Generation: "+ str(i)
    fitnessvalues = GA.fitness(population,m)
    fitnessvalues,population = Ordenation.selectionsort(fitnessvalues,population)
    print "     Best fitness: "+str(fitnessvalues[0])
    print "     Fitness average: "+str(sum(fitnessvalues)/len(fitnessvalues))
    pltBestFitness.append(fitnessvalues[0])
    pltFitnessAverage.append(sum(fitnessvalues)/len(fitnessvalues))
    population = GA.selection(population,numberOfSelectedIndividuals)
    population = GA.crossover(population,populationSize)
    population = GA.mutation(population,mutationPercentage)

printBestFitness(population[0])
printGraphic(pltBestFitness,pltFitnessAverage,generations)


