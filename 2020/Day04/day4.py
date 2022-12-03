# %%
import os
import re
import numpy as np
os.chdir('/Users/tobiasmolenaar/Documents/GitHub/AdventofCode/2020/Day04/')

with open('input_day4.txt', 'r') as f:
    data = f.read().split('\n')

REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
person_nr = 0
passports = {person_nr: {}}

for line in data:
    if line == '':
        person_nr += 1
        passports[person_nr] = {}
    else:
        pairs = line.split(' ')
        for pair in pairs:
            key, value = pair.split(':')
            passports[person_nr][key] = value

# part 1
valid_passports = 0
for person_nr, passport in passports.items():
    if len(set(passport.keys()) & set(REQUIRED_FIELDS)) == len(REQUIRED_FIELDS):
        valid_passports += 1

print(valid_passports)

# part 2
def check_year(value, min_year, max_year):
    try:
        value = int(value)
        if value >= min_year:
            if value <= max_year:
                return True
        return False
    except:
        return False
def check_hgt(value):
    try:
        height = int(value[:-2])
        if value[-2:] == 'cm':
            if height >= 150:
                if height <= 193:
                    return True
        elif value[-2:] == 'in':
            if height >= 59:
                if height <= 76:
                    return True
        return False
    except:
        return False
def check_hcl(value):
    possible_values = '0123456789abcdef'
    if len(value) == 7:
        if value[0] == '#':
            for val in value[1:]:
                if val not in possible_values:
                    return False
            return True
    return False
def check_ecl(value):
    possible_values = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if value in possible_values:
        return True
    return False
def check_pid(value):
    if len(value) == 9:
        try:
            value = int(value)
            return True
        except:
            return False
    return False

valid_passports = 0
for person_nr, passport in passports.items():
    fields = list(passport.keys())
    if len(set(fields) & set(REQUIRED_FIELDS)) == len(REQUIRED_FIELDS):
        checks = 0
        checks += check_year(passport['byr'], 1920, 2002)
        checks += check_year(passport['iyr'], 2010, 2020)
        checks += check_year(passport['eyr'], 2020, 2030)
        checks += check_hgt(passport['hgt'])
        checks += check_hcl(passport['hcl'])
        checks += check_ecl(passport['ecl'])
        checks += check_pid(passport['pid'])
        if checks == 7:
            valid_passports += 1

print(valid_passports)