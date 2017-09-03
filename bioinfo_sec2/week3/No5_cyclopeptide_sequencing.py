
#spectrum = [0,113,128,186,241,299,314,427]

#spectrum_list = open('cyclopeptide_sequencing.txt','r').read().split()
spectrum_list = open('dataset_100_6.txt','r').read().split()
spectrum = [int(x) for x in spectrum_list]

amino_acid_mass = {'G':57,'A':71,'S':87,'P':97,'V':99,'T':101,'C':103,'I':113,'L':113,
                   'N':114,'D':115,'K':128,'Q':128,'E':129,'M':131,'H':137,'F':147,
                   'R':156,'Y':163,'W':186}

######################################################################################
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
 
######################################################################################
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

##########################################################################################  

def expand(peptides):
    expanded_peptides = []
    for i in peptides:
        for j in 'GASPVTCILNDKQEMHFRYW':
            expanded_peptide = i + j
            expanded_peptides.append(expanded_peptide)
   
    return expanded_peptides
         
def mass(peptide):
    mass = 0
    for i in peptide:
        mass = mass + amino_acid_mass[i]

    return mass

#################################################################################
def check_consistent(peptide):
    peptide_spectrum = cyclic_spectrum(peptide, amino_acid_mass)
    for i in peptide_spectrum:
        if i not in spectrum:
            return True
            break
    return False
    
def cyclopeptide_sequencing(spectrum):
    peptides = ['']
    peptide_final = []
    while len(peptides) > 0:
        peptides = expand(peptides)
        peptides2 = peptides.copy()
        for peptide in peptides2:
            if mass(peptide) == spectrum[-1]:
                if cyclic_spectrum(peptide, amino_acid_mass) == spectrum:
                    peptide_final.append(peptide)
                    peptides.remove(peptide)
                else:
                    peptides.remove(peptide)
            ##### the below code  which is commented is a error , which introduce a very hidden bug!!!!
            #elif not set(cyclic_spectrum(peptide, amino_acid_mass)).issubset(set(spectrum)):
            elif not set(linear_spectrum(peptide, amino_acid_mass)).issubset(set(spectrum)):
            #elif not check_consistent(peptide):
                peptides.remove(peptide)
    return peptide_final 

#print(cyclopeptide_sequencing(spectrum))
peptide_final = cyclopeptide_sequencing(spectrum)
peptides_mass = []
for peptide in peptide_final:
    peptide_mass = []
    for amino in peptide:
        peptide_mass.append(str(amino_acid_mass[amino]))
        
    peptides_mass.append('-'.join(peptide_mass))
    
result = set(peptides_mass)
result = ' '.join(result)
print(result)

