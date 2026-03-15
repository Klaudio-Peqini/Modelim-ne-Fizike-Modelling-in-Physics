
import numpy as np

def simulate_traffic(num_cells=100, density=0.2, steps=100):

    road = -np.ones(num_cells, dtype=int)
    num_cars = int(num_cells * density)
    positions = np.random.choice(num_cells, num_cars, replace=False)
    road[positions] = 0

    history = []

    for _ in range(steps):
        new_road = -np.ones(num_cells, dtype=int)
        for i in range(num_cells):
            if road[i] >= 0:
                new_pos = (i + 1) % num_cells
                if road[new_pos] == -1:
                    new_road[new_pos] = 0
                else:
                    new_road[i] = 0
        road = new_road
        history.append(road.copy())

    return np.array(history)
