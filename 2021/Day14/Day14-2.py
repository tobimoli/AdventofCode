import numpy as np
filename = 'input_day14.txt'

with open('Day14/' + filename, 'r') as file:
    data = file.read().split('\n')

template = data[0]
rules = data[data.index('')+1:-1]

#template = 'NNCB'
#rules = ['CH -> B','HH -> N','CB -> H','NH -> C','HB -> C','HC -> B','HN -> C','NN -> C','BH -> H','NC -> B','NB -> B','BN -> B','BB -> N','BC -> B','CC -> N','CN -> C']
rules_dict = {}

for rule in rules:
    a, b = rule.split(' -> ')
    rules_dict[a] = (a[0]+b, b + a[1])

pairs = rules_dict.keys()
pairs_dict = {}
for pair in pairs:
    pairs_dict[pair] = 0
for ch in range(len(template)-1):
    pairs_dict[template[ch:ch+2]] += 1

STEPS = 40
for step in range(STEPS):
    new_dict = {key : 0 for key in rules_dict.keys()}
    for key, value in pairs_dict.items():
        new_dict[rules_dict[key][0]] += value
        new_dict[rules_dict[key][1]] += value
    pairs_dict = new_dict

alfabet = list(set([i[0] for i in pairs]))
sizes = [0]*len(alfabet)
for key, value in pairs_dict.items():
    sizes[alfabet.index(key[0])] += value
sizes[alfabet.index(template[-1])] += 1

for i, ch in enumerate(alfabet):
    print(ch, sizes[i])
print(max(sizes)-min(sizes))