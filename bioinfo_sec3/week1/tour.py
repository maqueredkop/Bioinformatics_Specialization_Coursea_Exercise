

#def add(n,m):
    

def Tour(n,m):
    if n == m == 1:
        return 2
    elif n == 1 and m > 1:
        return Tour(n, m-1) + 1
    elif m == 1 and n > 1:
        return Tour(n-1, m) + 1
    else:
        return Tour(n-1,m-1)  + 1


print(Tour(2,2))
