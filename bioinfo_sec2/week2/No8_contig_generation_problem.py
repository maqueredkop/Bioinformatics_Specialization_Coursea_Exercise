
################################################################################

#with open('test7.txt','r') as f:
#with open('contig_generation.txt','r') as f:
with open('dataset_205_5.txt','r') as f:
    kmer_list = []
    for i in f:
        kmer_list.append(i.strip())

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

adjacency_list = []
for i in node_connect:
    i = i + '->' + node_connect[i]
    adjacency_list.append(i)

################################################################################

graph = dict()
for line in adjacency_list:
    line = line.split('->')
    former_node = line[0].strip()
    latter_node = line[1].strip()
    if ',' in latter_node:
        latter_node = latter_node.split(',')
    else:
        latter_node = [latter_node]
    graph[former_node] = latter_node

node_list = list(graph.keys())
latter_node_list = []
for i in graph.values():
    latter_node_list.extend(i)

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

contigs = []
for path in paths:
    contig = path[0]
    for node in path[1:]:
        contig = contig + node[-1]
    contigs.append(contig)

contigs.sort()

for contig in contigs:
    print(contig)

