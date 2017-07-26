
#genome = 'CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA'
genome = open('dataset_4_5.txt').read().strip()
#genome = genome[1:10000]

#############################################################
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


def computing_frequencies(text, k):
    frequency_array = []
    for i in range(4**k):
        frequency_array.append(0)
    for i in range(len(text) - k + 1):
        pattern = text[i : i+k]
        j = pattern_to_number(pattern)
        frequency_array[j] = frequency_array[j] + 1
    return frequency_array


#############################################################
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


#############################################################

def clump_finding(genome, k, t, L):
    frequent_pattern = set()
    clump = []
    for i in range(4**k):
        clump.append(0)
    for i in range(len(genome) - L + 1):
        text = genome[i : i + L]
        frequency_array = computing_frequencies(text, k)
        for index in range(4**k):
            if frequency_array[index] >= t:
                clump[index] = 1
    for i in range(4**k):
        if clump[i] == 1:
            pattern = number_to_pattern(i, k)
            frequent_pattern.add(pattern)
    
    return frequent_pattern

print(clump_finding(genome, k=11, t=19, L=489))
        
