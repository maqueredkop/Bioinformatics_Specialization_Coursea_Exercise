
'''
DeBruijn Graph from k-mers Problem: Construct the de Bruijn graph from a set of k-mers.
     Input: A collection of k-mers Patterns.
     Output: The adjacency list of the de Bruijn graph DeBruijn(Patterns).

'''

#with open('test3.txt','r') as f:
with open('dataset_200_8.txt','r') as f:
    kmer_list = []
    for  i in f:
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
for i in sorted(node_connect):
    print(i + ' -> ' + node_connect[i])


