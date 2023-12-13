function generateCombinations(str, index, current, nums)
    if index > #str then
        return IsPatternValid(current, nums)
    end

    local char = string.sub(str, index, index)
    local result = 0
    if char == '?' then
        result = result + generateCombinations(str, index + 1, current .. '#', nums)
        result = result + generateCombinations(str, index + 1, current .. '.', nums)
    else
        result = result + generateCombinations(str, index + 1, current .. char, nums)
    end
    return result
end

function CalculateCombinations(str)
    local pattern, nums = str:match("(%S+)%s+(.*)")
    local numTable = {}
    for num in nums:gmatch("(%d+)") do
        table.insert(numTable, tonumber(num))
    end
    return generateCombinations(pattern,1 ,"" , numTable)
end

function IsPatternValid(inputString, nums)
    local result = {}
    for substring in inputString:gmatch("([^%.]+)") do
        table.insert(result, #substring)
    end

    if #result ~= #nums then
        return 0
    end

    for i, value in ipairs(result) do
        if value ~= nums[i] then
            return 0
        end
    end

    return 1
end

local file = io.open("input.txt", "r")

total = 0

for line in file:lines() do
    total = total + CalculateCombinations(line)
end

print(total)
file:close()
