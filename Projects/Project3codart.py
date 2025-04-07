import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle object
artist = turtle.Turtle()
artist.speed(0)  # Fastest drawing speed

colors = ["cyan", "magenta"]  # Two different colors used in the pattern

# Outer loop to draw multiple stars in a circular pattern
for i in range(36):
    artist.color(colors[i % 2])  # Alternate colors between cyan and magenta

    # Inner loop to draw a star
    for j in range(5):  # Draw a 5-point star
        artist.forward(100)
        artist.right(144)

    artist.right(10)  # Rotate to start the next star

# Hide the turtle and keep the window open
artist.hideturtle()
screen.mainloop() 