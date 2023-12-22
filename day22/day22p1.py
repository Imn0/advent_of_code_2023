from typing import List

def overlapping(brick1: List[int], brick2: List[int]) -> bool:
    return max(brick1[0], brick2[0]) <= min(brick1[3], brick2[3]) and max(brick1[1], brick2[1]) <= min(brick1[4], brick2[4])

# stat v   end v
# [x,y,z , x,y,z]
bricks = [[int(b) for b in (a.replace('~', ',').split(','))] for a in open('input.txt').read().split('\n')]
bricks.sort(key=lambda x: x[2])


for i, brick in enumerate(bricks):
    max_z = 1 
    for current_brick in bricks[:i]:
        if overlapping(brick, current_brick):
            max_z = max(max_z, current_brick[5] + 1)
    brick[5] -= brick[2] - max_z
    brick[2] = max_z

bricks.sort(key=lambda x: x[2])

brick_supports_key = {i: 0  for i in range(len(bricks))}
key_supports_brick = {i: set() for i in range(len(bricks))}

for i, upper_brick in enumerate(bricks):
    for j, lower_brick in enumerate(bricks[:i]):
        if overlapping(lower_brick, upper_brick) and lower_brick[5] + 1 == upper_brick[2]:
            key_supports_brick[j].add(i)
            brick_supports_key[i] += 1

total = 0
for i, brick in enumerate(bricks):
    if all(brick_supports_key[j] >= 2 for j in key_supports_brick[i]):
        total += 1

print(total)