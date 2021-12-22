import numpy as np
import os 
filename = 'input_day13.txt'

with open('Day13/' + filename, 'r') as file:
    data = file.read().split('\n')

points = data[:data.index('')]
folds = data[data.index('')+1:-1]

#points = ['6,10','0,14','9,10','0,3','10,4','4,11','6,0','6,12','4,1','0,13','10,12','3,4','3,0','8,4','1,10','2,14','8,10','9,0']
#folds = ['fold along y=7', 'fold along x=5']

x_max = np.max([int(p.split(',')[0]) for p in points])
y_max = np.max([int(p.split(',')[1]) for p in points])
paper = np.zeros(shape = (y_max+1, x_max+1))

def fold_up(paper, l):
    new_paper  = paper[:l, :]
    fold_paper = paper[l+1:,:]
    if paper.shape[0]%2 == 1:
        new_paper += fold_paper[::-1]
    else:
        new_paper[1:, :] += fold_paper[::-1]
    return new_paper

def fold_left(paper, l):
    new_paper = paper[:,:l]
    fold_paper = paper[:,l+1:]
    if paper.shape[1]%2 == 1:
        new_paper += np.flip(fold_paper, axis = 1)
    else:
        new_paper[:, 1:] += np.flip(fold_paper, axis = 1)
    return new_paper

for p in points:
    x,y = p.split(',')
    paper[int(y), int(x)] = 1

for fold in folds:
    s = fold.split(' ')[2]
    
    if s[0] == 'x':
        paper = fold_left(paper, int(s[2:]))
    elif s[0] == 'y':
        paper = fold_up(paper, int(s[2:]))

for i in range(8):
    print((paper[:,i*5:(i+1)*5]>0)*1)
    print()

