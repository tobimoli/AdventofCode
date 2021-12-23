import numpy as np
filename = 'input_day14.txt'

with open('Day14/' + filename, 'r') as file:
    data = file.read().split('\n')

template = data[0]
pairs = data[data.index('')+1:-1]

template = 'NNCB'
pairs = ['CH -> B','HH -> N','CB -> H','NH -> C','HB -> C','HC -> B','HN -> C','NN -> C','BH -> H','NC -> B','NB -> B','BN -> B','BB -> N','BC -> B','CC -> N','CN -> C']
pairs_dict = {}
for pair in pairs:
    a, b = pair.split(' -> ')
    pairs_dict[a] = b

STEPS = 10
steps = [template]
for step in range(STEPS):
    new_template = steps[step][0]
    for index in range(len(steps[step])-1):
        pair = steps[step][index] + steps[step][index+1]
        new_template += pairs_dict[pair] + pair[1]
    steps.append(new_template)
    
sizes = []
for ch in set(steps[-1]):
    print(ch, steps[-1].count(ch))
    sizes.append(steps[-1].count(ch))

print(max(sizes)-min(sizes))