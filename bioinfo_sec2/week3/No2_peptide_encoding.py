'''
Peptide Encoding Problem: Find substrings of a genome encoding a given amino acid sequence.
     Input: A DNA string Text, an amino acid string Peptide, and the array GeneticCode.
     Output: All substrings of Text encoding Peptide (if any such substrings exist).
'''


############################################################################
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

############################################################################

#dna_seq = 'ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA'
#dna_seq = open('peptide_encoding.txt','r').read().strip()
#dna_seq = open('dataset_96_7.txt','r').read().strip()
dna_seq = ''
with open('Bacillus_brevis.txt','r') as f:
    for line in f:
        line = line.strip()
        dna_seq = dna_seq + line

#peptide_seq = 'MA'
#peptide_seq = 'KEVFEPHYY'
#peptide_seq = 'IMNDHTCYME'
peptide_seq = 'VKLFPWFNQY'

def protein_translation(rna_seq):
    protein_seq = ''
    for i in range(0,len(rna_seq),3):
        codon = rna_seq[i:i+3]
        amino = codon_table[codon]
        protein_seq = protein_seq + amino

    return protein_seq

##############################################################################

base_comple = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}

def reverse_complement(dna):
    dna_comple = ''
    for i in dna:
        i_comple = base_comple[i]
        dna_comple = dna_comple + i_comple
    dna_reverse_comple = dna_comple[::-1]

    return dna_reverse_comple

##############################################################################

def peptide_encoding(dna_seq, peptide_seq):
    k = 3 * len(peptide_seq)
    substring_list = []
    for i in range(len(dna_seq)-k+1):
        substring_dna = dna_seq[i:i+k]
        substring_rna = substring_dna.replace('T','U')
        aminos = protein_translation(substring_rna)

        substring_dna_rc = reverse_complement(substring_dna)
        substring_rna_rc = substring_dna_rc.replace('T','U')
        aminos_rc = protein_translation(substring_rna_rc)

        if aminos == peptide_seq or aminos_rc == peptide_seq:
            substring_list.append(substring_dna)

    return substring_list


substring_list = peptide_encoding(dna_seq, peptide_seq)
print(len(substring_list))
for i in substring_list:
    print(i)


