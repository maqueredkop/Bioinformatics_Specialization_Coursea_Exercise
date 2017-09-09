#leaderboard = ['LAST','ALST','TLLT','TQAS']
#with open('trim.txt','r') as f:
with open('dataset_4913_3.txt','r') as f:
    leaderboard = next(f).strip().split()
    spectrum = next(f).strip().split()
    spectrum = [int(x) for x in spectrum]

N = 6
#spectrum = [0,71,87,101,113,158,184,188,259,271,372]
#spectrum = open('dataset_4913_1.txt','r').read().strip().split()
#spectrum = [int(x) for x in spectrum]
#spectrum.sort()

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
    spectrum2 = spectrum.copy()
    theory_spectrum = linear_spectrum(peptide, amino_acid_mass)
    score = 0
    for i in theory_spectrum:
        if i in spectrum2:
            score += 1
            spectrum2.remove(i)

    return score

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

leaderboard = leaderboard_trim(leaderboard, spectrum, N)
for i in leaderboard:
    print(i)
   
