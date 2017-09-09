
import collections

#spectrum = [0,137,186,323]
#spectrum = open('spectral_convolution.txt','r').read().strip().split()
spectrum = open('dataset_104_4.txt','r').read().strip().split()
spectrum = [int(x) for x in spectrum]
spectrum.sort()
#print(spectrum)

def spectrum_convolution(spectrum):
    spectrum2 = spectrum.copy()
    element_list = []
    for i in range(1,len(spectrum2)):
        for j in range(i):
            element_list.append(spectrum2[i] - spectrum[j])

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
    frequent_elements = []
    for i in range(len(frequent_list)):
        frequent_elements.append(frequent_list[i][0])

    return frequent_elements

print(frequent_elements(spectrum, M=4))

###############################################################################

