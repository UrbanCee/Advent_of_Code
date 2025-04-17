import re
import itertools
import numpy as np

rex = "([A-Za-z]+) would (gain|lose) (\\d+) happiness units by sitting next to ([A-Za-z]+)"

happy = {}
people = set()

with open("inputs/day13.txt") as fp:
    for line in fp.readlines():
        for person,sign,amt,neigh in re.findall(rex,line):
            happy[person+neigh]=-int(amt) if sign=="lose" else int(amt)
            people.add(person)

def happynessByArrangement(arrangement):
    happyness=0
    for i in range(len(arrangement)):
        for neighInd in [(i+1)%len(arrangement),(i+len(arrangement)-1)%len(arrangement)]:
            happyness+=happy[arrangement[i]+arrangement[neighInd]]
    return happyness

print("Task1: ",np.max([happynessByArrangement(arrangement) for arrangement in itertools.permutations(people)]))

for person in people:
    happy["You"+person]=0
    happy[person+"You"]=0

people.add("You")

print("Task2: ",np.max([happynessByArrangement(arrangement) for arrangement in itertools.permutations(people)]))

