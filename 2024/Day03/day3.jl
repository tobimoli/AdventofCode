file = "/Users/tobiasmolenaar/Documents/GitHub/AdventofCode/2024/Day03/input_day.txt"

using DelimitedFiles

println("part1")
global total = 0
for i in eachline(file)
    for j in findall("mul(", i)
        is_correct = true
        start = j[end] + 1
        digit1 = ""
        for k in [0, 1, 2]
            if all(isdigit, i[start:start+k])
                digit1 = parse(Int64, i[start:start+k])
                global len = k + 1
            end
        end
        if digit1 == ""
            is_correct = false
        end
        if i[start+len] != ','
            is_correct = false
        end

        start = j[end] + len + 2
        digit2 = ""
        for k in [0, 1, 2]
            if all(isdigit, i[start:start+k])
                digit2 = parse(Int64, i[start:start+k])
                global len = k + 1
            end
        end
        if digit2 == ""
            is_correct = false
        end
        if i[start+len] != ')'
            is_correct = false
        end
        if is_correct
            global total += digit1 * digit2
        end
    end
end
println(total)
