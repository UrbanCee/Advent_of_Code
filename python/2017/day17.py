offset=369

pos=1
buffer = [0,1]
for i in range(2,2018):
    buffer.insert(pos,i)
    pos=(pos+1+offset)%len(buffer)
print("Task1:", buffer[(pos+len(buffer)-offset)%len(buffer)])

currentIndex=0
numberPost0=0
for bufSize in range(1,50000000):
    currentIndex=(currentIndex+offset+1)%bufSize
    if (currentIndex==0):
        numberPost0=bufSize
print("Task2:",numberPost0)
