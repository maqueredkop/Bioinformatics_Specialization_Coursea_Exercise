'''
Code Challenge: Implement ConvolutionCyclopeptideSequencing.
     Input: An integer M, an integer N, and a collection of (possibly repeated) integers Spectrum.
     Output: A cyclic peptide LeaderPeptide with amino acids taken only from the top M elements (and ties) of the convolution of
     Spectrum that fall between 57 and 200, and where the size of Leaderboard is restricted to the top N (and ties).
'''

############################################################################################

#M = 20
#N = 60
#M = 17
#N = 341
M = 20
N = 1000

import collections

#spectrum = [0,57,57,71,99,129,137,170,186,194,208,228,265,285,299,307,323,356,364,394,422,493]
#spectrum = open('convolution_cyclopeptide_sequencing.txt','r').read().strip().split()
#spectrum = open('dataset_104_7.txt','r').read().strip().split()
spectrum = open('Tyrocidine_B1_Spectrum_25.txt','r').read().strip().split()
#spectrum = open('dataset_104_4.txt','r').read().strip().split()
spectrum = [int(x) for x in spectrum]
if min(spectrum) > 0:
    spectrum.append(0)
spectrum.sort()
#print(spectrum)

def spectrum_convolution(spectrum):
    spectrum2 = spectrum.copy()
    element_list = []
    for i in range(1,len(spectrum2)):
        for j in range(i):
            element_list.append(spectrum2[i] - spectrum[j])
    
    element_list = [x for x in element_list if x >= 57 and x <= 200]
    
    return element_list 
        
def frequent_elements(spectrum, M):
    element_list = spectrum_convolution(spectrum)
    element_list.sort()
    element_list = [x for x in element_list if x > 0]
    element_count = collections.Counter()
    for i in element_list:
        element_count[i] += 1

    element_sort = element_count.most_common()
    for i in range(M,len(element_count)):
        if not element_sort[i][1] < element_sort[M-1][1]:
            M = M + 1

    frequent_list = element_count.most_common(M)
    #frequent_elements = []
    #for i in range(len(frequent_list)):
    #    frequent_elements.append(frequent_list[i][0])

    #return frequent_elements
    return frequent_list

##############################################################################################3

amino_acid_mass = dict()
frequent_list = frequent_elements(spectrum, M)
frequent_amino = []
for i in frequent_list:
    frequent_amino.append(i[0])

for i in frequent_amino:
    amino_acid_mass[chr(i)] = i

##############################################################################################

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
    spectrum2 = spectrum.copy()
    theory_spectrum = linear_spectrum(peptide, amino_acid_mass)
    score = 0
    for i in theory_spectrum:
        if i in spectrum2:
            score += 1
            spectrum2.remove(i)

    return score

#################################################################################################

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
    spectrum2 = spectrum.copy()
    theory_spectrum = cyclic_spectrum(peptide, amino_acid_mass)
    score = 0
    for i in theory_spectrum:
        if i in spectrum2:
            score += 1
            spectrum2.remove(i)

    return score

#################################################################################################

def leaderboard_trim(leaderboard, spectrum, N):
    linear_scores = []
    for peptide in leaderboard:
        linear_scores.append(linear_scoring(peptide, spectrum))

    leaderboard = [x for _,x in reversed(sorted(zip(linear_scores,leaderboard)))]
    linear_scores = sorted(linear_scores)[::-1]
    for i in range(N, len(leaderboard)):
        if linear_scores[i] < linear_scores[N-1]:
            leaderboard = leaderboard[0:i]
            return leaderboard
    return leaderboard

#######################################################################################

def expand(peptides):
    expanded_peptides = []
    for i in peptides:
        for j in list(amino_acid_mass.keys()):
            expanded_peptide = i + j
            expanded_peptides.append(expanded_peptide)
   
    return expanded_peptides
         
def mass(peptide):
    mass = 0
    for i in peptide:
        mass = mass + amino_acid_mass[i]

    return mass

######################################################################################
def leaderboard_cyclopeptide_sequencing(spectrum, N):
    leaderboard = ['']
    leader_peptide = ''
    leader_peptide_list = []    
    
    while len(leaderboard) > 0:
        leaderboard = expand(leaderboard)
        leaderboard2 = leaderboard.copy()
        for peptide in leaderboard2:
            if mass(peptide) == spectrum[-1]:
                leader_peptide_list.append(peptide)
                if cyclopeptide_scoring(peptide, spectrum) > cyclopeptide_scoring(leader_peptide,spectrum):
                    leader_peptide = peptide
                    leaderboard.remove(peptide)
            elif mass(peptide) > spectrum[-1]:
                leaderboard.remove(peptide)
        leaderboard = leaderboard_trim(leaderboard, spectrum, N)
    
    return [leader_peptide,leader_peptide_list]
 
result = leaderboard_cyclopeptide_sequencing(spectrum, N)
peptide = result[0]
#print(peptide)
peptide_mass = []
for amino in peptide:
    peptide_mass.append(str(amino_acid_mass[amino]))
        
peptide_mass = '-'.join(peptide_mass)
#print(peptide_mass)



leader_peptide_list = result[1]
peptide_list = []
highest_score = cyclopeptide_scoring(peptide, spectrum)
print(highest_score)

for i in leader_peptide_list:
    if cyclopeptide_scoring(i, spectrum) == highest_score:
        peptide_list.append(i)

print(len(peptide_list))
print(peptide_list)
peptide_set = set(peptide_list)
print(len(peptide_set))

peptides_mass = []
for peptide in peptide_list:
    peptide_mass = []
    for amino in peptide:
        peptide_mass.append(str(amino_acid_mass[amino]))
        
    peptide_mass = '-'.join(peptide_mass)
    peptides_mass.append(peptide_mass)

peptides_mass = set(peptides_mass)
print(len(peptides_mass))
print(' '.join(peptides_mass))
