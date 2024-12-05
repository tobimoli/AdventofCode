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
println(total) # 170068701


println("part2")
global total = 0
for i in eachline(file)
    does = findall("do()", i)
    does = [does[k][end] for k = 1:length(does)]
    donts = findall("don't()", i)
    donts = [donts[k][end] for k = 1:length(donts)]
    println(does, ", ", donts)
    for j in findall("mul(", i)
        is_correct = true
        start = j[end] + 1

        verschil_does = [start - d for d in does if start - d > 0]
        verschil_donts = [start - d for d in donts if start - d > 0]

        if (length(verschil_does) > 0) | (length(verschil_donts) > 0)
            if (length(verschil_does) > 0) & (length(verschil_donts) == 0)
                is_correct = true
            elseif (length(verschil_donts) > 0) & (length(verschil_does) == 0)
                is_correct = false
            else
                if verschil_does[end] < verschil_donts[end]
                    is_correct = true
                else
                    is_correct = false
                end
            end
        end
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
        # println(digit1, ", ", digit2)
        # println(verschil_does, ", ", verschil_donts, ", ", start, ", ", is_correct)
        if is_correct
            global total += digit1 * digit2
        end
    end
end
println(total)

# 102_606_584 too high
#  83_596_387 too high
# 78_683_433
