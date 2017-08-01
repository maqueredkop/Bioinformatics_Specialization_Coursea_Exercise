
pattern = 'TACTTCCC'

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


print(iterative_neighbors(pattern, d=2))
