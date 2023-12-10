import numpy as np

f = open("input_day.txt", "r")
data = f.read().split("\n")
f.close()

data = np.array([[i for i in row] for row in data])
max_rows = len(data)
max_cols = len(data[0])

def two_connections(pipe1: tuple):
    row, col = pipe1
    if data[pipe1] == ".":
        connections = []
    elif data[pipe1] == "L":
        connections = [(row - 1, col), (row, col + 1)]
    elif data[pipe1] == "J":
        connections = [(row - 1, col), (row, col - 1)]
    elif data[pipe1] == "|":
        connections = [(row - 1, col), (row + 1, col)]
    elif data[pipe1] == "-":
        connections = [(row, col + 1), (row, col - 1)]
    elif data[pipe1] == "F":
        connections = [(row, col + 1), (row + 1, col)]
    elif data[pipe1] == "7":
        connections = [(row + 1, col), (row, col - 1)]
    else: # pipe1 is start position
        connections = []
        surrounding = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
        for pipe in surrounding:
            if pipe1 in two_connections(pipe):
                connections.append(pipe)
    return connections


# find index of start position
start = np.where(data == "S")
start = (start[0][0], start[1][0])

# find two connecting pipes
connections_start = two_connections(start)
# just take one connections
next_connection = connections_start[0]
connections = [start, next_connection]

while next_connection != start:
    previous_connection = connections[-2]
    current_connection = connections[-1]
    possible_connections = two_connections(current_connection)

    if possible_connections[0] == previous_connection:
        next_connection = possible_connections[1]
    else:
        next_connection = possible_connections[0]
    if next_connection != start:
        connections.append(next_connection)
    
print(len(connections) // 2)

# part 2
# replace each pipe in the data by "." if not in the loop
all_indices = [(i, j) for i in range(max_rows) for j in range(max_cols)]
for ind in all_indices:
    if ind not in connections:
        data[ind] = "."

# make every outside . an O
side_indices = [i for i in all_indices if (i[0] == 0) or (i[0] == max_rows - 1) or (i[1] == 0) or (i[1] == max_cols - 1)]
for ind in side_indices:
    if ind not in connections:
        data[ind] = "O"

# make every . connected to O an O
new_O = [1]
while len(new_O) > 0:
    new_O = []
    dot_indices = [i for i in all_indices if data[i] == "."]
    for dot_ind in dot_indices:
        row, col = dot_ind
        surrounding = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1),
                    (row + 1, col + 1), (row + 1, col - 1), (row - 1, col - 1), (row - 1, col + 1)]
        if any([data[i] == "O" for i in surrounding]):
            data[dot_ind] = "O"
            new_O.append(dot_ind)

# find out if rest of dots are enclosed
# start with a pipe on the edge of the loop and use the fact that the orientation (right or left)
# must be the same. If on the right are O's than this is for the rest.

# find a start
search = np.array([0, 0])
loop_found = False
while not loop_found:
    search += np.array([1, 1])
    if data[tuple(search)] in ["-", "|", "F", "L", "J", "7"]:
        loop_found = True
        loop_start = tuple(search)

# find orientation of O's for loop_start
if data[loop_start] == "-":
    orientation = "N"
elif data[loop_start] == "7":
    orientation = "NE"
elif data[loop_start] == "|":
    orientation = "W"
elif data[loop_start] == "J":
    orientation = "NW"
elif data[loop_start] == "L":
    orientation = "SW"
else: # F
    orientation = "NW"

def where_to_look(index: tuple, orientation: str):
    row, col = index
    if orientation == "N":
        look = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1)]
    elif orientation == "NE":
        look = [(row - 1, col), (row - 1, col + 1), (row, col + 1)]
    elif orientation == "E":
        look = [(row - 1, col + 1), (row, col + 1), (row + 1, col + 1)]
    elif orientation == "SE":
        look = [(row, col + 1), (row + 1, col + 1), (row + 1, col)]
    elif orientation == "S":
        look = [(row + 1, col - 1), (row + 1, col + 1), (row + 1, col)]
    elif orientation == "SW":
        look = [(row, col - 1), (row + 1, col - 1), (row + 1, col)]
    elif orientation == "W":
        look = [(row, col - 1), (row + 1, col - 1), (row - 1, col - 1)]
    else: # NW
        look = [(row, col - 1), (row - 1, col - 1), (row - 1, col)]
    
    # verwijder items buiten de map
    looks = []
    for i in look:
        if (i[0] >= 0) and (i[1] >= 0) and (i[0] < max_rows) and (i[1] < max_cols):
            looks.append(i)
    return looks


def find_new_orientation(orient, pr_con, con):
    if pr_con == con: # the same connection
        return orient
    elif pr_con == "|":
        if con in ["F", "J"]:
            if orient == "E":
                return "SE"
            else: #W
                return "NW"
        else: #con in ["7", "L"]:
            if orient == "E":
                return "NE"
            else: #W
                return "SW"
    elif pr_con == "-":
        if con in ["F", "J"]:
            if orient == "N":
                return "NW"
            else: #S
                return "SE"
        else: # con in ["7", "L"]
            if orient == "N":
                return "NE"
            else:
                return "SW"
    elif pr_con == "F":
        if con == "J":
            return orient
        if orient == "NW":
            if con == "-":
                return "N"
            elif con == "|":
                return "W"
            elif con == "7":
                return "NE"
            else: # L
                return "SW"
        else: # SE
            if con == "-":
                return "S"
            elif con == "|":
                return "E"
            elif con == "7":
                return "SW"
            else: # L
                return "NE"
    elif pr_con == "J":
        if con == "F":
            return orient
        if orient == "NW":
            if con == "-":
                return "N"
            elif con == "|":
                return "W"
            elif con == "7":
                return "SW"
            else: # L
                return "NE"
        else: #SE
            if con == "-":
                return "S"
            elif con == "|":
                return "E"
            elif con == "7":
                return "NE"
            else: # L
                return "SW"
    elif pr_con == "7":
        if con == "L":
            return orient
        if orient == "NE":
            if con == "-":
                return "N"
            elif con == "|":
                return "E"
            elif con == "J":
                return "SE"
            else: # F
                return "NW"
        else: #SW
            if con == "-":
                return "S"
            elif con == "|":
                return "W"
            elif con == "J":
                return "NW"
            else: # F
                return "SE"
    else: # L
        if con == "7":
            return orient
        if orient == "NE":
            if con == "-":
                return "N"
            elif con == "|":
                return "E"
            elif con == "J":
                return "NW"
            else: # F
                return "SE"
        else: #SW
            if con == "-":
                return "S"
            elif con == "|":
                return "W"
            elif con == "J":
                return "SE"
            else: # F
                return "NW"


# loop over the loop and compute orientation, set dots to O if they are on orientation side
# first find where to start in connections
index_start = 0
for i, c in enumerate(connections):
    if c == loop_start:
        index_start = i

i = index_start
next_connection = connections[(i + 1) % len(connections)]
previous_connection = connections[i % len(connections)]
while next_connection != loop_start:
    # find new orientation
    print(previous_connection, orientation)
    orientation = find_new_orientation(orientation, data[previous_connection], data[next_connection])
    look = where_to_look(next_connection, orientation)
    for ind in look:
        if data[ind] == ".":
            data[ind] = "O"
    i += 1
    next_connection = connections[(i + 1) % len(connections)]
    previous_connection = connections[i % len(connections)]

# make every . connected to O an O
new_O = [1]
while len(new_O) > 0:
    new_O = []
    dot_indices = [i for i in all_indices if data[i] == "."]
    
    for dot_ind in dot_indices:
        row, col = dot_ind
        surrounding = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1),
                    (row + 1, col + 1), (row + 1, col - 1), (row - 1, col - 1), (row - 1, col + 1)]
        if any([data[i] == "O" for i in surrounding]):
            data[dot_ind] = "O"
            new_O.append(dot_ind)

print((data == ".").sum())