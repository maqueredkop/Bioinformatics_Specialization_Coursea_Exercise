
text = 'GCACTTCTCGTAGGTGACCATTCGCACTTCTGCACTTCTAACAGCGCCAACAGCGCCCGTAGGTGGCACTTCTCGTAGGTGACCATTCACCATTCCGTAGGTGAACAGCGCCAACAGCGCCCGTAGGTGCGTAGGTGACCATTCACCATTCAACAGCGCCATAGCATCAACAGCGCCGCACTTCTACCATTCCGTAGGTGCGTAGGTGCGTAGGTGATAGCATCACCATTCCGTAGGTGATAGCATCCGTAGGTGAACAGCGCCACCATTCATAGCATCATAGCATCGCACTTCTCGTAGGTGGCACTTCTATAGCATCCGTAGGTGATAGCATCAACAGCGCCATAGCATCGCACTTCTCGTAGGTGGCACTTCTCGTAGGTGATAGCATCAACAGCGCCATAGCATCCGTAGGTGCGTAGGTGACCATTCAACAGCGCCACCATTCAACAGCGCCATAGCATCATAGCATCAACAGCGCCAACAGCGCCATAGCATCATAGCATCACCATTCATAGCATCGCACTTCTATAGCATCATAGCATCAACAGCGCCCGTAGGTGACCATTCATAGCATCGCACTTCTCGTAGGTGACCATTCCGTAGGTGCGTAGGTGGCACTTCTATAGCATCCGTAGGTGACCATTCACCATTCATAGCATCGCACTTCTACCATTCAACAGCGCCACCATTCATAGCATCCGTAGGTGATAGCATCATAGCATCCGTAGGTGCGTAGGTGCGTAGGTGCGTAGGTGCGTAGGTGCGTAGGTGAACAGCGCCATAGCATCGCACTTCTAACAGCGCCATAGCATCATAGCATC'
k = 11

symbol_to_number = dict()
symbol_to_number['A'] = 0
symbol_to_number['C'] = 1
symbol_to_number['G'] = 2
symbol_to_number['T'] = 3

number_to_symbol = ['A', 'C', 'G', 'T']

#index = 5871

#pattern = []

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
        #pattern.reverse()
        return patt

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


def faster_frequent_words(text, k):
    frequent_patterns = set()
    frequency_array =  computing_frequencies(text, k)
    max_count = max(frequency_array)
    #print(max_count)

    for i in range(4**k):
        if frequency_array[i] == max_count:
            print(i)
            patterns = number_to_pattern(i, k)
            print(patterns)
            frequent_patterns.add(patterns)
    return frequent_patterns

print(faster_frequent_words(text, k))



