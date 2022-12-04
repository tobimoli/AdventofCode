# %%
import os
import re
import numpy as np
os.chdir('/Users/tobiasmolenaar/Documents/GitHub/AdventofCode/2022/Day04/')
with open("input_day4.txt", "r") as f:
    data = f.read().split("\n")

# part 1 & 2
full_overlaps = 0
partially_overlaps = 0
for section_pair in data:
    s1, e1, s2, e2 = map(int, re.match("(\d+)-(\d+),(\d+)-(\d+)", section_pair).groups())
    
    set1 = set(range(s1, e1 + 1))
    set2 = set(range(s2, e2 + 1))
    overlap = set1 & set2
    
    if len(overlap) > 0:
        partially_overlaps += 1
    if len(overlap) == len(set1) or len(overlap) == len(set2):
        full_overlaps += 1

print(full_overlaps)
print(partially_overlaps)