
list 

with open("inputs/day1_training.txt","rt") as fp:
    lines = [list(map(int,line.split())) for line in fp.readlines()]
    
for out in lines:
    print(out)    
        
