
import copy

start_node = 0
end_node = 44

path_connect = []
with open('longest_path_in_DAG.txt','r') as f:
    for line in f:
        line = line.strip()
        line = line.split('->')
        node_start = line[0]
        node_end = line[1].split(':')[0]
        edge_weight = line[1].split(':')[1]
        path_connect.append([int(node_start),int(node_end),int(edge_weight)])

path_connect.sort()
print(path_connect)
print('-----------------------------------------------')

path_connect_copy = copy.deepcopy(path_connect)
for i in path_connect_copy:
    if 0 < i[0] < path_connect_copy[0][1]:
        path_connect.remove(i)

print(path_connect)
print('------------------------------------------------')

path_connect_copy2 = copy.deepcopy(path_connect)
node_start_list = []
node_end_list = []
for i in path_connect:
    node_start_list.append(i[0])
    node_end_list.append(i[1])

for i in path_connect_copy2:
    if i[0] > 0 and (i[0] not in node_end_list):
        path_connect.remove(i)

print(path_connect)


def longest_path(start_node,end_node,path_connect):
    path_length = []
    for i in range(end_node):
        path_length.append(0)
    
    node_end_list = []
    for i in path_connect:
        node_end_list.append(i[1])
    
    node_input_number = []
    for i in range(1,end_node+1):
        node_count = node_end_list.count(i)
        node_input_number.append(node_count)
  
    print(node_input_number)      
    print(len(node_input_number))
        #for j in range(len(path_connect)):
        #    if i == path_connect[j][1]:
        


longest_path(start_node,end_node,path_connect)
