
text = 'AAGTCTAAGTCTATTCAGAGAAGTCTCTCTAAGTCTCTAGTCTCTAAGTCTAGTCATTCTCAGAAGAAGAAGAGTCAGAAGTCTTCTAGAAGAGATTCTTCTCATAAGTCTAAGATTCAAGTCAGTCAAGTCTTCATATAGATTCTAGAAGTCTCTCTATTCTAGAAGATATAGAAGAGTCTATATTCTTCTTCAGTCAGTCATAGTCTATTCAAGATAGAGTCTATTCT'
d = 3
k = 6

############################################################################

base_comple = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}

def reverse_complement(dna):
    dna_comple = ''
    for i in dna:
        i_comple = base_comple[i]
        dna_comple = dna_comple + i_comple

    dna_reverse_comple = dna_comple[::-1]

    return dna_reverse_comple

############################################################################

symbol_to_number = dict()
symbol_to_number['A'] = 0
symbol_to_number['C'] = 1
symbol_to_number['G'] = 2
symbol_to_number['T'] = 3

def pattern_to_number(pattern):
    if len(pattern) == 0:
        return 0
    symbol = pattern[-1]
    prefix = pattern[:-1]
    return 4 * pattern_to_number(prefix) + symbol_to_number[symbol]

############################################################################

number_to_symbol = ['A', 'C', 'G', 'T']

def number_to_pattern(index, k, pattern=None):
    if pattern is None:
        pattern = []
    if k == 1:
        symbol = number_to_symbol[index]
        pattern.append(symbol)

    else:
        prefix_index = int(index) // 4
        r = int(index) % 4
        symbol = number_to_symbol[r]
    
        pattern.append(symbol)

        prefix_pattern = number_to_pattern(prefix_index, k - 1, pattern)

        patt = ''.join(pattern)
        patt = ''.join(reversed(patt))
    
        return patt


############################################################################

def hamming_distance(text1, text2):
    distance = 0
    for i in range(len(text1)):
        if text1[i] != text2[i]:
            distance = distance + 1

    return distance

def pattern_count(text, pattern):
    position = []
    for i in range(len(text) - len(pattern) + 1):
        if hamming_distance(text[i : i+len(pattern)], pattern) <= d:
            position.append(i)
    
    return len(position)

############################################################################

def immediate_neighbors(pattern):
    neighborhood = set()
    for i in range(len(pattern)):
        symbol = pattern[i]
        for nucleotide in ['A', 'C', 'G', 'T']:
            if nucleotide != symbol:
                neighbor = pattern[0:i] + nucleotide + pattern[i+1:]
                neighborhood.add(neighbor)

    return neighborhood


def iterative_neighbors(pattern,d):
    neighborhood = set()
    neighborhood.add(pattern)
    for i in range(1,d+1):
        for pattern in neighborhood:
            neighborhood = neighborhood.union(immediate_neighbors(pattern))
    return neighborhood

###############################################################################

def frequent_words_with_mismatches(text, d, k):
    all_candidate_pattern = set()
    frequency_array = []
    for i in range(4**k):
        frequency_array.append(0)
    
    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        all_candidate_pattern = all_candidate_pattern.union(iterative_neighbors(pattern, d))
    
    for pattern in all_candidate_pattern:
        pattern_reverse_complement = reverse_complement(pattern)
        pattern_index = pattern_to_number(pattern)
        frequency_array[pattern_index] = pattern_count(text, pattern) + pattern_count(text, pattern_reverse_complement)
    
    max_count = max(frequency_array)
    
    pattern_list = []
    
    for i in range(4**k):
        if frequency_array[i] == max_count:
            pattern = number_to_pattern(i, k)
            pattern_list.append(pattern)

    return pattern_list


#print(frequent_words_with_mismatches(text, d, k))
pattern_list = frequent_words_with_mismatches(text, d, k)
for i in pattern_list:
    print(i)

   
