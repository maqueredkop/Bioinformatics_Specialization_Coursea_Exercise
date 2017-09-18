import collections

def south_or_east(i,j,count=[]):
    if i == 0 and j == 0:
        return 0
    x = 0
    y = 0
    
    #counter = collections.Counter()
   
    if i > 0:
        if i == 3 and j == 2:
            count.append(1)
            #counter[1] += 1
            #print(count)
        south_or_east(i-1,j)
    if j > 0:
        if i == 3 and j == 2:
            count.append(1)
            #counter[1] += 1
        south_or_east(i,j-1)
    return len(count)
	
print(south_or_east(3,3))