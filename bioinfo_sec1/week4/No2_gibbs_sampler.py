
import random
import numpy

k = 15
t = 10
N = 100
dna = []

with open('subtle_motif_dataset.txt', 'r') as f:
#with open('dataset_163_4.txt', 'r') as f:
#with open('gibbs.txt', 'r') as f:
    for line in f:
        line = line.strip()
        dna.append(line)

###################################################################################

def motif_profile_forming(motif_list):
    profile_matrix = []
    matrix = []
    for i in range(k):
        matrix.append(0)
    for i in range(4):
        profile_matrix.append(matrix.copy())
    
    for i in range(k):
        base_string = ''
        for j in motif_list:
            base_string = base_string + j[i]
        A_freq = (base_string.count('A') + 1) / (len(base_string) + 4)
        C_freq = (base_string.count('C') + 1) / (len(base_string) + 4)
        G_freq = (base_string.count('G') + 1) / (len(base_string) + 4)
        T_freq = (base_string.count('T') + 1) / (len(base_string) + 4)
        
        profile_matrix[0][i] = A_freq
        profile_matrix[1][i] = C_freq
        profile_matrix[2][i] = G_freq
        profile_matrix[3][i] = T_freq

    return profile_matrix

###################################################################################

def profile_random_kmer(text, k, profile_matrix):
    base_index = ['A','C','G','T']
    pattern_list = []
    probable_list = []
    
    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        pattern_list.append(pattern)        
        probable_sum = 1

        for j in range(k):
            base = pattern[j]
            base_nu = base_index.index(base)
            probable_sum = probable_sum*float(profile_matrix[base_nu][j])

        probable_list.append(probable_sum)
    
    sum_probable = sum(probable_list)
    
    probable_new_list = [(i / sum_probable) for i in probable_list]
    pattern = numpy.random.choice(pattern_list, p = probable_new_list)
    
    return pattern


###################################################################################

def matrix_score(motif_list):
    score = 0
    for i in range(k):
        motif_string = ''
        for j in motif_list:
            motif_string = motif_string + j[i]
        A_count = motif_string.count('A')
        C_count = motif_string.count('C')
        G_count = motif_string.count('G')
        T_count = motif_string.count('T')
        
        max_count = max(A_count, C_count, G_count, T_count)
        score = score + t - max_count

    return score

###################################################################################

def gibbs_sampler(dna, k, t, N):
    motifs = []
    for i in dna:
        random_index = random.choice(range(len(i)-k+1))
        motif = i[random_index:random_index+k]
        motifs.append(motif)
    best_motifs = motifs.copy()
    
    for j in range(1,N+1):
        i = random.choice(range(t))
        motifs.remove(motifs[i])
        profile = motif_profile_forming(motifs)

        motif = profile_random_kmer(dna[i], k, profile)
        motifs.insert(i, motif)

        if matrix_score(motifs) < matrix_score(best_motifs):
            best_motifs = motifs
    
    return [best_motifs, matrix_score(best_motifs)]
    


motif_list = []
motif_score = []
for i in range(10000):
    result = gibbs_sampler(dna, k, t, N)
    motif_list.append(result[0])
    motif_score.append(result[1])

min_score = min(motif_score)

print(min_score)
motif_index = motif_score.index(min_score)

best_motif = motif_list[motif_index]

for i in best_motif:
    print(i)


