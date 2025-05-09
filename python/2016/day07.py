import re

exprIn = [re.compile(r'^([a-z]+)\['),re.compile(r'\]([a-z]+)$'),re.compile(r'\]([a-z]+)\[')]
exprOut = re.compile(r'\[([a-z]+)\]')

def TSL(s):
    return sum([s[i]==s[i+3] and s[i+1]==s[i+2] and s[i]!=s[i+1] for i in range(len(s)-3)])>0
def BABs(s):
    return [s[i+1]+s[i]+s[i+1] for i in range(len(s)-2) if s[i]==s[i+2] and s[i]!=s[i+1]]

with open("inputs/day07.txt") as fp:
    addresses = [([token  for ex in exprIn for token in ex.findall(line)],[token for token in exprOut.findall(line)]) for line in map(str.strip,fp.readlines())]

print("Task1: ",sum([ sum([ TSL(token) for token in address[0]])>0 and sum([TSL(token) for token in address[1]])==0 for address in addresses ]))
print("Task2: ",sum([ sum([ bab in token for token in address[1] for bab in [bab for token in address[0] for bab in BABs(token)] ])>0 for address in addresses ]))

