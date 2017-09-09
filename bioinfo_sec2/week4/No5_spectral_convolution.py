'''
Spectral Convolution Problem: Compute the convolution of a spectrum.
     Input: A collection of integers Spectrum.
     Output: The list of elements in the convolution of Spectrum. If an element has multiplicity k, it should appear exactly k times;
'''

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
        

element_list = spectrum_convolution(spectrum)
element_list.sort()
element_list = [x for x in element_list if x > 0]

elements = ' '.join([str(x) for x in element_list])
print(elements)

