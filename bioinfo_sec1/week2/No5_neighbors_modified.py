

def hamming_distance(text1, text2):
    distance = 0
    for i in range(len(text1)):
        if text1[i] != text2[i]:
            distance = distance + 1

    return distance

pattern = 'TACTTCCC'

def neighbors(pattern, d):
    if d == 0:
        return set(pattern)
    if len(pattern) == 1:
        return set(['A','C','G','T'])
    neighborhood = set()
    
    suffix_pattern = pattern[1:]
    suffix_neighbors = neighbors(suffix_pattern, d)
    #print(suffix_neighbors)
    for text in suffix_neighbors:
        if hamming_distance(suffix_pattern, text) == d-1:
            for nucleotide in ['A','C','G','T']:
                neighborhood.add(nucleotide + text)
        if hamming_distance(suffix_pattern, text) == d:
            neighborhood.add(pattern[0] + text)

    return neighborhood
    #for i in neighborhood:
     #   print(i)


neighbors = neighbors(pattern, d=2)

for i in neighbors:
    print(i)
