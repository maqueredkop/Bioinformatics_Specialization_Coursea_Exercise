
k = 12
t = 25

with open('dataset_160_9.txt','r') as f:
    dna = []
    for line in f:
        line = line.strip()
        dna.append(line)

###############################################################################

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
        
###############################################################################

def profile_most_probable(text, k, profile_matrix):
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

    max_probable = max(probable_list)
    max_probable_index = probable_list.index(max_probable)
    pattern = pattern_list[max_probable_index]

    return pattern

###############################################################################

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

###############################################################################

def greedy_motif_search(dna, k, t):
    best_motif = []
    for string in dna:
        first_motif = string[0:k]
        best_motif.append(first_motif)
    for i in range(len(dna[0])-k+1):
        motif = dna[0][i:i+k]
        motif_list = []
        motif_list.append(motif)
        for i in range(1,t):
            profile_matrix = motif_profile_forming(motif_list)
            motif = profile_most_probable(dna[i], k, profile_matrix)
            motif_list.append(motif)
        if matrix_score(motif_list) < matrix_score(best_motif):
            best_motif = motif_list

    return best_motif


        
best_motif = greedy_motif_search(dna, k, t)
for i in best_motif:
    print(i)
    
