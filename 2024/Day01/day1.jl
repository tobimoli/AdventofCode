file = "/Users/tobiasmolenaar/Documents/GitHub/AdventofCode/2024/Day01/input_day1.txt"

using DelimitedFiles
x = readdlm(file, Int)

# part 1
print(sum(abs.(sort(x[:, 2]) - sort(x[:, 1]))))

# part 2
similarity = 0
for value in x[:, 1]
    occurrence = count(isequal(value), x[:, 2])
    global similarity += occurrence * value
end
print("\n")
print(similarity)