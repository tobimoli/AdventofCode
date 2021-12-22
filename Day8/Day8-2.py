import numpy as np
filename = 'input_day8.txt'
input = np.loadtxt(filename, delimiter=' ', skiprows=0, dtype=str)
#input = [['be','cfbegad','cbdgef','fgaecd','cgeb','fdcge','agebfd','fecdb','fabcd','edb','|','fdgacbe','cefdb','cefbgd','gcbe']]

size = len(input)
# AAA
# B C
# DDD
# E F
# GGG
def length(list):
    #returns list of lengths of strings in the list
    lst = [0]*len(list)
    for i, item in enumerate(list):
        lst[i] = len(item)
    return np.array(lst)

def abc_ABC(list):
    array = np.array(list)
    abc = {}
    numbers = {}
    abcd = 'abcdefg'
    LENGTH = length(list)
    numbers[1] = array[LENGTH == 2][0]
    numbers[4] = array[LENGTH == 4][0]
    numbers[7] = array[LENGTH == 3][0]
    abc[str(set(numbers[7]) - set(numbers[1]))[2]] = 'A'
    for letter in abcd:
        som = 0
        for string in list:
            if letter in string:
                som += 1
        if som == 6:
            abc[letter] = 'B'
        elif som == 4:
            abc[letter] = 'E'
        elif som == 9:
            abc[letter] = 'F'
            abc[str(set(numbers[1]) - set(letter))[2]] = 'C'
    for letter in numbers[4]:
        if letter not in abc:
            abc[letter] = 'D'
    for letter in abcd:
        if letter not in abc:
            abc[letter] = 'G'
    return abc

def find_number(list, abc):
    #find all combinations 
    numbers = ''
    new_list = [''] * len(list)
    for i, string in enumerate(list):
        for char in string:
            new_list[i] += abc[char]
    for number in new_list:
        num = seven_seg_to_number(number.upper())
        numbers += str(num)
    return numbers

def seven_seg_to_number(string):
    if len(string) == 2:
        return 1
    elif len(string) == 3:
        return 7
    elif len(string) == 7:
        return 8
    elif len(string) == 4:
        return 4
    elif 'D' not in string:
        return 0
    elif 'B' not in string and 'E' not in string:
        return 3
    elif 'B' not in string and 'F' not in string:
        return 2
    elif 'C' not in string and 'E' not in string:
        return 5
    elif 'C' not in string:
        return 6
    elif 'E' not in string:
        return 9
    else:
        return 'something wrong in input string'

SOM = 0
for line in input:
    abc = abc_ABC(line[:10])
    numbers = find_number(line[11:], abc)
    SOM += int(numbers)

print('Sum =', SOM)