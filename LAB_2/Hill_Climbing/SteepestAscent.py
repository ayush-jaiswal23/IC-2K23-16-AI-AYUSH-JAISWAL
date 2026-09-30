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

random_start = random.uniform(-10, 10)
best_x, best_score = hill_climbing(objective_function, start_x=random_start)

print(f"Starting Point: x = {random_start:.4f}")
print(f"Optimal Point Found: x = {best_x:.4f}")
print(f"Maximum Value Found: f(x) = {best_score:.4f}")