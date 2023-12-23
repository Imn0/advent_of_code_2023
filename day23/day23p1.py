def valid_node(node) -> bool:
    global grid
    return node[0] >= 0 and node[0] < len(grid) and node[1] >= 0 and node[1] < len(grid[node[0]]) and grid[node[0]][node[1]] != '#'


def dfs(node):
    if node == end:
        return 0
    
    total = 0
    seen.add(node)
    for neighbor in graph[node]:
        if neighbor not in seen:
            total = max(total, dfs(neighbor) + graph[node][neighbor])
    seen.remove(node)
    
    return total



directions = {
    '.': [(-1, 0), (1, 0), (0, -1), (0, 1)],
    'v': [(1,0)],
    '^': [(-1, 0)],
    '<': [(0, -1)],
    '>': [(0, 1)]
}



grid = open('smol.txt').read().split('\n')
start = (0, grid[0].index('.'))
end = (len(grid) - 1, grid[-1].index("."))

nodes = [start, end]

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '#':
            continue
        neighbors = 0
        for new_node in [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]:
            if valid_node(new_node):
                neighbors += 1
        if neighbors > 2:
            nodes.append((i, j))

# ajacency list
graph = {p: {} for p in nodes}

# create edges
for node in nodes:
    # distance from node to node, node
    stack = [(0, node)]
    visited = {node}
    while stack:
        dist, curr = stack.pop()
        if dist > 0 and curr in nodes:
            graph[node][curr] = dist
            continue

        for direction in directions[grid[curr[0]][curr[1]]]:
            new_node = (curr[0] + direction[0], curr[1] + direction[1])
            if valid_node(new_node) and new_node not in visited:
                visited.add(new_node)
                stack.append((dist + 1, new_node))


seen = set()
print(dfs(start))

