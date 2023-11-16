import math
import random
import csv

def generate_path(start_point, end_point, num_points):
    x1, y1 = start_point
    x2, y2 = end_point
    
    # Calculate the angle between the two points
    angle = math.atan2(y2 - y1, x2 - x1)
    
    # Calculate the distance between the two points
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    # Calculate the step size based on the number of points
    step_size = distance / (num_points - 1)
    
    path = [start_point]
    
    for _ in range(num_points - 2):
        # Generate a random angle within the range of -40 to 40 degrees
        random_angle = math.radians(random.uniform(-40, 40))
        
        # Calculate the new point based on the random angle and step size
        new_x = path[-1][0] + math.cos(angle + random_angle) * step_size
        new_y = path[-1][1] + math.sin(angle + random_angle) * step_size
        
        path.append((new_x, new_y))
    
    path.append(end_point)
    
    return path

# Example usage
start_point = (0, 0)
end_point = (188, 210)
num_points = 100

random_path = generate_path(start_point, end_point, num_points)

# Save the random path to a CSV file
with open('r_path.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['x', 'y'])  # Write header
    writer.writerows(random_path)

print("Random path saved to r_path.csv")