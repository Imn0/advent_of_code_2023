from typing import List
from collections import deque

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

key_supports_brick = {i: set() for i in range(len(bricks))}
brick_supports_key = {i: set() for i in range(len(bricks))}

for i, upper_brick in enumerate(bricks):
    for j, lower_brick in enumerate(bricks[:i]):
        if overlapping(lower_brick, upper_brick) and lower_brick[5] + 1 == upper_brick[2]:
            key_supports_brick[j].add(i)
            brick_supports_key[i].add(j)

total = 0
for i in range(len(bricks)):
    # all bricks that are directly supported by only this brick
    fall_q = deque(j for j in key_supports_brick[i] if len(brick_supports_key[j]) == 1)
    falling_bricks = set(fall_q)

    while fall_q:
        brick = fall_q.popleft()
        for j in key_supports_brick[brick] - falling_bricks:
            # check if current brick isn't currently falling and if all bricks that are supported by current brick are falling
            if j not in falling_bricks and all(k in falling_bricks for k in brick_supports_key[j]):
                fall_q.append(j)
                falling_bricks.add(j)
    total += len(falling_bricks) 
print(total)
