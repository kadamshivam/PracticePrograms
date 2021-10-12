N = 10
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
prefer = [[10, 11, 12, 13, 14, 15, 16, 17, 18, 19],[19, 16, 14, 11, 12, 17, 10, 13, 15, 18],[13, 15, 14, 12, 19, 17, 10, 11, 16, 18],[12, 16, 15, 11, 10, 17, 19, 13, 14, 18],[10, 12, 14, 16, 18, 11, 13, 15, 17, 19],[19, 16, 14, 11, 12, 17, 10, 13, 15, 18],[13, 15, 14, 12, 19, 17, 10, 11, 16, 18],[12, 16, 15, 11, 10, 17, 19, 13, 14, 18],[10, 11, 12, 13, 14, 15, 16, 17, 18, 19],[19, 16, 14, 11, 12, 17, 10, 13, 15, 18],
          [0, 1, 2, 3, 5, 6, 4, 8, 9, 7],[7, 3, 4, 1, 5, 6, 8, 2, 9, 0],[0, 1, 3, 4, 5, 6, 2, 8, 9, 7],[0, 7, 2, 4, 3, 6, 5, 8, 9, 1],[6, 1, 2, 4, 5, 3, 9, 8, 0, 7],[7, 3, 4, 1, 5, 6, 8, 2, 9, 0],[0, 1, 3, 4, 5, 6, 2, 8, 9, 7],[0, 7, 2, 4, 3, 6, 5, 8, 9, 1],[0, 7, 2, 4, 3, 6, 5, 8, 9, 1],[7, 3, 4, 1, 5, 6, 8, 2, 9, 0]] 
stableMarriageProblem(prefer) 
print("--- %s seconds ---" % (time.time() - start_time))