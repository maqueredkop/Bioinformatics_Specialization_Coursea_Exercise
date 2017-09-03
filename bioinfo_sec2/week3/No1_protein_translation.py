
'''
Protein Translation Problem: Translate an RNA string into an amino acid string.
     Input: An RNA string Pattern and the array GeneticCode.
     Output: The translation of Pattern into an amino acid string Peptide.
'''

codon_table = dict()
with open('RNA_codon_table_1.txt','r') as f:
    for line in f:
        line = line.strip()
        line = line.split()
        codon = line[0].strip()
        if len(line) == 2:
            amino = line[1].strip()
        elif len(line) == 1:
            amino = ''
        codon_table[codon] = amino

#print(codon_table)

#seq = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
seq = open('dataset_96_4.txt','r').read().strip()

def protein_translation(rna_seq):
    protein_seq = ''
    for i in range(0,len(rna_seq),3):
        codon = rna_seq[i:i+3]
        amino = codon_table[codon]
        protein_seq = protein_seq + amino

    return protein_seq

print(protein_translation(seq))
    
