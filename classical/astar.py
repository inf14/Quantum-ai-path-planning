import numpy as np
import heapq
import random
import json

GRID_SIZE = 15
OBSTACLE_PROB = 0.25
NUM_RUNS = 30

START = (0, 0)
GOAL = (GRID_SIZE-1, GRID_SIZE-1)

random.seed(3)
np.random.seed(3)

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def neighbors(node, grid):
    x, y = node
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
            if grid[nx, ny] == 0:
                yield (nx, ny)

def a_star(grid, start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g = {start: 0}
    explored = []

    while open_set:
        _, current = heapq.heappop(open_set)
        explored.append(current)

        if current == goal:
            break

        for n in neighbors(current, grid):
            temp_g = g[current] + 1
            if n not in g or temp_g < g[n]:
                g[n] = temp_g
                f = temp_g + heuristic(n, goal)
                heapq.heappush(open_set, (f, n))
                came_from[n] = current

    path = []
    if goal in came_from:
        node = goal
        while node != start:
            path.append(node)
            node = came_from[node]
        path.append(start)
        path.reverse()

    return path, explored


# Experiment Loop
logs = []

for run in range(NUM_RUNS):
    grid = np.zeros((GRID_SIZE, GRID_SIZE))

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if random.random() < OBSTACLE_PROB:
                grid[i, j] = 1

    grid[START] = 0
    grid[GOAL] = 0

    path, explored = a_star(grid, START, GOAL)

    log_entry = {
        "run_id": run,
        "success": bool(path),
        "path_length": len(path)-1 if path else None,
        "explored_nodes": len(explored)
    }

    logs.append(log_entry)

with open("astar_logs.json", "w") as f:
    json.dump(logs, f, indent=2)

print("Experiment completed")
print("Successful runs:", sum(l["success"] for l in logs))
