from collections import deque
players =479
lastScore = 71035

currentMarble = 3
circle = [0,2,1]
currentIndex = 1
currentPlayerIndex = 2
score = dict()

while currentMarble<=lastScore:
    if (currentMarble%23==0):
        currentIndex=(currentIndex-7+len(circle))%(len(circle))
        score[currentPlayerIndex]=score.get(currentPlayerIndex,0)+currentMarble+circle[currentIndex]
        circle=circle[:currentIndex]+circle[currentIndex+1:]
    else:
        currentIndex=(currentIndex+1)%(len(circle))+1
        circle.insert(currentIndex,currentMarble)
    currentMarble+=1
    currentPlayerIndex=(currentPlayerIndex+1)%players

print("Task 1: ",score[max(score,key=lambda k:score[k])])
    


