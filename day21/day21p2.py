import numpy as np
from tqdm import tqdm


class Point:
    def __init__(self, r, c, actual_r, actual_c):
        self.r = r
        self.c = c
        self.actual_r = actual_r
        self.actual_c = actual_c

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Point):
            return False
        return self.actual_c == __value.actual_c and self.actual_r == __value.actual_r

    def __hash__(self) -> int:
        return hash((self.actual_r, self.actual_c))


grid = open('input.txt').read().split('\n')
grid = np.array([list(row) for row in grid])

[(start_r, start_c)] = list(zip(*np.where(grid == 'S')))
grid[start_r][start_c] = '.'
points = [Point(start_r, start_c, start_r, start_c)]

size = len(grid)

answers = []

for i in range(3*size):
    current = []
    
    for point in points:
        r = point.r
        c = point.c
        actual_r = point.actual_r
        actual_c = point.actual_c
        if grid[(r-1) % size][c] == '.':
            current.append(Point((r-1) % size, c, actual_r-1, actual_c))
        if grid[(r+1) % size][c] == '.':
            current.append(Point((r+1) % size, c, actual_r+1, actual_c))
        if grid[r][(c-1) % size] == '.':
            current.append(Point(r, (c-1) % size, actual_r, actual_c-1))
        if grid[r][(c+1) % size] == '.':
            current.append(Point(r, (c+1) % size, actual_r, actual_c+1))
    

    points = current.copy()
    points = list(set(points))
    if i % size == 64:
        print(len(points))
        answers.append(len(points))
        if len(answers) == 3:
            break

print(answers)


goal = 26501365
def f(n):
    a0 = answers[0]
    a1 = answers[1]
    a2 = answers[2]

    b0 = a0
    b1 = a1-a0
    b2 = a2-a1
    return b0 + b1*n + (n*(n-1)//2)*(b2-b1)
print(f(goal//size))

