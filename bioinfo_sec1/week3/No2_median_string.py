
k = 6

with open('dataset_158_9.txt','r') as f:
    dna = []
    for line in f.readlines():
        line = line.strip()
        dna.append(line)
##################################################################################

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


##################################################################################

def hamming_distance(text1, text2):
    distance = 0
    for i in range(len(text1)):
        if text1[i] != text2[i]:
            distance = distance + 1

    return distance

def min_hamming_distance(pattern, text):
    hamming_distance_list = []
    for i in range(len(text)-k + 1):
        distance = hamming_distance(pattern, text[i:i+k])
        hamming_distance_list.append(distance)
    return min(hamming_distance_list)


def sum_distance(pattern, dna):
    sum_distance = 0
    for string in dna:
        sum_distance = sum_distance + min_hamming_distance(pattern, string)

    return sum_distance


def median_string(dna, k):
    
    distance = float('inf')
    
    for i in range(4**k):
        pattern = number_to_pattern(i, k)
        if distance > sum_distance(pattern, dna):
            distance = sum_distance(pattern, dna)
            median = pattern

    return median
        

print(median_string(dna, k))
