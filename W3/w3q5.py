from collections import deque
def is_valid(state):
    farmer, fox, chicken, grain = state
    # Fox and chicken 
    if fox == chicken and farmer != fox:
        return False
    # Chicken and grain 
    if chicken == grain and farmer != chicken:
        return False
    return True
def get_next_states(state):
    farmer, fox, chicken, grain = state
    next_states = []
    # Farmer alone
    new_state = (1 - farmer, fox, chicken, grain)
    if is_valid(new_state):
        next_states.append((new_state, "Farmer crosses alone"))
    # Farmer fox
    if farmer == fox:
        new_state = (1 - farmer, 1 - fox, chicken, grain)

        if is_valid(new_state):
            next_states.append((new_state, "Farmer takes Fox"))
    # Farmer chicken
    if farmer == chicken:
        new_state = (1 - farmer, fox, 1 - chicken, grain)
        if is_valid(new_state):
            next_states.append((new_state, "Farmer takes Chicken"))
    # Farmer  grain
    if farmer == grain:
        new_state = (1 - farmer, fox, chicken, 1 - grain)
        if is_valid(new_state):
            next_states.append((new_state, "Farmer takes Grain"))
    return next_states
def solve_river_crossing():
    start = (0, 0, 0, 0)
    goal = (1, 1, 1, 1)
    queue = deque([(start, [])])
    visited = {start}
    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        for next_state, action in get_next_states(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [action]))
    return None
solution = solve_river_crossing() 
print("Solution:")
for i, step in enumerate(solution, 1):
    print(i, ".", step)
