peptide = 'CHAMNIIDVP'
#peptide = 'PAKM'
#peptide = 'LEQN'
#peptide = 'MPYENCCCWMFNIRKGQPDFFRKGAVPYVVPMNCIRWS'
#peptide = 'PPDRWDYAVAKMNQ'
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
        
result = cyclic_spectrum(peptide, amino_acid_mass)
result = str(result)
result = result.replace(',','')
print(result)

