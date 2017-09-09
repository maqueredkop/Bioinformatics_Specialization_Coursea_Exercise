
'''
Cyclopeptide Scoring Problem: Compute the score of a cyclic peptide against a spectrum.
     Input: An amino acid string Peptide and a collection of integers Spectrum.
     Output: The score of Peptide against Spectrum, Score(Peptide, Spectrum).
'''

#peptide = 'NQEL'
#peptide = 'VYYEVDWTMGRQIDPDEYPIAQCTRHRATILTLPDWQM'
peptide = 'WLTCWVKEDEEKWLLLDSHMSMFVVVGRILSQTYR'
#spectrum = [0,99,113,114,128,227,257,299,355,356,370,371,484]
#spectrum = open('cyclopeptide_scoring.txt','r').read().split()
spectrum = open('dataset_102_3.txt','r').read().strip().split()
spectrum = [int(x) for x in spectrum]
spectrum.sort()

amino_acid_mass = {'G':57,'A':71,'S':87,'P':97,'V':99,'T':101,'C':103,'I':113,'L':113,
                   'N':114,'D':115,'K':128,'Q':128,'E':129,'M':131,'H':137,'F':147,
                   'R':156,'Y':163,'W':186}

def cyclic_spectrum(peptide, amino_acid_mass):
    prefix_mass = [0]
    for i in range(len(peptide)):
        amino = peptide[i]
        amino_mass = amino_acid_mass[amino]
        prefix_mass.append(prefix_mass[i] + amino_mass)

    peptide_mass = prefix_mass[-1]
    cyclic_spectrum = [0]
    for i in range(len(peptide)):
        for j in range(i+1, len(peptide)+1):
            cyclic_spectrum.append(prefix_mass[j] - prefix_mass[i])
            if i > 0 and j < len(peptide):
                cyclic_spectrum.append(peptide_mass - (prefix_mass[j] - prefix_mass[i]))

    cyclic_spectrum.sort()

    return cyclic_spectrum
       

def cyclopeptide_scoring(peptide, spectrum):
    theory_spectrum = cyclic_spectrum(peptide, amino_acid_mass)
    score = 0
    for i in theory_spectrum:
        if i in spectrum:
            score += 1
            spectrum.remove(i)

    return score

print(cyclopeptide_scoring(peptide, spectrum))

