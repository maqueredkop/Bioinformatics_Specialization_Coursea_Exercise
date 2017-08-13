

'''
String Spelled by a Genome Path Problem. Reconstruct a string from its genome path.
     Input: A sequence of k-mers Pattern1, … ,Patternn such that the last k - 1 symbols of Patterni are equal to the first k-1 symbols
                of Patterni+1 for 1 ≤ i ≤ n-1.
     Output: A string Text of length k+n-1 such that the i-th k-mer in Text is equal to Patterni  (for 1 ≤ i ≤ n).

'''

genome_path = []
with open('dataset_198_3.txt', 'r') as f:
    for line in f:
        genome_path.append(line.strip())


def string_spelled_by_genome_path(genome_path):
    string = genome_path[0]
    for i in genome_path[1:]:
        string = string + i[-1]

    return string

print(string_spelled_by_genome_path(genome_path))
    
