

'''
Code Challenge: Implement StringSpelledByGappedPatterns.
     Input: Integers k and d followed by a sequence of (k, d)-mers (a1|b1), … , (an|bn) such that Suffix(ai|bi) = Prefix(ai+1|bi+1) for 1 ≤ i ≤ n-1.
     Output: A string Text of length k + d + k + n - 1 such that the i-th (k, d)-mer in Text is equal to (ai|bi)  for 1 ≤ i ≤ n (if such a string
     exists).

'''
k = 50
d = 200
gapped_patterns = []

#with open('test4.txt','r') as f:
#with open('GappedGenomePathString.txt','r') as f:
with open('dataset_6206_7.txt','r') as f:
    for line in f:
        line = line.strip()
        gapped_patterns.append(line)

def string_from_pattern(patterns):
    string = ''
    for i in patterns[:-1]:
        string = string + i[0]
    string = string + patterns[-1]
    
    return string

def string_spelled_by_gapped_patterns(gapped_patterns, k, d):
    first_patterns = []
    second_patterns = []
    for pattern in gapped_patterns:
        pattern = pattern.split('|')
        first_patterns.append(pattern[0].strip())
        second_patterns.append(pattern[1].strip())

    prefix_string = string_from_pattern(first_patterns)
    suffix_string = string_from_pattern(second_patterns)

    for i in range(k+d, len(prefix_string)):
        if prefix_string[i] != suffix_string[i-k-d]:
            return "there is no string spelled by gapped patterns"
    return prefix_string + suffix_string[len(suffix_string)-k-d : ]


print(string_spelled_by_gapped_patterns(gapped_patterns, k, d))
