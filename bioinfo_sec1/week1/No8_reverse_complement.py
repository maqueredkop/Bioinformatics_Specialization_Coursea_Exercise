
dna = 'TGTTGGCATCCTTCAGGAACTTAACACAAGCCTACTAGTGAATTCTGCTCCACGTTAATTTATATGATGGCAGGATAGTTCGCAATGAGAGTCTTGACTATT'

base_comple = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}

def reverse_complement(dna):
    dna_comple = ''
    for i in dna:
        i_comple = base_comple[i]
        dna_comple = dna_comple + i_comple

    dna_reverse_comple = dna_comple[::-1]

    return dna_reverse_comple


print(reverse_complement(dna))
        
    
    
