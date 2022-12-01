#Advent Of Code 2022 - Day 1: Calorie Counting 
#
#Print code are commented out but left intentionally just to show how i was checking my values!

def maxCalCount(): #returns the calorie count of the elf with the most calories
    calorie_list = open("..\..\Advent Of Code\Advent-Of-Code-2022\Day 1\input.txt", 'r') 

    elfCal = [] #empty array
    idx = 1

    for line in calorie_list:

        lineContent = line.strip() #strip \n (keeps empty spaces)
        #print(lineContent)
        if(lineContent == ""): #if elf's cal contents are exhausted, increment idx where we count total cal
            idx += 1
        else: #increment calorie total until there are no more
            if idx > len(elfCal): #if the index is larger than the length of the array, we need to add an item to the list
                elfCal.append(int(lineContent))
            else: #otherwise increment instead
                #print(elfCal)
                elfCal[idx-1] += int(lineContent) 
    return max(elfCal) , elfCal

def sumOfNthHighest(n, arr): #finds the sum of calories the Nth number of elves have
    temp = sorted(arr) #sort the array (least to greatest)

    try: #catch potential exceptions    

        #print(temp[-1], temp[-2], temp[-3])

        sum = 0 #set sum to 0
        for i in range(n): #for the number of members we want to sum up
            sum += temp[(i * -1) - 1]
        return sum
    except:
        print("An exception occured. Maybe you selected a number higher than there are elves?") 
        return 0

#function calls
maxElf, elfSumArray = maxCalCount()
print(maxElf)

print(sumOfNthHighest(3000, elfSumArray))