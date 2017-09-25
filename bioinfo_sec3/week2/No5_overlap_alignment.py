'''
Code Challenge: Solve the Fitting Alignment Problem.
     Input: Two nucleotide strings v and w, where v has length at most 1000 and w has length at most 100.
     Output: A highest-scoring fitting alignment between v and w. Use the simple scoring method in which matches count +1 and both the
     mismatch and indel penalties are 1.
'''

import sys
sys.setrecursionlimit(1500)

#v = 'PAWHEAE'
#w = 'HEAGAWGHEE'

#v = 'GCTATAAGAATAAACCACTAGATCACCTCCGGCTCGCTCACTCCTGATCATGGTTCGTGCTAACATCGCGCCGCGCTGACGCCGAATCGTTCGTAGGAGACAAGTCGACGACCTCATCTACAGGCAAAAGTTAAATTAGCTCTCGGCTAGATGTGACAATCGGAACCCTGCACCCTGCGTAATAGGGTAAATAGTCGGGAGTTGATGCACACACCTAGATATTGGCTGAATGACAGACTGCCATTCCTGCACTGGAAAGTAGAGTGCATATGTTTCGTGAGATTATGCAGGCTCTACGGTTATACTGGGCTCCACGGATTCGACCGGTACTGTTGATTGAAGACTCTTCTATAGAGGCTCTAACCGCGGAGGCCGCAACCAATCGACAATGAAGCACCCGTCGTCGGTATCGTTGGGAAGGACGACACCGTAAGGGCAGACTTTATCGTGACCCGTCTGCTTGCTAGAAAAGCCCTGGCGTTTGTACAACGTCCGTGCAGAATTAGCGTTTTTCTCAGGAAAGATGAGGGGGTTGATCATCATCTCGTTTCGCACGGGTCAAGCGCATTTTCCTACTGTTTTGGACACAGTACGTCTTCCACTGATCTCATACGGACATTACCAGCACCCTTTTGTACCTGTCGTAACTTGTGCCATTCTAGGCCCGTTTTCACTTGCGCTTATGATCATGGTTCCGCTGATCTATATGGGCCGGGTAGGGCACTCCCAGATGAAGGGGAGTAATGGTAGCCGGATCCAAGTGACGCGCCCTAGCGGCTCCGGAGTTTGATAGACGTCGTGCTATGGAGCGTTGGAGCGACAACGCGCTCGTGCTCTGGAAGGTCGCTGCTGATCCGTAA'
#w = 'TACTGGTCCTGACCCACCTCACTTTGATGTCCCCTTTTCTCGTTTGCGCATCAAGATCTGGCCCGCAACTATTGGCCGTGAAAGGCACTCATCAATAAAGACAGTACTCACGCGGTCGGATCCAAATGCGCGCACCGAGCGGCCCAGGAGTTGATAGCGTCGAGTAACCTATTAGGACTCGAGGCAACTCGCGCTCTCTCAGGAGGCTCGCCTGCTAGTCCGTGAACGACGGATCTTTGGTGCTGCCTTCCTATCATGACATTGCCTAATAACGAGCGGCACCTACTCCCAGGTCTTTGAAGGGATGGCTTGTTTACCCCGATTCCGAGAAATAGAGATGACTCCTAAGGAAGTAATGAAGGAAGTTCAGTGGTATGGGTATCGTTTAGTTTGCCAGGGAGATTGCCCATAACCTAAGTCCCTAATACAGCAGTAGATCTCACCATAGATGTAGGAAAGCACAGTGATTTAGACGCTTAGCCAAATACAAAGGAATGTACCCCCTCCTAACACTGAGCACCGCTTATTTACTAGTATACTCAGAGTGTGGAGCGCTGAACGTTGTGTCAACAAGAACATAAGCCGCCGTGAATGAATTTGTGAAGGGGAGTGATCATGGTTTTACTCGTGGTAGATTTGGGCAGAACCTGATTCCTCACGTGTGAATGTAATTGAAGCTGACTCCCACACATACAGGCACGATTCTTTTAGATGATGTTTTAGGAAGCGCATTTCGTATTAACACTGCCTTGCATTTGATAACCATCACTTGTTCATTACATGATCCCATAGGGCCGTGTTGTTACTTTCGTGTTAGTCGAGCAGTATGACCACCTTTTCGGCGCTTGATATGCCTCAAGACGTGCGATTCAAGGAATCAAACAAATGAACGCCGCACTGGATGACTGGG'

a = 2 

with open('dataset_248_7.txt','r') as f:
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
        #s[i][0] = s[i-1][0] - a
        s[i][0] = 0
    for j in range(1,len(w)+1):
        s[0][j] = s[0][j-1] - a
    for i in range(1,len(v)+1):
        for j in range(1,len(w)+1):
            if v[i-1] == w[j-1]:
                s[i][j] = max(s[i-1][j]-a, s[i][j-1]-a, s[i-1][j-1] + 1)
            else:
                s[i][j] = max(s[i-1][j]-a, s[i][j-1]-a, s[i-1][j-1] -a)
            if s[i][j] == s[i-1][j] - a:
                backtrack[i][j] = 'down'
            elif s[i][j] == s[i][j-1] -a:
                backtrack[i][j] = 'hor'
            elif (s[i][j] == s[i-1][j-1] + 1) and (v[i-1] == w[j-1]):
                backtrack[i][j] = 'digo'
            elif (s[i][j] == s[i-1][j-1] -a) and (v[i-1] != w[j-1]):
                backtrack[i][j] = 'digo_mis'
     
    #for i in s:
    #    print(i)
    
    #s_max = 0
    s_below = []
    for i in range(1,len(w)+1):
        s_below.append(s[len(v)][i])
    
    print(max(s_below))

    for i in range(1,len(w)+1):
        if s[len(v)][i] == max(s_below):
            m = len(v)
            n = i

    return [backtrack,m,n]
    
    
#backtrack = LCS_backtrack(v,w)


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
    if n == 0:
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

