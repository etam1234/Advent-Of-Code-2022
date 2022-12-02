#Advent Of Code 2022 - Day 2: Rock Paper Scissors


#1 for Rock, 2 for Paper, and 3 for Scissors plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won)

#A and X -> rock 
#B and Y -> paper
#C and Z -> scissor

#A X --> both rock, a draw (1+3 = 4)
#A Y --> rock loses to paper, a win (2+6 = 8)
#A Z --> rock wins to scissor, a loss (3+0 = 3)

#B X --> paper beats rock, a loss (1+0 = 1)
#B Y --> both paper, a draw (2+3 = 5)
#B Z --> paper loses to scissor, a win (3+6 = 9)

#C X --> scissor loses to rock, a win (1+6 = 7)
#C Y --> scissor beats paper, a loss (2+0 = 2)
#C Z --> scissor draws with scissor, a draw (3+3 = 6)

scoreDict = {
        "A X" : 4, "A Y" : 8, "A Z" : 3, 
        "B X": 1, "B Y" : 5, "B Z": 9,
        "C X": 7, "C Y" : 2, "C Z": 6
    } #the dictionary containing all the score values

def totalScore(): #adds the total score given the strategy guide
    strategy_guide = open("..\..\Advent Of Code\Advent-Of-Code-2022\Day 2\input.txt", 'r') 
    score = 0

    for line in strategy_guide:
        #print(line.strip())
        score += scoreDict[line.strip()]
        #print(scoreDict[line.strip()])
    return score

def decryptGuide(): #the guide now is actually telling us how we should play, so let's adjust our dictionary as such; we can still call the scoredict to grab our score tho.
    score = 0
    #a new dictionary to determine the cheat strat we should play
    #X we need to lose, Y we need to draw, Z we need to win
    strategyDict = {
             "A X" : "A Z", "A Y" : "A X", "A Z" : "A Y", 
             "B X": "B X", "B Y" : "B Y", "B Z": "B Z", #the interesting note here is that, your resulting play doesn't change when your opponent plays paper
             "C X": "C Y", "C Y" : "C Z", "C Z": "C X"
    }
    strategy_guide = open("..\..\Advent Of Code\Advent-Of-Code-2022\Day 2\input.txt", 'r') 
    for line in strategy_guide:
        #print(strategyDict[line.strip()])
        score += scoreDict[strategyDict[line.strip()]]
    return score

#A Y --> you want a draw, so you choose rock as well
#B X
#C Z

print(totalScore())
print(decryptGuide())