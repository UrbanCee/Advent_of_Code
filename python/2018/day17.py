import re


with open("inputs/day17_train.txt") as fp:
    claycoords = [(xy,c1,cs,ce) for xy,c1,cs,ce in re.findall(r'([xy])=(\d+), [xy]=(\d+)\.\.(\d+)',fp.read().strip())]


