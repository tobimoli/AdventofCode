file = "/Users/tobiasmolenaar/Documents/GitHub/AdventofCode/2024/Day03/input_day.txt"

using DelimitedFiles

global total = 0
for i in eachline(file)
    for j in findall("mul(", i)
        start = j[end] + 1
        digit1 = ""
        for k in [0, 1, 2]
            if all(isdigit, i[start:start+k])
                digit1 = parse(Int64, i[start:start+k])
                global len = k + 1
            end
        end
        if digit1 == ""
            break
        end

        if i[start+len] != ','
            break
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
            break
        end

        if i[start+len] != ')'
            break
        end
        println("")
        println(digit1)
        println(digit2)
        println(digit1 * digit2)
        global total += digit1 * digit2
    end
end
println(total)
