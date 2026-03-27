import numpy as np
import random

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator


# PARAMETERS
GRID_SIZE = 10
START = (0,0)
GOAL = (GRID_SIZE-1, GRID_SIZE-1)

simulator = AerSimulator()


# GROVER-INSPIRED CIRCUIT
def grover_direction():

    qc = QuantumCircuit(2,2)

    qc.h([0,1])
    qc.cz(0,1)

    qc.h([0,1])
    qc.x([0,1])
    qc.cz(0,1)
    qc.x([0,1])
    qc.h([0,1])

    qc.measure([0,1],[0,1])

    compiled = transpile(qc, simulator)
    job = simulator.run(compiled, shots=64)

    result = job.result()
    counts = result.get_counts()

    return max(counts, key=counts.get)


# QUANTUM MOVE
def quantum_move(current, grid, goal):

    x, y = current
    moves = [(-1,0),(1,0),(0,-1),(0,1)]

    valid_moves = []

    for dx,dy in moves:
        nx, ny = x + dx, y + dy

        if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
            if grid[nx,ny] == 0:
                dist = abs(nx - goal[0]) + abs(ny - goal[1])
                valid_moves.append((dist,(dx,dy)))

    if not valid_moves:
        return None

    valid_moves.sort()
    best_dist = valid_moves[0][0]

    candidates = [m for d,m in valid_moves if d == best_dist]

    if len(candidates) == 1:
        return candidates[0]

    direction = grover_direction()

    move_map = {
        "00": candidates[0],
        "01": candidates[0],
        "10": candidates[-1],
        "11": candidates[-1]
    }

    return move_map[direction]


# PATH PLANNER
def quantum_path(grid,start,goal):

    current = start
    path = [current]
    explored = []

    visited = set([current])
    steps = 0

    while current != goal and steps < GRID_SIZE * GRID_SIZE:

        explored.append(current)

        move = quantum_move(current, grid, goal)

        if move is None:
            break

        dx,dy = move
        next_node = (current[0]+dx, current[1]+dy)

        if next_node in visited:
            steps += 1
            continue

        visited.add(next_node)
        current = next_node
        path.append(current)

        steps += 1

    if current != goal:
        return [], explored

    return path, explored
