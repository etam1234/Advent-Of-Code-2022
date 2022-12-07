# Day 7: No Space Left On Device
# INCOMPLETE*


def totalSum(inputDict):
    sum = 0
    for name, value in inputDict.items():
        if(value <= 100000):
            sum += value
    return sum

# I followed the methodology as suggested by several users except with match/cases
# This was the first problem I had to search for external guidance for suggestions since I really wasnt sure how to approach the problem at all
def sumSmallFile():
    sum = 0
    dirsize = {} #a dictionary containing the contents of the dir following the traversal (dictionary within a dictionary)
    path = []

    with open("..\..\Advent Of Code\Advent-Of-Code-2022\Day 7\input.txt", 'r') as dirTraverse: 
        for line in dirTraverse:
            splitContent = line.split()
            #print(line.strip())
            match splitContent:
                case '$', 'ls': #with match case in python, i learned you can specify some really specific cases
                    pass #pass means you skip this case, that is, nothing happens.
                case '$' , 'cd', '..':
                    path = path[:-1]
                    #print(f"Escape once; New dir: {path}")
                case '$', 'cd', newDir: #I also learned a new technique where you can store variables as well with match/case!
                    #print(f'Entering a newDir: {newDir}') 
                    path.append(newDir)
                    #print(f'Path: [{path}]')
                case 'dir', dirName:
                    pass
                case size, fileName:
                    #print(f'Size is: {size}, filename: {fileName}')
                    currDir = ''
                    for dir in path: 
                        if(dir != '/' and currDir != '/'): #explicit full path in order to avoid duplicate directory names
                            currDir += '/'
                        currDir += dir
                        #print(f'dir is: {currDir}')
                        dirsize[currDir] = dirsize.get(currDir, 0) + int(size)

    print(f'Biggest Dir file size: {findBiggestDir(dirsize)}')
    return totalSum(dirsize)

def findBiggestDir(dirsize): #find the current extra space we have to spare, but then calculate the amount we need at least in order to delete
    requiredFile = 70000000
    remainingFile = 0
    #print(dirsize['/'])
    print(f"Finding current spare space we have atm...: {requiredFile - dirsize['/']}, therefore we need 30,000,000 - {requiredFile - dirsize['/']} to get the space we need to free: {30000000 - (requiredFile - dirsize['/'])}")
    remainingFile = 30000000 - (requiredFile - dirsize['/']) #to find the minimum size we have to reach
    return(min([value for key,value in dirsize.items() if value >= remainingFile]))

sumSmallFile()
print(sumSmallFile())