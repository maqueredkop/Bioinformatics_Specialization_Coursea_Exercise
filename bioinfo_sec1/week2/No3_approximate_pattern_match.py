

def hamming_distance(text1, text2):
    distance = 0
    for i in range(len(text1)):
        if text1[i] != text2[i]:
            distance = distance + 1

    return distance


############################################################


text = 'TTGTCACATCCGAAGAGTTCCCGTTTTCAGGATGTCCAGTATAAGAATAAGAGAGAAAGCGGGTTGCTTATCCCAGGGCAGTCACATGATCGATGACTATGATATTCAGGGTGATTGCCAGTTCGTAAAGGATAGGTTCTCGGTGCGTTTAACCGCTCATCCGTGAGTCCTGCTCCACTTGATTTCTGATTGGCCTAACGACCCCAGTTGGCCGAGCAGTGGCAGGATTCCGAGGGGACAATAACATTTGTCAGCGATGGCCCGTAGGTAGTCCTAGGTGTCTCTATATGCATGGGAAGGTTCGAGTGC'
#text = open('dataset_9_4.txt', 'r').read().strip()

pattern = 'GATAT'


def pattern_count(text, pattern, d):
    position = []
    for i in range(len(text) - len(pattern) + 1):
        if hamming_distance(text[i : i+len(pattern)], pattern) <= d:
            position.append(i)
    
    #position = str(position).replace(',', '')
    #return position
    return len(position)


print(pattern_count(text, pattern, d=2))


