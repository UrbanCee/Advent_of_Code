import re
with open("inputs/day10_train.txt") as fp:
    input = [([c == '#' for c in lights],[[int(n) for n in button.split(",")] for button in re.findall(r'\(([\d,]+)\)',buttons)],[int(n) for n in joltage.split(",")]) for lights,buttons,joltage in re.findall(r'\[([.#]+)\] (.*) {([\d,]+)}',fp.read())]

def pushbutton(lights,button):
    return [not s if i in button else s for i,s in enumerate(lights)]
def tryButtons(lights,buttons):
    for button in buttons:
        print(button)
        for 

for lights,buttons,_ in input:
