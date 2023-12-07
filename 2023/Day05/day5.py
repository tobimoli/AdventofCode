f = open("input_day5.txt", "r")
data = f.read().split("\n\n")
f.close()

seed, *others = data
seed = [int(i) for i in seed.split(":")[1].split()]

class Function:
    def __init__(self, S) -> None:
        lines = S.split("\n")[1:]
        self.tuples = [[int(x) for x in line.split()] for line in lines]
    def apply_one(self, x: int) -> int:
        for (dst, src, sz) in self.tuples:
            if src <= x < (src + sz):
                return x + dst - src
        return x
    def apply_range(self, R):
        A = []
        for (dest, src, size) in self.tuples:
            src_end = src + size
            NR = []
            while R:
                (st, ed) = R.pop()

                before = (st, min(ed, src))
                inter = (max(st, src), min(src_end, ed))
                after = (max(src_end, st), ed)
                if before[1] > before[0]:
                    NR.append(before)
                if inter[1] > inter[0]:
                    A.append((inter[0] - src + dest, inter[1] - src + dest))
                if after[1] > after[0]:
                    NR.append(after)
            R = NR
        return A + R

# part 1
P1 = []
Fs = [Function(s) for s in others]
for x in seed:
    for f in Fs:
        x = f.apply_one(x)
    P1.append(x)
print(min(P1))

# part 2
P2 = []
pairs = list(zip(seed[::2], seed[1::2]))
for start, length in pairs:
    R = [(start, start + length)]
    for f in Fs:
        R = f.apply_range(R)
    P2.append(min(R)[0])
print(min(P2))