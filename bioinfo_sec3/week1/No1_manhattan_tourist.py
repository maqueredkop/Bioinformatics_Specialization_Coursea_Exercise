
'''
import copy
import itertools               
location_list = []
for i in range(17):
    for j in range(13):
       location_list.append([i,j])
possible_combinations = list(itertools.combinations(location_list[1:-1], 27))

print(type(possible_combinations))
print(len(possible_combinations))

#possible_collections = possible_combinations.deepcopy()

#for tour in possible_combinations:
    
'''

import random

start_point = [0,0]
end_point = [4,4]

possible_tour = [start_point]

for i in range(8):
    start_point = possible_tour[-1]
    next_points = []
    if start_point[0] + 1 <= 4:
        next_point_down = [start_point[0] + 1, start_point[1]]
        next_points.append(next_point_down)
    if start_point[1] + 1 <= 4:
        next_point_right = [start_point[0], start_point[1] + 1]
        next_points.append(next_point_right)

    choose_point = random.choice(next_points)
    possible_tour.append(choose_point)


print(possible_tour)    
    
       
