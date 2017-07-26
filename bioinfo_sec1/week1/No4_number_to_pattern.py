

number_to_symbol = ['A', 'C', 'G', 'T']

index = 520
k = 5

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

print(number_to_pattern(index, k))


