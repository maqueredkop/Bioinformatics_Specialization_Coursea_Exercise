
'''
Code Challenge: Solve the Overlap Graph Problem .
     Input: A collection Patterns of k-mers.
     Output: The overlap graph Overlap(Patterns), in the form of an adjacency list. (You may return the edges in any order.)

'''

with open('dataset_198_10.txt','r') as f:
    pattern_list = []
    for i in f:
        pattern_list.append(i.strip())

def suffix(pattern):
    return pattern[1:]

def prefix(pattern):
    return pattern[:-1]

def overlap_graph(pattern_list):
    adjacency_list = []

    for pattern in pattern_list:
        pattern_connect = [pattern]
        pattern_list_remain = pattern_list.copy()
        pattern_list_remain.remove(pattern)

        for another_pattern in pattern_list_remain:
            if suffix(pattern) == prefix(another_pattern):
                pattern_connect.append(another_pattern)

        if len(pattern_connect) > 1:
            adjacency_list.append(pattern_connect)

    return adjacency_list

print(overlap_graph(pattern_list))
adjacency_list = overlap_graph(pattern_list)
for i in adjacency_list:
    print(i[0] + ' -> ' + i[1])


