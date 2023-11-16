import math
import turtle
import csv

def draw_path(path, color):
    turtle.penup()
    turtle.goto(path[0])
    turtle.pendown()
    turtle.pencolor(color)
    for point in path:
        turtle.goto(point)

def read_path_from_csv(filename):
    path = []
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header
        for row in reader:
            x, y = map(float, row)
            path.append((x, y))
    return path

# Set up the turtle screen
screen = turtle.Screen()
screen.title("Path Visualization")
screen.setup(width=800, height=600)

# Create turtles for each path
raw_path_turtle = turtle.Turtle()
processed_path_turtle = turtle.Turtle()
live_path_turtle = turtle.Turtle()

# Adjust turtle settings
raw_path_turtle.speed(2)
processed_path_turtle.speed(2)
live_path_turtle.speed(2)

# Read paths from CSV files
raw_path = read_path_from_csv('raw_path.csv')
processed_path = read_path_from_csv('processed_path.csv')
live_blind_location = read_path_from_csv('live_blind_location.csv')

# Draw raw path
draw_path(raw_path, 'blue')

# Draw processed path
draw_path(processed_path, 'green')

# Draw live blind location path
draw_path(live_blind_location, 'red')

# Hide the turtles
raw_path_turtle.hideturtle()
processed_path_turtle.hideturtle()
live_path_turtle.hideturtle()

# Exit on click
turtle.exitonclick()