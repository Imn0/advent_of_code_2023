import numpy as np


grid = open('input.txt').read().split('\n')
grid = np.array([list(row) for row in grid])

[(start_r, start_c)] = list(zip(*np.where(grid == 'S')))

grid[start_r][start_c] = 'O'

for _ in range(64):
    points = list(zip(*np.where(grid == 'O')))
    for r, c in points:
        if r > 0 and grid[r - 1][c] == '.':
            grid[r - 1][c] = 'O'
        if r < len(grid) - 1 and grid[r + 1][c] == '.':
            grid[r + 1][c] = 'O'
        if c > 0 and grid[r][c - 1] == '.':
            grid[r][c - 1] = 'O'
        if c < len(grid[0]) - 1 and grid[r][c + 1] == '.':
            grid[r][c + 1] = 'O'
        grid[r][c] = '.'

print(np.sum(grid == 'O'))

print(grid)
      