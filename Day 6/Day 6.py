# Day 6: Tuning Trouble


# Used a set to match every 4 (and 14) unique char in a single iteration of the giant! word
def startOfSignal(): #returns end idx of first unique 4 char
    signalContents = open("..\..\Advent Of Code\Advent-Of-Code-2022\Day 6\input.txt", 'r')

    for line in signalContents: #only one word actually not really necessary
        lineClean = line.strip()

        for i in range(len(lineClean)-3):
           #print(set(lineClean[i:i+4]))
           if(len(set(lineClean[i:i+4])) == 4):
               print(set(lineClean[i:i+4]))
               return i+4 #the first marker with 4 unique characters

    return -1 #no unique 4 chars found.

def startOfMessage(): #14 instead of 4 this time.
    signalContents = open("..\..\Advent Of Code\Advent-Of-Code-2022\Day 6\input.txt", 'r')

    for line in signalContents: #only one word actually not really necessary
        lineClean = line.strip()

        for i in range(len(lineClean)-13):
           if(len(set(lineClean[i:i+14])) == 14):
               print(set(lineClean[i:i+14]))
               return i+14 #the first marker with 14 unique characters

    return -1 #no unique 14 chars found.

print(startOfSignal())
print(startOfMessage())

