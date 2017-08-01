

#text = 'TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT'
text = open('E_coli.txt', 'r').read().strip()

def mininum_skew(text):

    base_value = {'A':0, 'C':-1, 'G':1, 'T':0}

    count_list = [0]

    count = 0
    for i in text:
        count = count + base_value[i]
        count_list.append(count)

    #return count_list
    minimum_index = []
    minimum_count = min(count_list)
    for i in range(1,len(count_list)-1):
        if count_list[i] == minimum_count:
            minimum_index.append(i)

            print(text[i-1] + ':' + text[i] + ':' + text[i])
    return minimum_index

        #if count_list[i] < count_list[i-1] and count_list[i] < count_list[i+1]:
        #    print(i)
        


print(mininum_skew(text))


 

