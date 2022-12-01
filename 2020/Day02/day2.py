# %%
import os
import re
os.chdir('/Users/tobiasmolenaar/Documents/GitHub/AdventofCode/2020/Day02/')

f = open('input_day2.txt', 'r')
data = f.read().split('\n')
f.close()

# part 1
passwords_valid = 0
for item in data:
    min_letter, max_letter, letter, password = re.match(r"(\d+)-(\d+) (\w): (\w+)", item).groups()
    
    letter_occurance = password.count(letter)

    if letter_occurance >= int(min_letter):
        if letter_occurance <= int(max_letter):
            passwords_valid += 1

print(passwords_valid)

# part 2
passwords_valid = 0
for item in data:
    index1, index2, letter, password = re.match(r"(\d+)-(\d+) (\w): (\w+)", item).groups()
    
    cond1 = password[int(index1)-1] == letter
    cond2 = password[int(index2)-1] == letter
    if cond1 + cond2 == 1:
        passwords_valid += 1

print(passwords_valid)