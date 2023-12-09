from typing import List


def predict(nums: List[int]) -> int:
    scans = [nums]
    all_zero = False
    row = 0
    while not all_zero:
        
        diffs = []
        for i in range(1, len(scans[row])):
            diffs.append(scans[row][i] - scans[row][i - 1])

        row += 1

        if all(d == 0 for d in diffs):
            diffs.append(0)
            all_zero = True
        
        scans.append(diffs)    

    
    for i in reversed(range(len(scans) - 1)):
        first = scans[i][len(scans[i]) - 1]
        s = scans[i+1][len(scans[i+1]) - 1]
        scans[i].append(first + s)

    
    return scans[0][len(scans[0]) - 1]




with open('input.txt', 'r') as file:
    lines = file.readlines()

total = 0
for line in lines:
    nums = list(map(int, line.split()))
    print(nums)
    total += predict(nums)

print(total)