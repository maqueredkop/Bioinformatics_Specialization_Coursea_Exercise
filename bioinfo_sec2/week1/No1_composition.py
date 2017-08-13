

######################################################################
'''

Code Challenge: Solve the String Composition Problem.
     Input: An integer k and a string Text.
     Output: Compositionk(Text) (the k-mers can be provided in any order).

'''
#######################################################################

#text = 'CAATCCAAC'
text = open('dataset_197_3.txt', 'r').read().strip()

def composition(text, k):
    kmer_list = []
    
    for i in range(len(text)-k+1):
        kmer = text[i:i+k]
        kmer_list.append(kmer)

    kmer_list.sort()

    return kmer_list


kmer_list = composition(text, k=100)
for i in kmer_list:
    print(i)
