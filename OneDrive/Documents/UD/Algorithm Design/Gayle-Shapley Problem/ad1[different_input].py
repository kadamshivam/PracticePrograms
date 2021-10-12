N = 100
import random
import time
start_time = time.time()
def womenFirstChoicePreference(prefer, women, other_mens, Firstchoice):
    for i in range(N): 
        if (prefer[women][i] == Firstchoice): 
            return True
        if (prefer[women][i] == other_mens): 
            return False

def stableMarriageProblem(prefer): 
    womenAlly = [-1 for i in range(N)] 
    other_mensFree = [False for i in range(N)] 
    freeCount = N 
    while (freeCount > 0): 
        other_mens = 0
        while (other_mens < N): 
            if (other_mensFree[other_mens] == False): 
                break
            other_mens += 1
        i = 0
        while i < N and other_mensFree[other_mens] == False: 
            women = prefer[other_mens][i] 
            if (womenAlly[women - N] == -1): 
                womenAlly[women - N] = other_mens 
                other_mensFree[other_mens] = True
                freeCount -= 1
            else:  
                Firstchoice = womenAlly[women - N] 
                if (womenFirstChoicePreference(prefer, women, other_mens, Firstchoice) == False): 
                    womenAlly[women - N] = other_mens 
                    other_mensFree[other_mens] = True
                    other_mensFree[Firstchoice] = False
            i += 1
    print("Woman ", " Man") 
    for i in range(N): 
        print(i + N, "\t", womenAlly[i]) 

prefer=[]

for i in range(N):
    prefer.append(random.sample(range(N,2*N), N))

for i in range(N):
    prefer.append(random.sample(range(0,N), N))    

print(prefer) 
stableMarriageProblem(prefer)
print("--- %s seconds ---" % (time.time() - start_time))
