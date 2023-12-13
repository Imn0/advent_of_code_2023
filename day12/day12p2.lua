local cache = {}

cache_hits = 0
function count(cfg, nums)
    if cfg == "" then
        return #nums == 0 and 1 or 0
    end

    if #nums == 0 then
        return cfg:find("#") and 0 or 1
    end

    local key = cfg .. ":" .. table.concat(nums, ",")

    if cache[key] then
        cache_hits = cache_hits + 1
        return cache[key]
    end

    local result = 0

    if cfg:sub(1, 1) == "." or cfg:sub(1, 1) == "?" then
        result = result + count(string.sub(cfg, 2), nums)
    end

    if cfg:sub(1, 1) == "#" or cfg:sub(1, 1) == "?" then
        if nums[1] <= #cfg and not string.find(cfg:sub(1, nums[1]), "%.") and (nums[1] == #cfg or cfg:sub(nums[1] + 1, nums[1] + 1) ~= "#") then
            result = result + count(cfg:sub(nums[1] + 2), {table.unpack(nums, 2)})
        end
    end

    cache[key] = result
    return result
end


function tableToString(tbl)
    local str = "{"
    for i, v in ipairs(tbl) do
      if type(v) == "table" then
        str = str .. tableToString(v)
      else
        str = str .. tostring(v)
      end
      if i < #tbl then
        str = str .. ","
      end
    end
    str = str .. "}"
    return str
end


function CalculateCombinations(str)
    local pattern, nums = str:match("(%S+)%s+(.*)")
    pattern = pattern .. "?" .. pattern .. "?" .. pattern .. "?" .. pattern .. "?" .. pattern
    nums = nums .. "," .. nums .. "," ..  nums .. "," ..  nums .. "," .. nums

    local numTable = {}
    for num in nums:gmatch("(%d+)") do
        table.insert(numTable, tonumber(num))
    end
    return count(pattern, numTable)
end


local file = io.open("input.txt", "r")

total = 0

for line in file:lines() do
    c =  CalculateCombinations(line)
    total = total + c
end

print(total)
print("cache hits", cache_hits)

file:close()
