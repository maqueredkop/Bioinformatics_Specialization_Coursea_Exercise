
import random

#with open('test1.txt', 'r') as f:
with open('dataset_203_2.txt', 'r') as f:
#with open('eulerian_cycle.txt', 'r') as f:
    adjacency_list = dict()
    for line in f:
        line_list = line.split('->')
        left = line_list[0].strip()
        right = line_list[1].strip()
        if ',' in right:
            right = right.split(',')
        else:
            right = [right].copy()
        adjacency_list[left] = right

    edge_len = 0
    for i in adjacency_list.values():
        edge_len = edge_len + len(i)
    edge_len = edge_len + 1

def graph_form(adjacency_list):
    start_point = random.choice(list(adjacency_list.keys()))
    graph_path = [start_point]
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


def eulerian_cycle(adjacency_list):
    graph = graph_form(adjacency_list)
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
        
        while adjacency_list[start_point] is not None:
            next_point = adjacency_list[start_point]
            if len(next_point) == 1:
                cycle_new.append(next_point[0])
                adjacency_list[start_point] = None
                start_point = next_point[0]
            else:
                next_point = random.choice(next_point)
                cycle_new.append(next_point)
                adjacency_list[start_point].remove(next_point)
                start_point = next_point

        cycle = cycle_new.copy()

    return cycle
            

eulerian_cycle = eulerian_cycle(adjacency_list)
result = ''
for i in eulerian_cycle:
    if len(result) == 0:
        result = i
    else:
        result = result + '->' + i

print(result)
