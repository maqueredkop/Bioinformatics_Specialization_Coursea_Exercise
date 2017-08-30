

graph = dict()
#with open('test6.txt','r') as f:
#with open('MaximalNonBranchingPaths.txt','r') as f:
with open('dataset_6207_2.txt','r') as f:
    for line in f:
        line = line.split('->')
        former_node = line[0].strip()
        latter_node = line[1].strip()
        if ',' in latter_node:
            latter_node = latter_node.split(',')
        else:
            latter_node = [latter_node]
        graph[former_node] = latter_node

#print(graph)

node_list = list(graph.keys())
latter_node_list = []
for i in graph.values():
    latter_node_list.extend(i)

#print(node_list)
#print(latter_node_list)

def indegree(node):
    node_nu = latter_node_list.count(node)
    return node_nu

def outdegree(node):
    node_nu = len(graph.get(node, ''))
    return node_nu

def maximal_nonbranching_paths(graph):
    paths = []
    for v in node_list:
        indeg = indegree(v)
        outdeg = outdegree(v)

        if not (indeg == outdeg == 1):
            if len(graph[v]) > 0:
                for w in graph[v]:
                    nonbranching_path = [v, w]
                    while indegree(w) == outdegree(w) == 1:
                        u = graph[w][0]
                        nonbranching_path.append(u)
                        w = u
                    paths.append(nonbranching_path)
    
    reached_node = []
    for i in paths:
        reached_node.extend(i)
    reached_node_set = set(reached_node)
    remain_node = list(set(node_list) - reached_node_set)
    for v in remain_node:
        if v in reached_node:
            pass
        else:
            indeg = indegree(v)
            outdeg = outdegree(v)
            if indeg == outdeg == 1:
                w = graph[v][0]
                path = [v, w]
        
                while indegree(w) == outdegree(w) == 1:
                    u = graph[w][0]
                    if u != v:
                        path.append(u)
                        w = u
                    else:
                        path.append(u) 
                        break

            paths.append(path)        
            reached_node.extend(path)
    return paths


paths = maximal_nonbranching_paths(graph)
for i in paths:
    print(' -> '.join(i))

