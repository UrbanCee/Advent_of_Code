import re
from itertools import combinations as co
from functools import reduce
with open("inputs/day10.txt") as fp:
    inputs = [([c == '#' for c in lights],[[int(n) for n in button.split(",")] for button in re.findall(r'\(([\d,]+)\)',buttons)],[int(n) for n in joltage.split(",")]) for lights,buttons,joltage in re.findall(r'\[([.#]+)\] (.*) {([\d,]+)}',fp.read())]

def pushbutton(lights,button):
    return [not s if i in button else s for i,s in enumerate(lights)]
def lowestComb(inp):
    for i in range(1,len(inp[1])):
        for comb in co(inp[1],i):
            if reduce(pushbutton,comb,[False for _ in inp[0]])==inp[0]:return i
print("Task 1:",sum(lowestComb(input) for input in inputs))