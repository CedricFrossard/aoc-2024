directions = {
    {-1, 0}, -- left --
    {0 , -1}, -- up --
    {1, 0}, -- right --
    {0, 1}, -- down --
}

function findUser(lines) 
    for i,line in pairs(lines) do
        for j,c in pairs(line) do 
            if (c == '>' or c == '<' or c == 'V' or c == '^') then
                return {j,i}
            end
        end
    end
end

function tablelength(T)
    local count = 0
    for _ in pairs(T) do count = count + 1 end
    return count
  end

  
function getOrientation(c)
    if (c == '<') then
        return 1
    elseif (c == '^') then
        return 2
    elseif (c == '>') then
        return 3
    elseif (c == 'V') then
        return 4
    end
end

file = io.open("./input", "r")
io.input(file)
-- maze = io.read("*a")

lines = {}
for line in io.lines("./input") do
    local split = {}
    for c in line:gmatch '.' do
        split[#split + 1] = c
    end 
    lines[#lines + 1] = split
end


startingPoint = findUser(lines);
startCharacter = lines[startingPoint[2]][startingPoint[1]]
--default orientation
function solvePart1()
    local step = 1
    local position = startingPoint
    local orientation = getOrientation(startCharacter)
    local continue = true
    local uniquePositions = {}
    uniquePositions[position[2]..'-'..position[1]] = 'X'
    while ( continue ) do
        local x = position[1] + directions[orientation][1]
        local y = position[2] + directions[orientation][2]
        
        if (x < 1 or x > #(lines[1]) or y < 1 or y > #(lines)) then
            continue = false -- out of bound
        elseif (lines[y][x] == '#') then
            continue = true -- out of bound
            orientation = orientation%4 +1
        else 
            position[1] = x
            position[2] = y

            uniquePositions[y..'-'..x] = 'X'
        end
    end
    return tablelength(uniquePositions)
end

print(solvePart1(directions, lines))