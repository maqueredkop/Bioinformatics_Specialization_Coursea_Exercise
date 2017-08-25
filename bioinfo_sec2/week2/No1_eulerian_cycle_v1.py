
'''
Code Challenge: Solve the Eulerian Cycle Problem.
     Input: The adjacency list of an Eulerian directed graph.
     Output: An Eulerian cycle in this graph.

'''
import random
import copy

with open('test1.txt','r') as f:
#with open('dataset_203_2.txt','r') as f:
    adjacency_list = dict()
    eulerian_edge_len = 0
    muti_node = []
    for i in f:
        i = i.split('->')
        left = int(i[0].strip())
        right = i[1].strip()
        if ',' in right:
            muti_node.append(left)
            right = right.split(',')
            right = [int(x) for x in right]
            eulerian_edge_len = eulerian_edge_len + len(right)
        else:
            eulerian_edge_len = eulerian_edge_len + len(right)
            right = int(right)
        adjacency_list[left] = right

def cycle_form(adjacency_list, start_point):
    adjacency_list_temp = copy.deepcopy(adjacency_list)
    cycle_nodes = [start_point]
    start_node = start_point
    for i in range(eulerian_edge_len):
        next_node = adjacency_list_temp[start_point]
        if type(next_node) == int:
            cycle_nodes.append(next_node)
            start_point = next_node
        else:
            next_node = random.choice(next_node)            
            adjacency_list_temp[start_point].remove(next_node)
            cycle_nodes.append(next_node)
            start_point = next_node
       
        if  start_point in muti_node:
            if len(adjacency_list_temp[start_point]) == 0:
                break
        if cycle_nodes[-1] == cycle_nodes[0]:
            if type(adjacency_list_temp[cycle_nodes[0]]) == int:
                break
    if len(cycle_nodes) < (eulerian_edge_len + 1):
        remain_muti_node = []
        for i in muti_node:
            if i in cycle_nodes:
                if len(adjacency_list_temp[i]) > 0:
                    remain_muti_node.append(i)
        new_start = random.choice(remain_muti_node)

    else:
        new_start = None

    return [cycle_nodes, new_start]


def eulerian_cycle(adjacency_list):
    start_point = random.choice(list(adjacency_list.keys()))
    cycle_result = cycle_form(adjacency_list, start_point)
    cycle = cycle_result[0]
    
    while len(cycle) < (eulerian_edge_len + 1):
            
        new_start = cycle_result[1]
        cycle_new = cycle_form(adjacency_list, new_start)
        cycle = cycle_new[0]

    return cycle


print(eulerian_cycle(adjacency_list))

