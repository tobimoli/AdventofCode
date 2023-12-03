f = open("input_day3.txt", "r")
data = f.read().split("\n")
f.close()

def get_check_rows(data: list, row_nr: int):
    if row_nr == 0:
        check_rows = [row_nr, row_nr + 1]
    elif row_nr == len(data) - 1:
        check_rows = [row_nr - 1, row_nr]
    else:
        check_rows = [row_nr - 1, row_nr, row_nr + 1]
    return check_rows


def get_check_cols(data: list, col_nrs: list):
    max_cols = len(data[0])
    if (col_nrs[0] == 0) and (col_nrs[-1] == max_cols - 1):
        check_cols = col_nrs
    elif col_nrs[0] == 0: # nummer begint helemaal links
        check_cols = col_nrs + [col_nrs[-1] + 1]
    elif col_nrs[-1] == max_cols - 1: # nummer eindigt helemaal rechts
        check_cols = [col_nrs[0] - 1] + col_nrs
    else:
        check_cols = [col_nrs[0] - 1] + col_nrs + [col_nrs[-1] + 1]
    return check_cols


def retrieve_numbers(string: str):
    for s in string:
        if not s.isdigit() and s != ".":
            string = string.replace(s, ".")
    numbers = string.split(".")
    numbers = [int(n) for n in numbers if n.isdigit()]
    return numbers


def retrieve_set_col_nrs(row: str, numbers: list): 
    lengths = [len(str(n)) for n in numbers]
    col_nrs = [[] for _ in range(len(numbers))]
    nr = 0
    for col_nr, s in enumerate(row):
        if s.isdigit():
            col_nrs[nr].append(col_nr)
            if len(col_nrs[nr]) == lengths[nr]:
                nr += 1
    return col_nrs


def get_surrounding(data: list, row_nr: int, col_nrs: list):
    check_rows = get_check_rows(data, row_nr)
    check_cols = get_check_cols(data, col_nrs)
    
    surrounding = []
    for row in check_rows:
        for col in check_cols:
            ch = data[row][col]
            surrounding.append(ch)
    return surrounding


def surrounding_contains_symbol(surrounding: list):
    for s in surrounding:
        if not s.isdigit() and s != ".":
            return True
    return False


def get_numbers_with_symbol(data: list):
    nrs_w_symbol = []
    for row_nr, row in enumerate(data):
        
        numbers = retrieve_numbers(row)
        set_col_nrs = retrieve_set_col_nrs(row, numbers)

        for i, col_nrs in enumerate(set_col_nrs):
            surrounding = get_surrounding(data, row_nr, col_nrs)
            if surrounding_contains_symbol(surrounding):
                nrs_w_symbol.append(numbers[i])
    return nrs_w_symbol


def get_gears(data: list):
    gears = []
    gear_locations = []
    # replace symbol other than * by .
    for i, row in enumerate(data):
        for j, r in enumerate(row):
            if not r.isdigit() and r not in ["*", "."]:
                row = row.replace(r, ".")
            if r == "*":
                gear_locations.append([i, j])
        data[i] = row
    for gear_loc in gear_locations:
        gear_numbers = []
        gear_row_nr, gear_col_nr = gear_loc
        check_rows = get_check_rows(data, gear_row_nr)
        for row in check_rows:
            numbers = retrieve_numbers(data[row])
            set_col_nrs = retrieve_set_col_nrs(data[row], numbers)
            for i, num in enumerate(numbers):
                col_nrs = set_col_nrs[i]
                min_dist = min([abs(gear_col_nr - col_nr) for col_nr in col_nrs])
                if min_dist <= 1:
                    gear_numbers.append(num)
        if len(gear_numbers) == 2:
            gears.append(gear_numbers)
    return gears

# part 1
nrs_w_symbol = get_numbers_with_symbol(data)
print(sum(nrs_w_symbol))

# part 2
gears = get_gears(data)
print(sum([i * j for i,j in gears]))
