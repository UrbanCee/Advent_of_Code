from collections import deque

def marble_game(players,highestMarble):
    marbleCircle = deque([0])
    score = dict()
    for i in range(1,highestMarble):
        if i%23!=0:
            marbleCircle.rotate(1)
            marbleCircle.appendleft(i)
        else:
            marbleCircle.rotate(-7)
            score[i%players]=score.get(i%players,0)+i+marbleCircle.popleft()
            marbleCircle.rotate(1)
    return score

players,highestMarble=479,71035
print("Task 1:",max(marble_game(players,highestMarble).values()))
print("Task 2:",max(marble_game(players,highestMarble*100).values()))



