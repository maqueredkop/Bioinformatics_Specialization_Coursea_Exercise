
#text = 'AGGTGTGTGTATGTGTGTTGTGTGTTCCTGTGTGTCTCTGTGTGTCTGTGTGTTTGGTGTGTGTAGTGTGTGTTGTGTGTTAAGGAGTGTGTGTCTCGATACAACATGTGTGTCTTGTGTG'

genome_file = 'Vibrio_cholerae.txt'

text = open(genome_file, 'r').read().strip()

pattern = 'CTTGATCAT'


def pattern_count(text, pattern):
    position = []
    for i in range(len(text) - len(pattern) + 1):
        if text[i : i+len(pattern)] == pattern:
            position.append(i)
    
    position = str(position).replace(',', '')
    return position


print(pattern_count(text, pattern))


