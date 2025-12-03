import re
with open("inputs/day02.txt") as fp:
    ranges = [(int(l),int(h)) for l,h in re.findall(r'(\d+)\-(\d+)',fp.read())]

def checkrepeating(s,parts): return sum(s[i*len(s)//parts:(i+1)*len(s)//parts]!=s[:len(s)//parts] for i in range(1,parts))==0

print("Task 1:",sum(int(si) for l,h in ranges for si in [str(i) for i in range(l,h+1)] if len(si)%2 == 0 and checkrepeating(si,2)))
print("Task 2:",sum({int(si) for l,h in ranges for si in [str(i) for i in range(l,h+1)] for p in [i for i in range(2,len(si)+1) if len(si)%i==0] if checkrepeating(si,p)}))

