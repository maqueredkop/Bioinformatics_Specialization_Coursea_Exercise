'''
Code Challenge: Implement LeaderboardCyclopeptideSequencing.
     Input: An integer N and a collection of integers Spectrum.
     Output: LeaderPeptide after running LeaderboardCyclopeptideSequencing(Spectrum, N).
'''

#with open('dataset_102_8.txt','r') as f:
#with open('Tyrocidine_B1_Spectrum_10.txt','r') as f:
with open('Tyrocidine_B1_Spectrum_25.txt','r') as f:
    #leaderboard = next(f).strip().split()
    spectrum = next(f).strip().split()
    spectrum = [int(x) for x in spectrum]
#spectrum = [0,71,113,129,147,200,218,260,313,331,347,389,460]
N = 1000

amino_acid_mass = {'G':57,'A':71,'S':87,'P':97,'V':99,'T':101,'C':103,'I':113,'L':113,
                   'N':114,'D':115,'K':128,'Q':128,'E':129,'M':131,'H':137,'F':147,
                   'R':156,'Y':163,'W':186}

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
        for j in 'GASPVTCILNDKQEMHFRYW':
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
    
    while len(leaderboard) > 0:
        leaderboard = expand(leaderboard)
        leaderboard2 = leaderboard.copy()
        for peptide in leaderboard2:
            if mass(peptide) == spectrum[-1]:
                #if linear_scoring(peptide,spectrum) > linear_scoring(leader_peptide,spectrum):
                if cyclopeptide_scoring(peptide, spectrum) > cyclopeptide_scoring(leader_peptide,spectrum):
                    leader_peptide = peptide
                    leaderboard.remove(peptide)
            elif mass(peptide) > spectrum[-1]:
                leaderboard.remove(peptide)
        leaderboard = leaderboard_trim(leaderboard, spectrum, N)
    
    return leader_peptide
 
peptide = leaderboard_cyclopeptide_sequencing(spectrum, N)
print(peptide)
print(cyclopeptide_scoring(peptide, spectrum))
peptide_mass = []
for amino in peptide:
    peptide_mass.append(str(amino_acid_mass[amino]))
        
peptide_mass = '-'.join(peptide_mass)
print(peptide_mass)
