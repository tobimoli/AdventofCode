f = open('input_day1.txt', 'r')
data = f.read().split()
data = list(map(int, data))
f.close()

answer = 0
for i in range(3, len(data)):
    if sum(data[i-3:i]) < sum(data[i-2:i+1]):
        answer += 1

print(answer)