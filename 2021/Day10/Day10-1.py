import numpy as np
filename = 'input_day10.txt'
input = np.loadtxt(filename, skiprows=0, dtype=str)
#input = ['[({(<(())[]>[[{[]{<()<>>','[(()[<>])]({[<{<<[]>>(','{([(<{}[<>[]}>{[]{[(<()>','(((({<>}<{<{<>}{[]{[]{}','[[<[([]))<([[{}[[()]]]','[{[{({}]{}}([{[{{{}}([]','{<[[]]>}<{[{[{[]{()[[[]','[<(<(<(<{}))><([]([]()','<{([([[(<>()){}]>(<<{{','<{([{{}}[<[[[<>{}]]]>[]]']

size = len(input)
brackets_open = ['(', '[', '{', '<']
brackets_close = [')', ']', '}', '>']
brackets_pairs = ['()', '[]', '{}', '<>']
syntax_error = {')':1,']':2,'}':3,'>':4}
SCORES = []
def corrupted(line):
    copy = line
    done = False
    corrupt = False
    while not done:
        for br in brackets_pairs:
            if br in copy:
                copy = copy.replace(br,'')
        done = True
        for br in brackets_pairs:
            if br in copy:
                done = False
    indices = []
    brackets = []
    for i,b_open in enumerate(brackets_open):
        for j,b_close in enumerate(brackets_close):
            if i!=j and copy.find(b_open+b_close) != -1:
                indices.append(copy.find(b_open+b_close))
                brackets.append(b_close)
                corrupt = True
    if indices == []:
        bracket = ''
    else:
        bracket = brackets[np.argmin(indices)]
    return corrupt, bracket

def complete(line):
    copy = line
    done = False
    string = ''
    while not done:
        for br in brackets_pairs:
            if br in copy:
                copy = copy.replace(br,'')
        done = True
        for br in brackets_pairs:
            if br in copy:
                done = False
    for char in copy[::-1]:
        string += brackets_close[brackets_open.index(char)]
    return copy, string

for line in input:
    corrupt, bracket = corrupted(line)
    if not corrupt:
        score = 0
        _, fill = complete(line)
        for ch in fill:
            score = score * 5
            score += syntax_error[ch]
        SCORES.append(score)

SCORES.sort()
middle = (len(SCORES)-1)//2

print(SCORES[middle])