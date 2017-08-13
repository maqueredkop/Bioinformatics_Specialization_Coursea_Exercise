
'''
Code Challenge: Solve the De Bruijn Graph from a String Problem.
     Input: An integer k and a string Text.
     Output: DeBruijnk(Text), in the form of an adjacency list.

'''

#text  = 'AAGATTCTCTAAGA'
#text  = open('dataset_199_6.txt','r').read().strip()
text = 'TAATGGGATGCCATGTT'
k = 3
#k = 12

def debruijn_graph(text, k):
    node_list = []
    for i in range(len(text)-k+2):
        node_list.append(text[i:i+k-1])

    node_connect = dict()
    for i in range(len(node_list)-1):
        former_node = node_list[i]
        latter_node = node_list[i+1]
        if former_node not in node_connect.keys():
            node_connect[former_node] = latter_node
        else:
            node_connect[former_node] = node_connect[former_node] + ',' + latter_node

    return node_connect


node_connect = debruijn_graph(text, k)
for i in sorted(node_connect):
    print(i + ' -> ' + node_connect[i])


