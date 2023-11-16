import math
import csv

def save_path_to_csv(path):
    with open('path.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['x', 'y'])
        writer.writerows(path)
    print("Path saved to path.csv")

def generate_s_shape(num_points):
    path = []
    angle_increment = math.radians(40)
    radius = 100
    center_x = 300
    center_y = 300

    for i in range(num_points):
        angle = i * angle_increment
        x = center_x + radius * math.sin(angle)
        y = center_y + radius * math.cos(angle)
        path.append([x, y])

    return path

# Generate the S-shaped path
path = generate_s_shape(1000)

# Save the path to a CSV file
save_path_to_csv(path)
