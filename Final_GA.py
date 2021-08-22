from GA_CurveFit import PrintList
from typing import Coroutine
import numpy as np, random, operator, pandas as pd, sys, matplotlib.pyplot as plt, matplotlib.cm as cm, math, time
from mpl_toolkits import mplot3d

from mpl_toolkits.mplot3d import Axes3D

POPULATION_SIZE = 2000
CROMOSOME_SIZE = 39
tournamentSize = 10
ITERATIOS = 100
STATES = ['Jalisco', 'Chihuahua', 'Sinaloa', 'Ciudad de Mexico', 'Michoacan', 'Nuevo Leon']
YEARS = ['2014', '2015', '2016', '2017', '2018', '2019']
DATA = [
        [403, 284, 301, 316, 351, 291], # Jalisco
        [235, 317, 286, 268, 270, 263], # Chihuahua
        [234, 285, 255, 275, 278, 236], # Sinaloa
        [291, 200, 220, 193, 223, 220], # Ciudad de Mexico
        [298, 252, 286, 189, 171, 212], # Michoacan
        [226, 202, 245, 223, 229, 204]  # Nuevo Leon
        ]

X = []
Y = []
Z = []
parents = []

def VerifyParent(arr):
    for index in range(len(arr)):
        if index == 6 or index == 7 or index == 8 or index == 9 or index == 10 or index == 11:
            if arr[index] <5:
                arr[index] = 5
    return arr

def CreatePopulation(parents):    
    for i in range(0, POPULATION_SIZE):
        cromosome = []
        for genIndex in range(0,CROMOSOME_SIZE):
            randomGen = random.randint(5,255)
            cromosome.append(randomGen)
        # print(len(cromosome))
        parents.append(cromosome)
        #Print adjusted values
        # for gen in cromosome:
        #     print(gen/5)

def Mask_Number(value, n):
    return value & ((1 << n) - 1)

def SwapBytes(parent1, parent2, startByte):
    #print(startByte)
    while startByte < len(parent1):
        
        temp = parent2[startByte]
        parent2[startByte] = parent1[startByte]
        parent1[startByte] = temp
        startByte += 1
    return parent1, parent2

def Breed(parent1, parent2):
    # del(parent2[-1])
    # del(parent1[-1])
    #print(len(parent1))
    cut = random.randint(0, int(CROMOSOME_SIZE*8)-2)
    #print(cut)
    #cut = 24
    startByte = int(cut/8)

    # print("Parent1: ", parent1)
    # print("Parent2: ", parent2)

    child1 = []
    child2 = []
    y = []
    yy = []
    if cut % 8 != 0:
        
        modulus = cut % 8
        bitsToCut = 8 - modulus        
        # print("Bit to cut: ", cut)
        # print("Bit position: ", modulus)
        # print("Bits to cut: ", bitsToCut)
        # print("Cut is not zero: ",cut," Start byte:", startByte )
        yByte = parent1[startByte]
        yyByte = parent2[startByte]
        # print("YByte: ", bin(yByte))
        # print("YYByte: ", bin(yyByte))
        yCut = Mask_Number(yByte, bitsToCut)
        yyCut = Mask_Number(yyByte, bitsToCut)
        yFinal = ((yByte >> bitsToCut) << bitsToCut) | yyCut
        yyFinal = ((yyByte >> bitsToCut) << bitsToCut) | yCut
        # print("YCut: ", bin(yCut))
        # print("YYCut: ", bin(yyCut))
        # print("YFinal: ", bin(yFinal))
        # print("YYFinal: ", bin(yyFinal))
        parent1[startByte] = yFinal
        parent2[startByte] = yyFinal
        child1, child2 = SwapBytes(parent1, parent2, startByte)
        # print(child1)
        # print(child1)
        
    else:
        child1, child2 = SwapBytes(parent1, parent2, startByte)
        # print(parent1)
        # print(parent2)
        
    # print("Child1: ", child1)
    # print("Child2: ", child2)    
    return child1, child2

def Tournament(parents):
    winner1 = []
    winner2 = []
    distanceToBeat = sys.maxsize

    tournamentList1 =  random.sample(parents, tournamentSize)
    tournamentList2 =  random.sample(parents, tournamentSize)
    for element in tournamentList1:
        #print(element)
        if element[-1] < distanceToBeat:
            winner1 = element
    for element in tournamentList2:
        #print(element)
        if element[-1] < distanceToBeat:
            winner2 = element
    # print("W1: ", winner1)
    # print("W2: ", winner2)
    return winner1, winner2

def CalculateError(population):
    for cromosome in population:
        cromosome = VerifyParent(cromosome)
        m1 = cromosome[0]/5
        m2 = cromosome[1]/5
        m3 = cromosome[2]/5
        m4 = cromosome[3]/5
        m5 = cromosome[4]/5
        m6 = cromosome[5]/5
        de1 = cromosome[6]/5
        de2 = cromosome[7]/5
        de3 = cromosome[8]/5
        de4 = cromosome[9]/5
        de5 = cromosome[10]/5
        de6 = cromosome[11]/5
        p1 = cromosome[12]/5
        p2 = cromosome[13]/5
        p3 = cromosome[14]/5
        p4 = cromosome[15]/5
        p5 = cromosome[16]/5
        p6 = cromosome[17]/5
        p7 = cromosome[18]/5
        p8 = cromosome[19]/5
        p9 = cromosome[20]/5
        q1 = cromosome[21]/5
        q2 = cromosome[22]/5
        q3 = cromosome[23]/5
        q4 = cromosome[24]/5
        q5 = cromosome[25]/5
        q6 = cromosome[26]/5
        q7 = cromosome[27]/5
        q8 = cromosome[28]/5
        q9 = cromosome[29]/5
        r1 = cromosome[30]/5
        r2 = cromosome[31]/5
        r3 = cromosome[32]/5
        r4 = cromosome[33]/5
        r5 = cromosome[34]/5
        r6 = cromosome[35]/5
        r7 = cromosome[36]/5
        r8 = cromosome[37]/5
        r9 = cromosome[38]/5
        error = 0

        for i in range(0, len(STATES)):
            for j in range(0, len(STATES)):
                x=i/10
                y=j/10
                mf1=math.exp((-(x-m1)**2)/(2*de1**2))
                mf2=math.exp((-(x-m2)**2)/(2*de2**2))
                mf3=math.exp((-(x-m3)**2)/(2*de3**2))
                mf4=math.exp((-(y-m4)**2)/(2*de4**2))
                mf5=math.exp((-(y-m5)**2)/(2*de5**2))
                mf6=math.exp((-(y-m6)**2)/(2*de6**2))
                inf1=mf1*mf4
                inf2=mf1*mf5
                inf3=mf1*mf6
                inf4=mf2*mf4
                inf5=mf2*mf5
                inf6=mf2*mf6
                inf7=mf3*mf4
                inf8=mf3*mf5
                inf9=mf3*mf6
                reg1=inf1*(p1*x+q1*y+r1)
                reg2=inf2*(p2*x+q2*y+r2)
                reg3=inf1*(p3*x+q3*y+r3)
                reg4=inf1*(p4*x+q4*y+r4)
                reg5=inf1*(p5*x+q5*y+r5)
                reg6=inf1*(p6*x+q6*y+r6)
                reg7=inf1*(p7*x+q7*y+r7)
                reg8=inf1*(p8*x+q8*y+r8)
                reg9=inf1*(p9*x+q9*y+r9)
                b=inf1+inf2+inf3+inf4+inf5+inf6+inf7+inf8+inf9
                a=reg1+reg2+reg3+reg4+reg5+reg6+reg7+reg8+reg9
                z=a/b
                error += (abs(z-DATA[i][j]))
        cromosome.append(error)

def CreateGraph():
    m1=0
    m2=.6
    m3=1.2
    m4=0
    m5=.6
    m6=1.2
    de1=0.5
    de2=0.5
    de3=0.5
    de4=0.5
    de5=0.5
    de6=0.5
    p1=0
    p2=0
    p3=0
    p4=10
    p5=10
    p6=10
    p7=0
    p8=0
    p9=0
    q1=0
    q2=0
    q3=0
    q4=10
    q5=10
    q6=10
    q7=0
    q8=0
    q9=0
    r1=0
    r2=0
    r3=0
    r4=0
    r5=0
    r6=0
    r7=0
    r8=0
    r9=0

    for i in range(1,10):
        for j in range(1,10):
            x=i/10
            y=j/10
            mf1=math.exp((-(x-m1)**2)/(2*de1**2))
            mf2=math.exp((-(x-m2)**2)/(2*de2**2))
            mf3=math.exp((-(x-m3)**2)/(2*de3**2))
            mf4=math.exp((-(y-m4)**2)/(2*de4**2))
            mf5=math.exp((-(y-m5)**2)/(2*de5**2))
            mf6=math.exp((-(y-m6)**2)/(2*de6**2))
            inf1=mf1*mf4
            inf2=mf1*mf5
            inf3=mf1*mf6
            inf4=mf2*mf4
            inf5=mf2*mf5
            inf6=mf2*mf6
            inf7=mf3*mf4
            inf8=mf3*mf5
            inf9=mf3*mf6
            reg1=inf1*(p1*x+q1*y+r1)
            reg2=inf2*(p2*x+q2*y+r2)
            reg3=inf1*(p3*x+q3*y+r3)
            reg4=inf1*(p4*x+q4*y+r4)
            reg5=inf1*(p5*x+q5*y+r5)
            reg6=inf1*(p6*x+q6*y+r6)
            reg7=inf1*(p7*x+q7*y+r7)
            reg8=inf1*(p8*x+q8*y+r8)
            reg9=inf1*(p9*x+q9*y+r9)
            b=inf1+inf2+inf3+inf4+inf5+inf6+inf7+inf8+inf9
            a=reg1+reg2+reg3+reg4+reg5+reg6+reg7+reg8+reg9
            z=a/b
            X.append(x)
            Y.append(y)
            Z.append(z)
    print(X)
    XGraph, YGraph, ZGraph = np.array(X), np.array(Y), np.array(Z)
    print(X)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    # Z = np.array(DATA)
    # ax.plot_surface(XGraph, YGraph, Z,cmap='viridis', edgecolor='none')
    ax.plot_trisurf(X, Y, Z, linewidth=0, antialiased=False)
    ax.set_title('Surface plot')
    plt.show()

def MutateCromosome(arr, probGen, probBit):
    mutatedArray = []
    mutatedArray = arr
    mutatedIndexes = []
    #print(array)
    for mutated in range(0, probGen):
        index = random.randint(0,len(arr) -2)
        
        if index not in mutatedIndexes:
            # print("Index: ", index)
            mutated += 1
            bitIndexes =[]
            mutatedIndexes.append(index)
            #print("Gen: ", index)
            for bit in range(0,probBit):
                bitIndex = random.randint(0,7)
                if bitIndex not in bitIndexes:
                    bitIndexes.append(bitIndex)
                    bit += 1
                    # print("Bit: ", bitIndex)
                    # print("Val:", arr[index])
                    num = arr[index] ^ (1 << bitIndex)
                    if num < 5:
                        arr[index] = 5
                    else:
                        arr[index] = num
    return arr

def Mutate(arrs, probList, probGen, probBit):
    arr= arrs
    mutatedCromosomes = []
    #Pick random cromosomes to mutate
    for mutatedCromosome in range(0, probList):        
        cromosome = random.randint(0,len(arr) -1)        
        if cromosome not in mutatedCromosomes:
            mutatedCromosomes.append(cromosome)
            #print("Mutated cromosome: ", cromosome)
            mutatedCromosome += 1
            #print("Original: ", arr[cromosome])
            arr[cromosome] = MutateCromosome(arr[cromosome], probGen, probBit)
            #print("Mutated: ", arr[cromosome])
    return arr

def RemoveError(arr):
    temp = []
    for child in arr:
        tempChild = []
        for i in range(0,CROMOSOME_SIZE):
            tempChild.append(child[i])
        #print(tempChild, len(tempChild))
        temp.append(tempChild)
    return temp
def Elitism(arr1,arr2):
    temp = []
    # print("Iteration")
    for element in arr1:
        temp.append(element)
    for element in arr2:
        temp.append(element)
    temp.sort(key = lambda x: x[-1])
    # print("Temp before cutting:")
    # PrintList(temp)
    temp = temp[:int(len(temp)/2)]
    # print(len(temp[0]))
    # print("Temp after cutting:")
    # PrintList(temp)
    # print(len(temp))
    # PrintList(temp)
    return temp

def main():
    # CreateGraph()
    parents = []
    CreatePopulation(parents)
    CalculateError(parents)
    # PrintList(parents)

    for i in range(0, POPULATION_SIZE):
        print("Iteration: ", i)
        children = []
        elite = []
        for i in range(0,int(POPULATION_SIZE/2)):
            
            winner1, winner2 = Tournament(parents)
            child1, child2 = Breed(winner1, winner2)
            children.append(child1)
            children.append(child2)
            # print(len(children))
        print(len(children))
    #     # print("Children:")
    #     #SortList(children)
    #     # PrintList(children)
        children = Mutate(children, 200,19,3)
        children = RemoveError(children)
        CalculateError(children)
        
        parents = Elitism(parents,children)
    #     # parents = children
    #     # print("Mutated Children:")
    #     # SortList(children)
    #     # PrintList(children)
    #     #print(len(parents[0]))
        print("Best from iteration: ", parents[0][-1])
    #     best.append(parents[0])
    #     TemperatureErrors.append(parents[0][-1])


if __name__=="__main__":
    main()