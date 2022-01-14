import numpy as np
filename = 'input_day15.txt'

with open('Day15/' + filename, 'r') as file:
    data = file.read().split('\n')

cave = data[:-1]
depth = len(cave)
width = len(data[0])
cave_ar = np.zeros(shape = (width,depth))
for row in range(width):
    cave_ar[row] = list(cave[row])

risks = 0


import heapq
from collections import defaultdict

with open('Day15/' + filename) as f: 
    inp = f.read() 

x_len = len(inp.split('\n')[0]) 
y_len = len(inp.split('\n'))

inp = [[int(x) for x in y]*5 for y in inp.split('\n')]*5
chiton = {}
for y in range(len(inp)): 
    for x in range(len(inp[0])): 
        chiton[(x,y)] = ( (x//x_len) + (y//y_len) + inp[y][x] ) if ( (x//x_len) + (y//y_len) + inp[y][x] ) <= 9 else ( (x//x_len) + (y//y_len) + inp[y][x] )%10 + 1

start = (0,0) 
end = (max(chiton, key = lambda x: x[0])[0], max(chiton, key = lambda x: x[1])[1])

distances = {} 
for k,v in chiton.items(): 
    distances[k] = float('inf') 
distances[start] = 0 
pq = [(0,start)]

d = [(0,1), (1,0), (-1,0), (0,-1)] 
while len(pq)>0: 
    current_distance, current_node = heapq.heappop(pq) 
    if current_distance>distances[current_node]: 
        continue
    x,y = current_node 
    for dx,dy in d: 
        x1,y1 = x+dx, y+dy 
        if 0<=x1<=end[0] and 0<=y1<=end[1]: 
            cost = current_distance + chiton[(x1,y1)] 
            if cost < distances[(x1,y1)]: 
                distances[(x1,y1)] = cost 
                heapq.heappush(pq, (cost, (x1,y1)))

print(distances[end])