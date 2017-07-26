#text = 'ATCGCAGCAGAATGACTAACCCAGACATGTGGTGCTCTCTCGTGACCGCTGACTAGTTCGCAGCCTTCAACGTGGATGTGGCGTGCTCGCTAACTGAGACCAAGTAAAAAATGAATATGCAACCTTGGACGTAATGCAGGACGTTAGACCCAAGAACGACGATTTGAAGCCTCTGTCGCGCCGTCGAACAGCCGTTAGGTTTGCTGGGCAACTGACAAAAAACTACTTTAAGTTAACAAGGGCGACGCGGGACCATTTGCACATGTTTGTTGATCAAACGCCAAAGTGCGACTGGTGGCGTCCATAGGTATTTTAAGTTTCGGCTCTTTGGCATCACTGTCAAAATTATATATCCAAATCTTCTTGGCCAGGTCGTTGGAGGCACTTCGGCAAGAAAGAGGGCATAGACGTGGAGGACCCCGAAGCGTATGTGCACTGCGCTACTGCCCTCGTCACCATGTAGGGACGACCCGGCAGTATGAATCACAAAAGGATGGTATGGTAGGGGACACCCTGGTTGATGTCTAGTAGACCAGTGCTCTCTGCGTTGTTTCATAATGTCCAATTCAACGTGTAGCAAAAAATCTCACCTAGGCCACGGCCGTTAATCCGCACCCCGTAGGACGGTACTGTTGTGCCCCGACATTTTGAAAATGCATAGTT'

#text = 'AGCAAAGGTGGGC'
text = 'GCAAAGGTGGGCG'
k = 3

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
    return str(frequency_array).replace(',', ' ')

print(computing_frequencies(text, k))

