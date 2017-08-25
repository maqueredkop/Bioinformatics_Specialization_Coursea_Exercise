
import random

k = 50
d = 200


###########################################################################


def debruijn_graph(kmer_list):

    node_connect = dict()

    for i in kmer_list:
        former_node = i[:-1]
        latter_node = i[1:]
        if former_node not in node_connect.keys():
            node_connect[former_node] = latter_node
        else:
            node_connect[former_node] = node_connect[former_node] + ',' + latter_node

    #node_connect = debruijn_graph(kmer_list)

    adjacency_list = dict()
    for i in node_connect:
        left = i
        right = node_connect[i]
        if ',' in right:
            right = right.split(',')
        else:
            right = [right].copy()
        adjacency_list[left] = right


    right_list = []
    for i in adjacency_list.values():
        right_list.extend(i)

    for i in adjacency_list:
        if len(adjacency_list[i]) - right_list.count(i) == 1:
            right_node = i
            break

    left_set = set(adjacency_list.keys())
    right_set = set(right_list)

    for i in right_set:
        if right_list.count(i) - len(adjacency_list.get(i, [])) == 1:
            left_node = i
            break

    if left_node in adjacency_list.keys():
        adjacency_list[left_node].append(right_node)
    else:
        adjacency_list[left_node] = [right_node]
    
    edge_len = 0
    for i in adjacency_list.values():
        edge_len = edge_len + len(i)
    edge_len = edge_len + 1

    return [adjacency_list, edge_len, left_node, right_node]


#print(debruijn_graph(kmer_list))

##################################################################

def graph_form(adjacency_list, start_point,graph_path):
    while adjacency_list[start_point] is not None:
        next_point = adjacency_list[start_point]
        if len(next_point) == 1:
            graph_path.append(next_point[0])
            adjacency_list[start_point] = None
            start_point = next_point[0]
        else:
            next_point = random.choice(next_point)
            graph_path.append(next_point)
            adjacency_list[start_point].remove(next_point)
            start_point = next_point

    return [graph_path, adjacency_list]

######################################################################

def eulerian_cycle(adjacency_list, edge_len, left_node, right_node):
    start_point = random.choice(list(adjacency_list.keys()))
    graph_path = [start_point]
    graph = graph_form(adjacency_list, start_point, graph_path)
    cycle = graph[0]
    adjacency_list = graph[1]
    avaiable_start = []
    while len(cycle) < edge_len:
        for i in cycle:
            if adjacency_list[i] is not None:
                avaiable_start.append(i)
        start_point = random.choice(avaiable_start)
        index = cycle.index(start_point)
        cycle_new = cycle[index:-1]
        cycle_new.extend(cycle[:index])
        cycle_new.append(start_point)
        
        
        cycle_new = graph_form(adjacency_list, start_point, cycle_new)[0]
        
        cycle = cycle_new.copy()

    eulerian_cycle = cycle

    for i in range(len(eulerian_cycle)):
        if eulerian_cycle[i] == left_node:
            if eulerian_cycle[i+1] == right_node:
                index = i + 1

    eulerian_path = eulerian_cycle[index:-1]
    eulerian_path.extend(eulerian_cycle[:index])

    text = eulerian_path[0]
    for i in eulerian_path[1:]:
        text = text + i[-1]

    return text

##################################################################################

s = 'CCAATTGTTGGCAACAAAGAATCGCTTATGCTAGGGTGACGTGCCAATCGACTGATTTGACTGGCCGGGGGATCGGCTGCGTAAAACCGGTGTCAGAATAAATAGTCATGGCCGGCGTCGACAGGCGCCCCGAGGGATAGGTAACGGGCGTGAAGAAGCGGTTCTGGGTGCATAGCCGGACGCCACGAAGTCGTGAAGAAGCGGTTCTGGGTGCATAGCCGGACGCCACGAAGTGTCAACTGTCAACTACGTGAAGAAGCGGTTCTGGGTGCATAGCCGGACGCCACGAAGTGTCAACTGAGCCTGAGGCCCGTGAAGAAGCCGTGAAGAAGCGGTTCTGGGTGCATAGCCGGACGCCACGAAGTGTCAACTGGTTCTGGGTGCATAGCCGCGTGAAGAAGCGGTTCTGGGTGCATAGCCGGACGCCACGAAGTGTCAACTGACGCCACGAAGTGTCAACTAGTGTTGTCATGAGAGAGTTATTATAGCAGGCCTACTTGTAGGTAAATACACTCTAGGTTATTCGCTCTGCTCCCCTCCTGCGTAACCCCTACCGTGAAGAAGCGGTCGTGAAGAAGCGGTTCTGGGTGCATAGCCGGACGCCACGAAGTGTCAACTTCTGGGTGCATAGCCGGACGCCACGAAGTGTCAACTGTGTTACTACCCATAGCGTCGGCCTCGTGAAGAAGCGGTTCTGGGCGTGAAGAAGCGGTTCTGGGTGCATAGCCGGACGCCACGAAGTGTCAACTTGCATAGCCGTGAAGAAGCGGTTCTGGGTGCATAGCCGGACGCCACGACGTGAAGAAGCGGTTCTGGGTGCATAGCCGGACGCCACGAAGTGTCAACTAGTGTCAACTCGGACGTGAAGAAGCGGTTCTGGGTGCATAGCCGGACGCCACGAAGTGTCAACTCGCCACGAAGTGTCAACTACGTGGCAATCATCGTGAAGAAGCGGTTCTGGGTGCATAGCCGGACGCCACGAAGTGTCAACTGTACTAGTTTAGCTGTAGGGCTTGAGGCAATTCCACGATCAGCGGGAACAGCGATATAACCCTTACATATCTAAACGCTGGACTGCATAAAGTAAGCAAGGAAATTGACTGAGGCGCTTACCCCGTGAAGAAGCGGTTCTGGGTGCATAGCCGGACGCCACGAAGTGTCAACTCCAGTATCAAGCCGCAACCGGGCCCGTGACTCATCCTCCTGCATACCCGTGAAGAAGCGGTTCTGGGTGCATAGCCGGACGCCACGAAGTGTCAACTGAACGGGGCCTGGTCCCGTTTTCGAAGGGTGAGTTCTGCTTAGCGTTGTCTTTCATTCGCTCAAAAGTCCCGCGTAAGAGCATCCTGGATTGTTCGCCCTGTAAGCGGGACTACGCGTGCCGATGGTGGGCTTGCAATTATCATAGCGTGAAGAAGCGGTTCTGGGTGCATAGCCGGACGCCACGAAGTGTCAACTTCCTGTTCCGTCAATTCCTCTCTAAATACTATCTAACCTGGTCGCAGAACTCGAAGAACTACCGGCCGTCAGCAATTCTAGCTTAATACCTCGTCGTGAAGAAGCGGTTCTGGGTGCATAGCCGGACGCCACGAAGTGTCAACTTGAATAGTGCGTGAAGAAGCGGTTCTGGGTGCATAGCCGGACGCCACGAAGTGTCAACTGCCCCTCGGAACGGTATGTACTGCAAGCGTAGAAACCCTGATAGCTTGGATGACGAAACTGTTAGATGTACTGCCAACGGTTAGTCGCGCTGTCGGTTTCGTTAACGATGCATTAAGTCGAACTCGTACCTAGAAACGTGAAGAAGCGGTTCTGGGTGCATAGCCGGACGCCACGAAGTGTCAACTAGTGGGATATTGGTGAAGCAGAGGACGAATTGCGATATCCAAGATGAGAACTGTTTGTCAGTCGGGGAAGACCCAGCTGACTACGCTCAGAGCCCGGTCATGTGTCTGAATCAATCTAAAAACGTATAGTTTGGCTACTGGGGCGCTAGGTGC'


##################################################################################



def call(kmer_list):
    result = debruijn_graph(kmer_list)
    adjacency_list = result[0]
    edge_len = result[1]
    left_node = result[2]
    right_node = result[3]
    
    text = eulerian_cycle(adjacency_list, edge_len, left_node, right_node)

    return text


#kmer_list = ['AG','GC','CA','AG','GC','CT','TG','GC','CT']
#print(call(kmer_list))

 
gapped_patterns = []
#with open('test4.txt','r') as f:
#with open('GappedGenomePathString1000.txt','r') as f:
with open('StringReconstructionFromReadPairs.txt','r') as f:
#with open('GappedGenomePathString.txt','r') as f:
#with open('dataset_6206_7.txt','r') as f:
    for i in f:
        gapped_patterns.append(i.strip())

#print(len(gapped_patterns))
#print(gapped_patterns[0])
#print(gapped_patterns[-1])

def string_spelled_by_gapped_patterns(gapped_patterns, k, d):
    first_patterns = []
    second_patterns = []
    for pattern in gapped_patterns:
        pattern = pattern.split('|')
        first_patterns.append(pattern[0].strip())
        second_patterns.append(pattern[1].strip())
    
    #print(len(first_patterns))    
    prefix_string = call(first_patterns)
    suffix_string = call(second_patterns)

    print(prefix_string)
    print(suffix_string)
    
    result = True
    while result:
        for i in range(k+d, len(prefix_string)):
            #text = prefix_string + suffix_string[-(k+d):]
            #if text in s:
            if prefix_string[i] == suffix_string[i-k-d]:
                #print('try again')
                return prefix_string + suffix_string[-(k+d):]
                #return text
                result = False
            else:
                print('try again')
                
                #return "there is no string spelled by the gapped patterns"
        #return prefix_string + suffix_string[-(k+d):]


print(string_spelled_by_gapped_patterns(gapped_patterns, k, d))



