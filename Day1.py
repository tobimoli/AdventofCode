f = open('input_day1.txt', 'r')
data = f.read().split()
data = list(map(int, data))
f.close()

answer = 0
for i in range(len(data)):
    if i != 0:
        if data[i] - data[i-1] < 0:
            answer += 1
