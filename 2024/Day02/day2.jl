file = "/Users/tobiasmolenaar/Documents/GitHub/AdventofCode/2024/Day02/input_day.txt"

using DelimitedFiles

max_dist = 3
min_dist = 1

function is_safe(numbers)
    first_num = numbers[1]
    second_num = numbers[2]

    direction = sign(second_num - first_num)
    if direction == 0
        return false
    end
    for num in numbers[2:end]
        diff = num - first_num
        if (abs(diff) < min_dist) | (abs(diff) > max_dist)
            return false
        end
        if sign(diff) != direction
            return false
        end
        first_num = num
    end
    return true
end

# part 1
n_safe = 0
for safe in eachline(file)
    safe = [parse(Int64, y) for y in split(safe)]
    if is_safe(safe)
        global n_safe += 1
    end
end
print(n_safe)

# part 2
print('\n')
n_safe = 0
for safe in eachline(file)
    safe = [parse(Int64, y) for y in split(safe)]
    local bool_safe = false
    if is_safe(safe)
        bool_safe = true
    else
        for i = 1:length(safe)
            if is_safe(safe[setdiff(1:end, i)])
                bool_safe = true
            end
        end
    end
    global n_safe += bool_safe
end
print(n_safe)