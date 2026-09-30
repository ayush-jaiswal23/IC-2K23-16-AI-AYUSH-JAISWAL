import random

def objective_function(x):
    """Function to maximize: f(x) = -(x - 3)^2 + 10"""
    return -(x - 3)**2 + 10

def get_neighbors(x, step_size=0.1):
    """Generate left and right adjacent neighbors."""
    return [x - step_size, x + step_size]

def hill_climbing(objective_func, start_x, step_size=0.1, max_iterations=1000):
    current_x = start_x
    current_score = objective_func(current_x)
    
    for _ in range(max_iterations):
        neighbors = get_neighbors(current_x, step_size)
        best_neighbor = None
        best_neighbor_score = float('-inf')
        
        # Evaluate all neighbors to find the best one
        for neighbor in neighbors:
            score = objective_func(neighbor)
            if score > best_neighbor_score:
                best_neighbor_score = score
                best_neighbor = neighbor
        
        # Stop if no neighbor improves the current score (Local Optimum)
        if best_neighbor_score <= current_score:
            break
            
        # Move to the better neighbor
        current_x = best_neighbor
        current_score = best_neighbor_score
        
    return current_x, current_score

def random_restart_hill_climbing(objective_func, restarts=20, search_bounds=(-10, 10)):
    global_best_x = None
    global_best_score = float('-inf')
    
    for i in range(restarts):
        start_x = random.uniform(*search_bounds)
        best_x, best_score = hill_climbing(objective_func, start_x=start_x)
        
        if best_score > global_best_score:
            global_best_score = best_score
            global_best_x = best_x
            
    return global_best_x, global_best_score

# --- Run Example ---
opt_x, opt_score = random_restart_hill_climbing(objective_function, restarts=10)

print("\nRandom-Restart Results: ")
print(f"Best Overall Point: x = {opt_x:.4f}")
print(f"Best Overall Value: f(x) = {opt_score:.4f}")