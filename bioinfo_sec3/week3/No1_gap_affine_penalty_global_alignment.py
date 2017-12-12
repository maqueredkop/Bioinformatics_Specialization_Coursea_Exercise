# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 2017

@author: maque

Code Challenge: Solve the Alignment with Affine Gap Penalties Problem.
     Input: Two amino acid strings v and w (each of length at most 100).
     Output: The maximum alignment score between v and w, followed by an 
             alignment of v and w achieving this maximum score. Use the
     BLOSUM62 scoring matrix, a gap opening penalty of 11, and a gap extension penalty of 1.
"""

import sys
sys.setrecursionlimit(1500)

score_matrix = dict()
with open('BLOSUM62.txt','r') as f:
    amino_acid = next(f).strip().split()
    
    for line in f:
        line = line.strip().split()
        score = [int(x) for x in line[1:]]
        score_matrix[line[0]] = score

def get_score(amino1, amino2):
    return int(score_matrix[amino1][amino_acid.index(amino2)])

#print(get_score('F','A'))

##########################################################################
## construct the score matrix

#v = 'PRTEINS'
#w = 'PRTWPSEIN'

#v = 'AHRQPQ'
#w = 'AHED'

#v = 'YHFDVPDCWAHRYWVENPQAIAQMEQICFNWFPSMMMKQPHVFKVDHHMSCRWLPIRGKKCSSCCTRMRVRTVWE'
#w = 'YHEDVAHEDAIAQMVNTFGFVWQICLNQFPSMMMKIYWIAVLSAHVADRKTWSKHMSCRWLPIISATCARMRVRTVWE'

v = 'WERRWLAISKPGYAYDSVFWDGAKQVREKQRDALPKETGTMDRCLFCIERDPMWSNMRYSDIDWCSMWRGLS'
w = 'WERWISSWCQWLWLAISKPGYAYDSVFWDGAKQRDALPKETGTMDRCLFCIERDVMWCPMREPKLQVWRGLS'

gap_open = 11
gap_ext = 1

## construct M matrix
M = []
for i in range(len(v)+1):
    M.append([0]*(len(w)+1))
 
for i in range(1,len(w)+1):
    M[0][i] = -float('inf')

for j in range(1,len(v)+1):
    M[j][0] = -float('inf')

## construct I matrix
I = []
for i in range(len(v)+1):
    I.append([0]*(len(w)+1))

for i in range(len(w)+1):
    I[0][i] = -float('inf')

for j in range(1,len(v)+1):
    I[j][0] = -gap_open - (j-1)*gap_ext
    
## construct J matrix
J = []
for i in range(len(v)+1):
    J.append([0]*(len(w)+1))

for i in range(1,len(w)+1):
    J[0][i] = -gap_open - (i-1)*gap_ext

for j in range(len(v)+1):
    J[j][0] = -float('inf')
        
## construct the backtrack matrix

M_bt = []
for i in range(len(v)+1):
    M_bt.append(['']*(len(w)+1))

M_bt[0][0] = 'start'

for i in range(1,len(v)+1):
    M_bt[i][0] = 'I'
for i in range(1,len(w)+1):
    M_bt[0][i] = 'J'

I_bt = []
for i in range(len(v)+1):
    I_bt.append(['']*(len(w)+1))

I_bt[1][0] = 'go'
for i in range(2,len(v)+1):
    I_bt[i][0] = 'ge'
        
J_bt = []
for i in range(len(v)+1):
    J_bt.append(['']*(len(w)+1))

J_bt[0][1] = 'go'
for i in range(2,len(w)+1):
    J_bt[0][i] = 'ge'
    
V_bt = []
for i in range(len(v)+1):
    V_bt.append(['']*(len(w)+1))
    
V_bt[1][0] = 'go'
for i in range(2,len(v)+1):
    V_bt[i][0] = 'ge'

V_bt[0][1] = 'go'
for i in range(2,len(w)+1):
    V_bt[0][i] = 'ge'
    
################################################################
### fill the score matrix and backtrack matrix

for i in range(1, len(v)+1):
    for j in range(1, len(w)+1):
        I[i][j] = max(M[i-1][j] - gap_open, I[i-1][j] - gap_ext)
        J[i][j] = max(M[i][j-1] - gap_open, J[i][j-1] - gap_ext)
        M[i][j] = max(M[i-1][j-1] + get_score(v[i-1],w[j-1]),
                      I[i][j],
                      J[i][j])
        
        if M[i][j] == M[i-1][j-1] + get_score(v[i-1],w[j-1]):
            M_bt[i][j] = 'match'
        elif M[i][j] == I[i][j]:
            M_bt[i][j] = 'I'
        elif M[i][j] == J[i][j]:
            M_bt[i][j] = 'J'
        
        if I[i][j] == M[i-1][j] - gap_open:
            I_bt[i][j] = 'go'
        elif I[i][j] == I[i-1][j] - gap_ext:
            I_bt[i][j] = 'ge'
            
        if J[i][j] == M[i][j-1] - gap_open:
            J_bt[i][j] = 'go'
        elif J[i][j] == J[i][j-1] - gap_ext:
            J_bt[i][j] = 'ge'
        
'''
for i in range(len(V_bt)):
    print(V_bt[i])
print('#########################################################')
for i in range(len(M_bt)):
    print(M_bt[i])
print('#########################################################')
for i in range(len(I_bt)):
    print(I_bt[i])
print('#########################################################')
for i in range(len(J_bt)):
    print(J_bt[i])    
'''          

#####################################################################
## output the alignment 

v_len = len(v)
w_len = len(w)

v_align = []
w_align = []

def output_M(M_bt,v_len,w_len):
    if v_len == 0 and w_len == 0:
        return ''
    elif M_bt[v_len][w_len] == 'match':
        v_align.append(v[v_len-1])
        w_align.append(w[w_len-1])
        return output_M(M_bt, v_len-1, w_len-1)
    elif M_bt[v_len][w_len] == 'I':
        return output_I(I_bt, v_len, w_len)
    elif M_bt[v_len][w_len] == 'J':
        return output_J(J_bt, v_len, w_len)
         
def output_I(I_bt,v_len,w_len):
    if v_len == 0 and w_len == 0:
        return ''
    elif I_bt[v_len][w_len] == 'ge':
        v_align.append(v[v_len-1])
        w_align.append('-')
        return output_I(I_bt, v_len-1, w_len)
    elif I_bt[v_len][w_len] == 'go':
        v_align.append(v[v_len-1])
        w_align.append('-')
        return output_M(M_bt,v_len-1, w_len)
      
def output_J(J_bt, v_len,w_len):
    if v_len == 0 and w_len == 0:
        return ''
    elif J_bt[v_len][w_len] == 'ge':
        v_align.append('-')
        w_align.append(w[w_len-1])
        return output_J(J_bt,v_len, w_len-1)
    elif J_bt[v_len][w_len] == 'go':
        v_align.append('-')
        w_align.append(w[w_len-1])
        return output_M(M_bt, v_len, w_len-1)
    
    
output_M(M_bt,v_len,w_len)             
        
print(M[v_len][w_len])
print(''.join(v_align[::-1]))
print(''.join(w_align[::-1]))

