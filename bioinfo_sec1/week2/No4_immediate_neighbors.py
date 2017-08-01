
pattern = 'TCGGGAC'

def immediate_neighbors(pattern):
    neighborhood = set()
    for i in range(len(pattern)):
        symbol = pattern[i]
        for nucleotide in ['A', 'C', 'G', 'T']:
            if nucleotide != symbol:
                neighbor = pattern[0:i] + nucleotide + pattern[i+1:]
                neighborhood.add(neighbor)


    return neighborhood


print(immediate_neighbors(pattern))
