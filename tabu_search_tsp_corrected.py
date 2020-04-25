from xlrd import *
import matplotlib.pyplot as plt
import random

def fitness(candidate):
    ctr = 0
    
    
    for i in range(len(candidate)-1):
        ctr = ctr + wb.sheets()[0].cell(candidate[i]-1,candidate[i+1]-1).value
        
    return (1/ctr)

wb = open_workbook("cmr.xlsx")

def choose_initial():
    s = list(range(2,100))
    s.append(1)
    min_cost = 99400
    min_fitness = 1/min_cost
    while(fitness(s) < min_fitness):
        s.remove(1)
        random.shuffle(s)
        s.append(1)
    return s
        
            
        

s0 = choose_initial()
    
sBest = s0
bestCandidate = s0
tabuList = []
tabuList.append(s0)
i = 10000



def contains(lst, e):
    for i in lst:
        if(i == e):
            return 1
    return 0





def getNeighbour(candidate_b):
    candidate = []
    for i in candidate_b:
        candidate.append(i)
    candidate.remove(1)
    random.shuffle(candidate)
    candidate.append(1)
    
    return candidate

print("Generation : ", 1, "Candidate : ", sBest, "Distance : ", (1/fitness(sBest)))
generations = []
cost = []
generations.append(1)
cost.append(1/fitness(sBest))
gen = 1

while(i):
    i = i - 1
    sCandidate = getNeighbour(bestCandidate)
    if((not contains(tabuList , sCandidate)) and (fitness(sCandidate) > fitness(bestCandidate))):
           bestCandidate = sCandidate
              

    if(fitness(bestCandidate) > fitness(sBest)):
           sBest = bestCandidate
           gen = gen + 1
           print("Generation : ", gen, "Candidate : ", sBest, "Distance : ", (1/fitness(sBest)))
           generations.append(gen)
           cost.append(1/fitness(sBest))
           
    tabuList.append(bestCandidate)
    if (len(tabuList) > 10):
           tabuList.pop(0)



plt.scatter(generations,cost)
plt.title("Cost vs Generation")
plt.ylabel("Cost")
plt.xlabel("Generation")
plt.show()
           
