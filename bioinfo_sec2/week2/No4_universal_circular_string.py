
'''
Code Challenge: Solve the k-Universal Circular String Problem.
     Input: An integer k.
     Output: A k-universal circular string.
'''

import random
import itertools

k = 9

string_list = []
for i in itertools.product('01', repeat=k):
    string_list.append(''.join(i))

###########################################################################

kmer_list = string_list.copy()

def debruijn_graph(kmer_list):

    node_connect = dict()

    for i in kmer_list:
        former_node = i[:-1]
        latter_node = i[1:]
        if former_node not in node_connect.keys():
            node_connect[former_node] = latter_node
        else:
            node_connect[former_node] = node_connect[former_node] + ',' + latter_node

    return node_connect


node_connect = debruijn_graph(kmer_list)

#print(node_connect)
###########################################################################

#with open('debruijn_graph.txt', 'r') as f:
adjacency_list = dict()
for i in node_connect:
    left = i
    right = node_connect[i]
    if ',' in right:
        right = right.split(',')
    else:
        right = [right].copy()
    adjacency_list[left] = right

#print(adjacency_list)


edge_len = 0
for i in adjacency_list.values():
    edge_len = edge_len + len(i)
edge_len = edge_len + 1
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

def eulerian_cycle(adjacency_list):
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

    return cycle
            

eulerian_cycle = eulerian_cycle(adjacency_list)

print(eulerian_cycle)


result = eulerian_cycle[0]
for i in range(1,2**k):
    result = result + eulerian_cycle[i][-1]


result = result[0:2**k]
print(result)
print(len(result))

