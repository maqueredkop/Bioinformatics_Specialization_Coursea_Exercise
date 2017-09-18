import numpy as np
 
n = 14
m = 5

s = np.zeros((n+1,m+1), dtype=np.int)

#down = [[1,0,2,4,3],[4,6,5,2,1],[4,4,5,2,1],[5,6,8,5,3]]
#right = [[3,2,4,0],[3,2,4,2],[0,7,3,3],[3,3,0,2],[1,3,2,2]]

#with open('Manhattan_tourist.txt','r') as f:
with open('dataset_261_10.txt','r') as f:
    score_data = []
    for line in f:
        line = line.strip()
        line = line.split()
        if '-' not in line:
            line = [int(x) for x in line]
        score_data.append(line)

index = score_data.index(['-'])
down = score_data[0:index]
right = score_data[index+1 :]

down_array = np.array(down)
right_array = np.array(right)

#print(down_array)
#print(right_array)

def manhattan_tourist(n,m,down,right):
    s[0,0] = 0
    for i in range(1,n+1):
        s[i,0] = s[i-1,0] + down_array[i-1,0]
    for j in range(1,m+1):
        s[0,j] = s[0,j-1] + right_array[0,j-1]
    for i in range(1,n+1):
        for j in range(1,m+1):
            s[i,j] = max(s[i-1,j]+down_array[i-1,j], s[i,j-1]+right_array[i,j-1])
    
    return s[n,m]
        
print(manhattan_tourist(n,m,down,right))
