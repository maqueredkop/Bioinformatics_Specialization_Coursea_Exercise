###### this agorithim is very slow compared to No4_cyclic_spectrum.py


#peptide = 'NQEL'
peptide = 'MPYENCCCWMFNIRKGQPDFFRKGAVPYVVPMNCIRWS'
peptide = 100 * peptide
amino_acid_mass = {'G':57,'A':71,'S':87,'P':97,'V':99,'T':101,'C':103,'I':113,'L':113,
                   'N':114,'D':115,'K':128,'Q':128,'E':129,'M':131,'H':137,'F':147,
                   'R':156,'Y':163,'W':186}

def get_peptide_mass(peptide):
    mass = 0
    for i in peptide:
        mass = mass + amino_acid_mass[i]
    return mass

def cyclic_spectrum(peptide, amino_acid_mass):
    peptide2 = peptide + peptide
    peptide_mass = [0]
    for i in range(len(peptide)-1):
        for j in range(len(peptide)):
            sub_peptide = peptide2[j:j+i+1]
            peptide_mass.append(get_peptide_mass(sub_peptide))
    peptide_mass.append(get_peptide_mass(peptide))
    peptide_mass.sort()

    return peptide_mass
           
result = cyclic_spectrum(peptide, amino_acid_mass)
result = str(result)
result = result.replace(',','')
#print(result)

