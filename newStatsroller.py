import random

statcounter = 0
roll = [0,0,0,0]
minVal = 0
for statcounter in range(6):
    counter = 0
    counter2 = 0
    output = 0
    tookOneOut = 0
    for counter in range(4):
        roll[counter] = random.randint(1,6)
    minVal = min(roll)
    for counter2 in range(len(roll)):
        if roll[counter2] == minVal and tookOneOut == 0:
            roll[counter2] = 0
            tookOneOut = 1
        #print roll[counter2]
        output = roll[counter2] + output
    print output
