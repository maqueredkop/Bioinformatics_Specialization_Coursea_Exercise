#peptide = 'NQEL'
peptide = 'FNSQGKPRALMGIYGCNMPLDLGKATRQQFLEPDRLCHFSMKQKC'
#spectrum = [0,99,113,114,128,227,257,299,355,356,370,371,484]
spectrum = open('dataset_4913_1.txt','r').read().strip().split()
spectrum = [int(x) for x in spectrum]
spectrum.sort()

amino_acid_mass = {'G':57,'A':71,'S':87,'P':97,'V':99,'T':101,'C':103,'I':113,'L':113,
                   'N':114,'D':115,'K':128,'Q':128,'E':129,'M':131,'H':137,'F':147,
                   'R':156,'Y':163,'W':186}

def linear_spectrum(peptide, amino_acid_mass):
    prefix_mass = [0]
    for i in range(len(peptide)):
        amino = peptide[i]
        amino_mass = amino_acid_mass[amino]
        prefix_mass.append(prefix_mass[i] + amino_mass)

    linear_spectrum = [0]
    for i in range(len(peptide)):
        for j in range(i+1, len(peptide)+1):
            linear_spectrum.append(prefix_mass[j] - prefix_mass[i])

    linear_spectrum.sort()
    return linear_spectrum

def linear_scoring(peptide, spectrum):
    theory_spectrum = linear_spectrum(peptide, amino_acid_mass)
    score = 0
    for i in theory_spectrum:
        if i in spectrum:
            score += 1
            spectrum.remove(i)

    return score

print(linear_scoring(peptide, spectrum))

