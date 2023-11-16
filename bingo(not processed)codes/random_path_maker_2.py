import random
import csv
import math

def generate_random_path(start_point, stop_point, num_points):
    path = [start_point]
    prev_point = start_point
    
    for _ in range(num_points - 1):
        angle = random.uniform(-math.pi/3, math.pi/3)  # Generate a random angle between -60 and 60 degrees
        distance = random.uniform(0.1, 1.0)  # Generate a random distance between 0.1 and 1.0 (adjust as needed)

        x = prev_point[0] + distance * math.cos(angle)
        y = prev_point[1] + distance * math.sin(angle)
        point = (x, y)
        path.append(point)
        prev_point = point

    return path

def save_path_to_csv(path, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['x', 'y'])  # Write header
        writer.writerows(path)

# Example usage
start_point = (0, 0)
stop_point = (1000, 1000)
num_points = 1000

random_path = generate_random_path(start_point, stop_point, num_points)
save_path_to_csv(random_path, 'random_path.csv')

print("Random path generated and saved to random_path.csv.")