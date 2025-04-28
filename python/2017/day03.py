import math
from size import *

input = 368078
squareLength = int(math.sqrt(input-1)) if int(math.sqrt(input-1))%2==1 else int(math.sqrt(input-1))-1 
print("Task 1:",(squareLength+1)//2+abs((input-squareLength**2)%(squareLength+1)-((squareLength+1)//2)))

