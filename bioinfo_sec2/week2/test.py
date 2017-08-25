
import random


###########################################################################

with open('GappedGenomePathString.txt','r') as f:
#with open('StringReconstructionProblem.txt','r') as f:
#with open('dataset_203_7.txt','r') as f:
    kmer_list = []
    for  i in f:
        i = i.split('|')
        kmer_list.append(i[1].strip())

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

'''
with open('debruijn_graph.txt','a') as f:
    for i in node_connect:
        line = i + '->' + node_connect[i]
        f.write(line)
        f.write('\n')
'''

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

#### search the right node
right_list = []
for i in adjacency_list.values():
    right_list.extend(i)

for i in adjacency_list:
    if len(adjacency_list[i]) - right_list.count(i) == 1:
        right_node = i
        break

#print(right_node)

##### search the left node
left_set = set(adjacency_list.keys())
right_set = set(right_list)

#print(left_set)
#print(right_set)

for i in right_set:
    if right_list.count(i) - len(adjacency_list.get(i, [])) == 1:
        left_node = i
        break

'''
if len(right_set) > len(left_set):
    left_node = list(right_set - left_set)[0]
else:
    for i in adjacency_list:
        if len(adjacency_list[i]) - right_list.count(i) == -1:
            left_node = i
            break
'''
#print(left_node)

##################################################

if left_node in adjacency_list.keys():
    adjacency_list[left_node].append(right_node)
else:
    adjacency_list[left_node] = [right_node]
    

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

for i in range(len(eulerian_cycle)):
    if eulerian_cycle[i] == left_node:
        if eulerian_cycle[i+1] == right_node:
            index = i + 1

eulerian_path = eulerian_cycle[index:-1]
eulerian_path.extend(eulerian_cycle[:index])


text = eulerian_path[0]
for i in eulerian_path[1:]:
    text = text + i[-1]

print(text)


'''
result = ''
for i in eulerian_path:
    if len(result) == 0:
        result = i
    else:
        result = result + '->' + i

print(result)
'''

