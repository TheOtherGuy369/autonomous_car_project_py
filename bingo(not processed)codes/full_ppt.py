import math
import csv
import matplotlib.pyplot as plt

def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_angle(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.degrees(math.atan2(y2 - y1, x2 - x1))

def calculate_time(distance, wheel_periphery, motor_rpm):
    wheel_circumference = 2 * math.pi * wheel_periphery
    linear_speed = wheel_circumference * motor_rpm / 60  # in cm/s
    time = distance / linear_speed  # in seconds
    return time

def smooth_path(raw_path):
    smoothed_path = []
    prev_point = raw_path[0]
    smoothed_path.append(prev_point)

    for i in range(1, len(raw_path)-1):
        current_point = raw_path[i]
        next_point = raw_path[i+1]

        angle1 = calculate_angle(prev_point, current_point)
        angle2 = calculate_angle(current_point, next_point)

        if abs(angle2 - angle1) <= 40:
            smoothed_path.append(current_point)

        prev_point = current_point

    smoothed_path.append(raw_path[-1])

    return smoothed_path

def adjust_turns(path, car_width):
    adjusted_path = []
    adjusted_path.append(path[0])

    for i in range(1, len(path)-1):
        prev_point = path[i-1]
        current_point = path[i]
        next_point = path[i+1]

        angle1 = calculate_angle(prev_point, current_point)
        angle2 = calculate_angle(current_point, next_point)

        if abs(angle2 - angle1) > 40:
            adjusted_path.append((current_point[0] - car_width/2, current_point[1] - car_width/2))
            adjusted_path.append((current_point[0] + car_width/2, current_point[1] + car_width/2))
            adjusted_path.append(current_point)

    adjusted_path.append(path[-1])

    return adjusted_path

def process_path(raw_path, car_width):
    smoothed_path = smooth_path(raw_path)
    adjusted_path = adjust_turns(smoothed_path, car_width)
    return adjusted_path

def save_path_to_csv(path, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['x', 'y'])  # Write header
        writer.writerows(path)

def plot_path(path, label):
    x = [point[0] for point in path]
    y = [point[1] for point in path]
    plt.plot(x, y, label=label)

# Example usage
raw_path = []

with open('random_path.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header row
    for row in reader:
        x, y = map(float, row)
        raw_path.append((x, y))

car_width = 0.5  # 50 cm
motor_rpm = 1500
wheel_periphery = 4

processed_path = process_path(raw_path, car_width)
save_path_to_csv(processed_path, 'processed_path.csv')

# Calculate time between each point and total time
total_time = 0
times = []
for i in range(len(processed_path)-1):
    point1 = processed_path[i]
    point2 = processed_path[i+1]
    distance = calculate_distance(point1, point2)
    time = calculate_time(distance, wheel_periphery, motor_rpm)
    total_time += time
    times.append(time)

# Plot raw_path and processed_path
plot_path(raw_path, label='Raw Path')
plot_path(processed_path, label='Processed Path')

# Set plot labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Raw Path vs Processed Path')
plt.legend()

# Display the plot
plt.show()

print("Total time:", total_time)
print("Times between each point:", times)