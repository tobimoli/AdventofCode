file = "/Users/tobiasmolenaar/Documents/GitHub/AdventofCode/2024/Day04/input_day.txt"

using DelimitedFiles
using LinearAlgebra

println("part1")
global total = 0
global xmas = "XMAS"

lines = map(collect, readlines(file))
grid = permutedims(hcat(lines...))
for col = 1:size(grid, 2)
    for row = 1:size(grid, 1)
        if grid[row, col] == 'X'
            # verticaal
            try
                if join(grid[row:1:row+3, col]) == xmas
                    println(row, ", ", col, ", 1v")
                    global total += 1
                end
            catch
            end
            try
                if join(grid[row:-1:row-3, col]) == xmas
                    println(row, ", ", col, ", 3v")
                    global total += 1
                end
            catch
            end
            # horizontaal
            try
                if join(grid[row, col:1:col+3]) == xmas
                    println(row, ", ", col, ", 1h")
                    global total += 1
                end
            catch
            end
            try
                if join(grid[row, col:-1:col-3]) == xmas
                    println(row, ", ", col, ", 3h")
                    global total += 1
                end
            catch
            end
            # diagonaal
            try
                if join(diag(grid[row:1:row+3, col:1:col+3])) == xmas
                    println(row, ", ", col, ", 1d")
                    global total += 1
                end
            catch
            end
            try
                if join(diag(grid[row:1:row+3, col:-1:col-3])) == xmas
                    println(row, ", ", col, ", 2d")
                    global total += 1
                end
            catch
            end
            try
                if join(diag(grid[row:-1:row-3, col:-1:col-3])) == xmas
                    println(row, ", ", col, ", 3d")
                    global total += 1
                end
            catch
            end
            try
                if join(diag(grid[row:-1:row-3, col:1:col+3])) == xmas
                    println(row, ", ", col, ", 4d")
                    global total += 1
                end
            catch
            end
        end
    end
end
print(total)

println("part2")
global total = 0
global mas = "MAS"

for col = 1:size(grid, 2)
    for row = 1:size(grid, 1)
        if grid[row, col] == 'A'
            # \ v
            try
                if (join(diag(grid[row-1:1:row+1, col-1:1:col+1])) == mas) | (join(diag(grid[row+1:-1:row-1, col+1:-1:col-1])) == mas)
                    if (join(diag(grid[row+1:-1:row-1, col-1:1:col+1])) == mas) | (join(diag(grid[row-1:1:row+1, col+1:-1:col-1])) == mas)
                        global total += 1
                    end
                end
            catch
            end
        end
    end
end
print(total)