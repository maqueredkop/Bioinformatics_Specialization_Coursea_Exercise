
import random

k = 50
d = 200

###########################################################################

def debruijn_graph(kmer_list):
    node_connect = dict()

    for read in kmer_list:
        read = read.split('|')
        read1 = read[0]
        read2 = read[1]
        prefix_paired = read1[:-1] + '|' + read2[:-1]
        suffix_paired = read1[1:] + '|' + read2[1:]
        former_node = prefix_paired
        latter_node = suffix_paired
        if former_node not in node_connect.keys():
            node_connect[former_node] = latter_node
        else:
            node_connect[former_node] = node_connect[former_node] + ',' + latter_node

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

    return eulerian_path

##################################################################################

def call(kmer_list):
    result = debruijn_graph(kmer_list)
    adjacency_list = result[0]
    edge_len = result[1]
    left_node = result[2]
    right_node = result[3]
    
    paired_eulerian_path = eulerian_cycle(adjacency_list, edge_len, left_node, right_node)

    return paired_eulerian_path

#####################################################################################

def string_from_pattern(patterns):
    string = ''
    for i in patterns[:-1]:
        string = string + i[0]
    string = string + patterns[-1]
    
    return string

def string_spelled_by_gapped_patterns(gapped_patterns, k, d):
    first_patterns = []
    second_patterns = []
    for pattern in gapped_patterns:
        pattern = pattern.split('|')
        first_patterns.append(pattern[0].strip())
        second_patterns.append(pattern[1].strip())

    prefix_string = string_from_pattern(first_patterns)
    suffix_string = string_from_pattern(second_patterns)

    for i in range(k+d, len(prefix_string)):
        if prefix_string[i] != suffix_string[i-k-d]:
            return "there is no string spelled by gapped patterns"
    return prefix_string + suffix_string[len(suffix_string)-k-d : ]

####################################################################################

paired_reads = []
#with open('test5.txt','r') as f:
#with open('StringReconstructionFromReadPairs.txt','r') as f:
with open('dataset_204_15.txt','r') as f:
#with open('reads.txt','r') as f:
    for line in f:
        line = line.strip()
        paired_reads.append(line)

def string_reconstruction_from_read_pairs(paired_reads, k, d):
    paired_eulerian_path = call(paired_reads)
    #print(paired_eulerian_path)
    string = string_spelled_by_gapped_patterns(paired_eulerian_path, k, d)
    
    return string

print(string_reconstruction_from_read_pairs(paired_reads, k, d))
