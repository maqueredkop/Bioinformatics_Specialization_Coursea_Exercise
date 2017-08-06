
k = 5
d = 1

##################################################################################

def hamming_distance(text1, text2):
    distance = 0
    for i in range(len(text1)):
        if text1[i] != text2[i]:
            distance = distance + 1

    return distance

def pattern_count(text, pattern, d):
    position = []
    for i in range(len(text) - len(pattern) + 1):
        if hamming_distance(text[i : i+len(pattern)], pattern) <= d:
            position.append(i)
    
    return len(position)

##################################################################################

def immediate_neighbors(pattern):
    neighborhood = set()
    for i in range(len(pattern)):
        symbol = pattern[i]
        for nucleotide in ['A', 'C', 'G', 'T']:
            if nucleotide != symbol:
                neighbor = pattern[0:i] + nucleotide + pattern[i+1:]
                neighborhood.add(neighbor)


    return neighborhood


def iterative_neighbors(pattern, d):
    neighborhood = set()
    neighborhood.add(pattern)
    for i in range(1,d+1):
        for pattern in neighborhood:
            neighborhood = neighborhood.union(immediate_neighbors(pattern))
    return neighborhood


#################################################################################
dna = []
with open('dataset_156_8.txt', 'r') as f:
    for line in f:
        line = line.strip()
        dna.append(line)

def motif_enumeration(dna, k, d):
    patterns = set()
    candidate_pattern = set()
    for string in dna:
        for i in range(len(string)-k+1):
            candidate_pattern.add(string[i:i+k])

    all_possible_pattern = set()
    for pattern in candidate_pattern:
        all_possible_pattern = all_possible_pattern.union(iterative_neighbors(pattern, d))

    for pattern in all_possible_pattern:
        match_string_time = 0
        for string in dna:
            match_count = pattern_count(string, pattern, d)
            if match_count >= 1:
                match_string_time = match_string_time + 1

        if match_string_time == len(dna):
            patterns.add(pattern)

    #return patterns
    for i in patterns:
        print(i)


motif_enumeration(dna, k, d)
        
