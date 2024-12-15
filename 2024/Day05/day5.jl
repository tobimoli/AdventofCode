file = "/Users/tobiasmolenaar/Documents/GitHub/AdventofCode/2024/Day05/input_day.txt"

using DelimitedFiles
using LinearAlgebra

global first = Dict()
global last = Dict()

for line in eachline(file)
    if '|' in line
        i, j = split(line, "|")
        if haskey(first, i)
            first[i] = push!(first[i], j)
        else
            first[i] = [j]
        end
        if haskey(last, j)
            last[j] = push!(last[j], i)
        else
            last[j] = [i]
        end
    end
end

function is_item_ordered(update, item)
    index_item = findfirst(q -> q == item, update)
    if haskey(first, item)
        for other_item in first[item]
            if other_item in update
                index_other_item = findfirst(q -> q == other_item, update)
                if index_other_item < index_item
                    return false
                end
            end
        end
    end
    if haskey(last, item)
        for other_item in last[item]
            if other_item in update
                index_other_item = findfirst(q -> q == other_item, update)
                if index_other_item > index_item
                    return false
                end
            end
        end
    end
    return true
end

function is_ordered(update)
    items = split(update, ",")
    for item in items
        if !is_item_ordered(items, item)
            return false
        end
    end
    return true
end

println("part1")
global total = 0
for line in eachline(file)
    if ',' in line
        if is_ordered(line)
            local x = split(line, ",")
            global total += parse(Int64, x[div(length(x) + 1, 2)])
        end
    end
end
println(total)

function order_line(update)
    len = length(split(update, ","))
    while !is_ordered(update)
        items = split(update, ",")
        for index in 1:len-1
            # als items[index+1] | items[index] dan swappen
            if haskey(last, items[index])
                if items[index+1] in last[items[index]]
                    # swap items
                    items = vcat(items[1:index-1], [items[index+1]], [items[index]], items[index+2:end])
                end
            end
        end
        update = join(items, ',')
    end
    items = split(update, ",")
    return parse(Int64, items[div(len + 1, 2)])
end

function create_order()
end

println("part2")
global total = 0
for line in eachline(file)
    if ',' in line
        if !is_ordered(line)
            global total += order_line(line)
        end
    end
end
println(total)
