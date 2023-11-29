import math
import csv
import random

def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_angle(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.degrees(math.atan2(y2 - y1, x2 - x1))

def add_error_to_path(path, error_percentage):
    error_path = []
    for i in range(len(path)-1):
        point1 = path[i]
        point2 = path[i+1]
        distance = calculate_distance(point1, point2)
        error_distance = distance * (1 + error_percentage)
        angle = calculate_angle(point1, point2)
        error_point2 = (
            point1[0] + error_distance * math.cos(math.radians(angle)),
            point1[1] + error_distance * math.sin(math.radians(angle))
        )
        error_path.append(error_point2)
    return error_path

def save_path_to_csv(path, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['x', 'y'])  # Write header
        writer.writerows(path)

# Example usage
raw_path = [(0, 0), (1, 1), (2, 2), (3, 1), (4, 0)]

error_percentage = 0.05

error_path = add_error_to_path(raw_path, error_percentage)
save_path_to_csv(error_path, 'live_blind_location.csv')

print("Error path:", error_path)
print("test")