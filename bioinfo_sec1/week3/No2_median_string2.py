
k = 6
pattern = 'GCTCCT'

#with open('dataset_5164_1.txt','r') as f:
#    dna = []
#    for line in f.readlines():
#        line = line.strip()
#        dna.append(line)
#print(dna)

seq = open('dataset_5164_1.txt','r').read().strip()

dna = seq.split(' ')

print(dna)

##################################################################################
def hamming_distance(text1, text2):
    distance = 0
    for i in range(len(text1)):
        if text1[i] != text2[i]:
            distance = distance + 1

    return distance

def min_hamming_distance(pattern, text):
    hamming_distance_list = []
    for i in range(len(text)-k + 1):
        distance = hamming_distance(pattern, text[i:i+k])
        hamming_distance_list.append(distance)
    #print(min(hamming_distance_list))
    return min(hamming_distance_list)


def sum_distance(pattern, dna):
    sum_distance = 0
    for string in dna:
        sum_distance = sum_distance + min_hamming_distance(pattern, string)

    return sum_distance


print(sum_distance(pattern, dna))
