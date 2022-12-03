# Day 3: Rucksack Reorganization

#helper function to calculate alphabetical value
def calcValue(char):
    if(ord(char) < 97): #uppercase calculation
        value =  ((ord(char) - 65) + 27) #subtract 65 but add 26 (whole loop of alphabet) and add 1 more
    else:
        value =  (ord(char) - 97) + 1 #we just need to add 1 for lowercase value
    return value

# Thought process: split line in half. Then, in a for loop, maintain a set of the unique characters.
# Once we find a character that exists in both containers, we add convert it to find its value, exit out of that loop and continue with next line.
def calcSum():

    rucksackContents = open("..\..\Advent Of Code\Advent-Of-Code-2022\Day 3\input.txt", 'r') 
    sum = 0

    for line in rucksackContents: #for each line
        
        lineContent = line.strip() #strip any new lines
        halfLen = int(len(lineContent) / 2)

        rucksackSet = set(lineContent[:halfLen]) #we set the contents with half the length of the line to compare
        #print(rucksackSet)

        #print(lineContent)
        for char in range(halfLen): #split line in half
            lastIterChar = lineContent[(char * -1) -1] #the last character (based on our iterator, char)

            if(lastIterChar in rucksackSet): #if we find the duplicate letter, we add that value to the sum.
                value = calcValue(lastIterChar)
                sum += value
                print(f"The char, {lastIterChar} is already in the set, so we will call out, and add its value: {value} and sum is now {sum}")
                break #we found the duplicate the elf added, the rest [of the duplicates] don't matter as long as we just add the value from first occurence.
            else: #do nothing 
                print(f"The char, {lastIterChar} is not in the set, we will do nothing.")

            #checker = (char * -1) - 1
            #print(lineContent[(char * -1) - 1])
    return(sum)

#Similar approach with 1st part except we instead are comparing 3 lines with eachother, so we read (and store) the 3 lines, set them, and find the only
#Duplicate letter which we will calculate its value much like the 1st part
def calcBadgeSum():
    sum = 0
    rucksackContents = open("..\..\Advent Of Code\Advent-Of-Code-2022\Day 3\input.txt", 'r') 

    iter = 1 #lazy read lines by 3
    line1 = ""
    line2 = ""
    line3 = ""

    for line in rucksackContents: #for each line
        lineContent = line.strip() #strip any new lines
        #print(iter)

        if(iter % 3 == 1): #lazy read and store values of 3 lines to calc the badge every 3 lines
            line1 = set(lineContent)
            iter += 1
        elif(iter % 3 == 2):
            line2 = set(lineContent)
            iter += 1
        elif(iter % 3 == 0):
            line3 = set(lineContent)
            badgeLetter = list(line1 & line2 & line3)
    
            value = calcValue(badgeLetter[0])
            sum += value

            print(sum)
            #print(calcValue(badgeLetter[0]))
            #calcValue(str(line1 & line2 & line3))
            line1, line2, line3 = "","",""
            iter += 1
    return sum

print(calcSum())
print(calcBadgeSum())
