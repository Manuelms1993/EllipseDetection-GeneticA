def selectionsort(fitnessValues,population):

    tam = len(fitnessValues)
    for i in range(0,tam-1):
        max=i
        for j in range(i+1,tam):
            if fitnessValues[max] < fitnessValues[j]:
                max=j

        aux = fitnessValues[max]
        fitnessValues[max] = fitnessValues[i]
        fitnessValues[i] = aux

        for k in range(len(population[0])-1):
            aux2=population[max][k]
            population[max,k] = population[i,k]
            population[i,k] = aux2

    return fitnessValues,population
