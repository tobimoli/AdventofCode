import heapq

f = open("input_day.txt", "r")
data = f.read().split("\n")
f.close()

data = {(i, j): int(h) for i, r in enumerate(data) for j, h in enumerate(r)}

start = min(data)
end = max(data)

def minimal_heat(least, most):
    queue = [(0, *start, 0, 0)]
    seen = set()
    while queue:
        heat,x,y,px,py = heapq.heappop(queue)
        if (x, y) == end: 
            return heat
        if (x, y, px, py) in seen: 
            continue
        seen.add((x, y, px, py))
        # calculate turns only
        for dx, dy in {(1,0),(0,1),(-1,0),(0,-1)}-{(px, py),(-px, -py)}:
            a, b, h = x, y, heat
            # enter 4-10 moves in the chosen direction
            for i in range(1, most + 1):
                a, b = a + dx, b + dy
                if (a, b) in data:
                    h += data[a,b]
                    if i >= least:
                        heapq.heappush(queue, (h, a, b, dx, dy))

print(minimal_heat(1, 3))
print(minimal_heat(4, 10))