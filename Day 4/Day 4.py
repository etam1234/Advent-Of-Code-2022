# Day 4: Camp Cleanup

#need to find ranges wholly in another range
def containOthersCount(): #part 1
    cleaningNotes = open("..\..\Advent Of Code\Advent-Of-Code-2022\Day 4\input.txt", 'r')
    count = 0 

    for line in cleaningNotes:
        #print(line.strip())
        filteredline = line.strip()

        elf1, elf2 = filteredline.split(",")
        #print(f'{elf1} and {elf2}')

        elf1lower, elf1upper = elf1.split("-")
        elf1lower, elf1upper = int(elf1lower) , int(elf1upper)

        elf2lower, elf2upper = elf2.split("-")
        elf2lower, elf2upper = int(elf2lower) , int(elf2upper)

        print(f'Elf1: {elf1lower} and {elf1upper}. Elf2: {elf2lower} and {elf2upper}')

        #print(elf1lower > elf2lower and elf1upper <= elf2upper)
        #print(f'Checker as follows: {elf1lower} > {elf2lower} and {elf1upper} <= {elf2upper}')
        if((elf1lower >= elf2lower) and (elf1upper <= elf2upper)): #within range of elf1 or both ranges are the same so it counts (elf2 would also count if not elif)
            count += 1
            print(f'elf1 is within the range of elf2, adding to count which is...{count}')
        elif(elf2lower >= elf1lower and elf2upper <= elf1upper): #within range of elf2
            count += 1
            print(f'elf2 is within the range of elf1, adding to count which is...{count}')
    return count

#here, instead of just wholly in one range, we just need to see if there is any overlap at all
def overlapCount(): #part 2
    cleaningNotes = open("..\..\Advent Of Code\Advent-Of-Code-2022\Day 4\input.txt", 'r') #lazy copy over
    count = 0 

    for line in cleaningNotes:
        #print(line.strip())
        filteredline = line.strip()

        elf1, elf2 = filteredline.split(",")
        #print(f'{elf1} and {elf2}')

        elf1lower, elf1upper = elf1.split("-")
        elf1lower, elf1upper = int(elf1lower) , int(elf1upper)

        elf2lower, elf2upper = elf2.split("-")
        elf2lower, elf2upper = int(elf2lower) , int(elf2upper)

        print(f'Elf1: {elf1lower} and {elf1upper}. Elf2: {elf2lower} and {elf2upper}')

        if( elf1lower <= elf2lower <= elf1upper or elf2lower <= elf1lower <= elf2upper): #checks to see if there is an overlap on elf1 on elf2 or elf2 on elf1
            count += 1
            print(f'overlap detected')
    return count

print(containOthersCount())
print(overlapCount())


