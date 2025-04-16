import numpy as np
import itertools as it

def increment(string):
    if len(string)==0:
        return "a"
    if (string[-1]=="z"):
        return increment(string[:-1])+"a"
    return string[:-1]+chr(ord(string[-1]) + 1)

def noStraight(string):
    for i in range (len(string)-2):
        if ord(string[i])+1==ord(string[i+1]) and ord(string[i+1])+1==ord(string[i+2]):
            return False
    return True

def forbiddenvowels(string):
    for ch in ["i","o","l"]:
        if ch in string:
            return True
    return False


def noDoublePairs(string):
    return len([1 for char,groups in it.groupby(string) if len(list(groups))>1])<=1

def nextValid(password):
    while (forbiddenvowels(password) or noStraight(password) or noDoublePairs(password)):
        password=increment(password)
    return password



password = increment("cqjxjnds")
password = nextValid(password)
print("Task 1: pwd:",password)
password = nextValid(increment(password))
print("Task 2: pwd:",password)