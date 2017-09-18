


#v = 'AACCTTGG'
#w = 'ACACTGTGA'
w = 'ATCGTCC'
v = 'ATGTTATA'

s1 = [0]*(len(w)+1)
s = []

for i in range(len(v)+1):
    s.append(s1.copy())

s2 = ['']*len(w)
backtrack = []
for i in range(len(v)):
    backtrack.append(s2.copy())

#print(backtrack)

def LCS_backtrack(v,w):
    for i in range(len(v)+1):
        s[i][0] = 0
    for j in range(len(w)+1):
        s[0][j] = 0
    for i in range(1,len(v)+1):
        for j in range(1,len(w)+1):
            if v[i-1] == w[j-1]:
                s[i][j] = max(s[i-1][j], s[i][j-1], s[i-1][j-1] + 1)
            else:
                s[i][j] = max(s[i-1][j], s[i][j-1])
            if s[i][j] == s[i-1][j]:
                backtrack[i-1][j-1] = 'down'
            elif s[i][j] == s[i][j-1]:
                backtrack[i-1][j-1] = 'hor'
            elif (s[i][j] == s[i-1][j-1] + 1) and (v[i-1] == w[j-1]):
                backtrack[i-1][j-1] = 'digo'
    for i in s:
        print(i)
    return backtrack

backtrack = LCS_backtrack(v,w)
for i in backtrack:
    print(i)
