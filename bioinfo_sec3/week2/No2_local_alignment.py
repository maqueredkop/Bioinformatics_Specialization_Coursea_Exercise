'''
Code Challenge: Solve the Local Alignment Problem.
     Input: Two protein strings written in the single-letter amino acid alphabet.
     Output: The maximum score of a local alignment of the strings, followed by a local alignment of these strings achieving the maximum
     score. Use the PAM250 scoring matrix and indel penalty σ = 5.
'''

import sys
sys.setrecursionlimit(1500)

score_matrix = dict()
with open('PAM250.txt','r') as f:
    amino_acid = next(f).strip().split()
    
    for line in f:
        line = line.strip().split()
        score = [int(x) for x in line[1:]]
        score_matrix[line[0]] = score

own_score = dict()
for i in amino_acid:
    score_list = score_matrix[i]
    index = amino_acid.index(i)
    score = score_list[index]
    own_score[i] = score

#v = 'MEANLYI'
#w = 'PENALTYA'

a = 5 

with open('dataset_247_10.txt','r') as f:
    v = next(f).strip()
    w = next(f).strip()

m = len(v)
n = len(w)

s1 = [0]*(len(w)+1)
s = []

for i in range(len(v)+1):
    s.append(s1.copy())

s2 = ['']*(len(w)+1)
backtrack = []
for i in range(len(v)+1):
    backtrack.append(s2.copy())

backtrack[0][0] = 'start'
for i in range(1,len(v)+1):
    backtrack[i][0] = 'down'
for i in range(1,len(w)+1):
    backtrack[0][i] = 'hor'

def LCS_backtrack(v,w):
    s[0][0] = 0
    for i in range(1,len(v)+1):
        s[i][0] = s[i-1][0] - a
    for j in range(1,len(w)+1):
        s[0][j] = s[0][j-1] - a
    for i in range(1,len(v)+1):
        for j in range(1,len(w)+1):
            if v[i-1] == w[j-1]:
                score_list = score_matrix[v[i-1]]
                index = amino_acid.index(v[i-1])
                score = score_list[index]
                s[i][j] = max(s[i-1][j]-a, s[i][j-1]-a, s[i-1][j-1] + score, 0)
            else:
                score_list = score_matrix[v[i-1]]
                index = amino_acid.index(w[j-1])
                penaty = score_list[index]
                s[i][j] = max(s[i-1][j]-a, s[i][j-1]-a, s[i-1][j-1] +  penaty, 0)
            if s[i][j] == s[i-1][j] - a:
                backtrack[i][j] = 'down'
            elif s[i][j] == s[i][j-1] -a:
                backtrack[i][j] = 'hor'
            elif (s[i][j] == s[i-1][j-1] + own_score[v[i-1]]) and (v[i-1] == w[j-1]):
                backtrack[i][j] = 'digo'
            elif (s[i][j] == s[i-1][j-1] + penaty) and (v[i-1] != w[j-1]):
                backtrack[i][j] = 'digo_mis'
            elif s[i][j] == 0:
                backtrack[i][j] = 'new_start'
     
    #for i in s:
    #    print(i)
    s_max = 0
    for i in range(1,len(v)+1):
        for j in range(1,len(w)+1):
            #print(s[i][j])
            if s[i][j] > s_max:
                s_max = s[i][j]
    print(s_max)
    for i in range(1,len(v)+1):
        for j in range(1,len(w)+1):
            if s[i][j] == s_max:
                #print(i)
                #print(j)
                m = i
                n = j                
    #print(s[len(v)][len(w)])
    return [backtrack,m,n]

result = LCS_backtrack(v,w)
backtrack = result[0]
m = result[1]
n = result[2]
    
v = v[:m]
w = w[:n]

align_v = []
align_w = []

v_list = list(v)
w_list = list(w)

def output_LCS(backtrack,v,w,v_list,w_list,m,n,lcs=[]):
    #if m == 0 or n == 0:
    if m == 0 and n == 0:
        return ''
    if backtrack[m][n] == 'down':
        align_v.append(v_list[-1])
        v_list.pop()
        align_w.append('-')
        output_LCS(backtrack,v,w,v_list,w_list,m-1,n)
    elif backtrack[m][n] == 'hor':
        align_v.append('-')
        align_w.append(w_list[-1])
        w_list.pop()
        output_LCS(backtrack,v,w,v_list,w_list,m,n-1)
    elif backtrack[m][n] == 'digo_mis':
        align_v.append(v_list[-1])
        v_list.pop()
        align_w.append(w_list[-1])
        w_list.pop()
        output_LCS(backtrack,v,w,v_list,w_list,m-1,n-1)
    elif backtrack[m][n] == 'new_start':
        pass
    else:
        align_v.append(v_list[-1])
        v_list.pop()
        align_w.append(w_list[-1])
        w_list.pop()
        output_LCS(backtrack,v,w,v_list,w_list,m-1,n-1)
        
        lcs.append(v[m-1])

    return [align_v,align_w]

align_result = output_LCS(backtrack,v,w,v_list,w_list,m,n)
align_v = align_result[0]
align_w = align_result[1]
align_v.reverse()
align_w.reverse()

print(''.join(align_v))
print(''.join(align_w))

'''
with open('new.txt','a') as f:
    f.write(''.join(align_v))
    f.write('\n')
    f.write(''.join(align_w))
    f.write('\n')
'''
