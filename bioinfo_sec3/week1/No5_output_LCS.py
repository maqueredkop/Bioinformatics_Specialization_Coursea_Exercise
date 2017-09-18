'''
Code Challenge: Use OutputLCS (reproduced below) to solve the Longest Common Subsequence Problem.
     Input: Two strings s and t.
     Output: A longest common subsequence of s and t. (Note: more than one solution may exist, in which case you may output any one.)
'''

import sys
sys.setrecursionlimit(1500)

#v = 'AACCTTGG'
#w = 'ACACTGTGA'

#with open('longest_common_subsequence.txt','r') as f:
with open('dataset_245_5.txt','r') as f:
    v = next(f).strip()
    w = next(f).strip()

i = len(v)
j = len(w)

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
    
    return backtrack

backtrack = LCS_backtrack(v,w)

def output_LCS(backtrack,v,i,j,lcs=[]):
    if i == 0 or j == 0:
        return ''
    if backtrack[i-1][j-1] == 'down':
        output_LCS(backtrack,v,i-1,j)
    elif backtrack[i-1][j-1] == 'hor':
        output_LCS(backtrack,v,i,j-1)
    else:
        output_LCS(backtrack,v,i-1,j-1)
        lcs.append(v[i-1])
        #print(v[i-1])
    return ''.join(lcs)

print(output_LCS(backtrack,v,i,j))

