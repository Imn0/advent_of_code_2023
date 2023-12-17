from heapq import heappush, heappop

gird = [list(map(int, line.strip())) for line in open('smol.txt').readlines()]

seen = set()
# heat loss, row, col, direction_row, direction_col, steps
q = [(0, 0, 0, 0, 0, 0)]
while q:
    heat_loss, row, col, direction_row, direction_col, steps = heappop(q)

    if row == len(gird) - 1 and col == len(gird[0]) - 1:
        print(heat_loss)
        break

    if (row, col, direction_row, direction_col, steps) in seen:
        continue

    seen.add((row, col, direction_row, direction_col, steps)) 

    if steps < 3:
        new_row = row + direction_row
        new_col = col + direction_col
        if new_row >= 0 and new_col >= 0 and new_row < len(gird) and new_col < len(gird[0]):
            heappush(q, (heat_loss + gird[new_row][new_col], new_row, new_col, direction_row, direction_col, steps + 1))

    for new_direction_row, new_direction_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if (new_direction_row, new_direction_col) == (direction_row, direction_col) or (new_direction_row, new_direction_col) == (-direction_row, -direction_col):
            continue
        new_row = row + new_direction_row
        new_col = col + new_direction_col
        if new_row >= 0 and new_col >= 0 and new_row < len(gird) and new_col < len(gird[0]):
            heappush(q, (heat_loss + gird[new_row][new_col], new_row, new_col, new_direction_row, new_direction_col, 1))
