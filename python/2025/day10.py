import re
with open("inputs/day10_train.txt") as fp:
    input = [([c == '#' for c in lights],[[int(n) for n in button.split(",")] for button in re.findall(r'\(([\d,]+)\)',buttons)],[int(n) for n in joltage.split(",")]) for lights,buttons,joltage in re.findall(r'\[([.#]+)\] (.*) {([\d,]+)}',fp.read())]

for lights,buttons,_ in input:
    