file = "input"
# file = "example"


f = open(f'{file}.txt', 'r')
data = f.read().split('\n')
f.close()

data = data[0]

# part 1
down = data.count(")")
up = data.count("(")

print(up - down)

# part 2
floor = 0
for i, ch in enumerate(data):
    if ch == ")":
        floor -= 1
    else:
        floor += 1
    
    if floor == -1:
        print(i + 1)
        break