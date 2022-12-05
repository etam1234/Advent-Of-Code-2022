#Day 5: Supply Stacks

myDict = {} #utilizing dict
myDict['1'] = []
myDict['2'] = []
myDict['3'] = []
myDict['4'] = []
myDict['5'] = []
myDict['6'] = []
myDict['7'] = []
myDict['8'] = []
myDict['9'] = []

#helper to count how many spaces to skip for the next crate 
def countSkip(element):
    spaces = int(element.count(" "))
    if(spaces == 1):
        return 1
    elif(spaces == 5):
        return 2
    else:
        spaces -= 1
        spaces /= 4
        return spaces + 1
#1 is 1 space, 5 is 2 spaces, 9 is 3 spaces, 13 is 4 spaces
# 1,5,9,13
# 1 + 4(n-1) = spaces
# 4(n-1) = spaces - 1
# n = ((spaces  - 1) / 4) + 1
# (n - 4) + 1 where n is number of spaces

#helper to insert the element
def insertElement(idxCounter, element):
    myDict[str(int(idxCounter))].insert(0, element)

#Part 1 pop
def customPop(list1, list2):
    #print(f'Pop {list1} and append {list2}')
    #myDict[str(int(idxCounter))].insert(0, element)
    itemToPop = myDict[list1].pop()

    myDict[list2].append(itemToPop)
    #print(f'New values are List{list1}: {myDict[list1]} and List{list2}: {myDict[list2]}')
    return

#Part 2 pop
def customPopVER2(length, list1):
    storedDict = {}
    storedDict['temp'] = []
    for i in range(length):
        storedDict['temp'].append(myDict[list1].pop())
    return storedDict

# This function is for both Part 1 and 2
# Using a dictionary of lists to store the contents of the crates 
# then we build it as a stack after we initialize the beginning contents.
def moveContents():
    cratesOrder = open("..\..\Advent Of Code\Advent-Of-Code-2022\Day 5\input.txt", 'r')
    contentCounter = 0
    idxCounter = 1
    finalString = ""
    for line in cratesOrder:
        lineContent = line.strip()
        #print(repr(line))
        if(contentCounter <= 8):
            idxCounter = 1
            tempTest = lineContent.split("[")
            print(f'Length: {len(tempTest)} and contents: {tempTest}')
            contentCounter += 1
            for i in range(1, len(tempTest)):
                #print(f'Element: {tempTest[i]},(to track spaces)')
                currEle = tempTest[i]
                #print(len(currEle))
                insertElement(idxCounter, currEle[0])
                print(f'Adding element {currEle[0]} to position {idxCounter}...')
                idxCounter = idxCounter + countSkip(currEle)

        elif(contentCounter == 9): #skip line
            contentCounter += 1
        else:
            splitLine = lineContent.split(" ")
           # print(splitLine)
            numMove = splitLine[1]
            #print(int(numMove))
            
            tempDict = customPopVER2(int(numMove), splitLine[3])
            #print(tempDict)
            for i in range(int(numMove)):
                itemToPop = tempDict['temp'].pop()
                myDict[splitLine[5]].append(itemToPop)
            #########################################################################################
            ###  customPop(splitLine[3], splitLine[5]) #call this function only for part1 results ###
            #########################################################################################
    print(myDict)
    finalString = myDict['1'].pop() + myDict['2'].pop() + myDict['3'].pop() + myDict['4'].pop() + myDict['5'].pop() + myDict['6'].pop() + myDict['7'].pop() + myDict['8'].pop() + myDict['9'].pop()
    return finalString
        
print(moveContents())
