# Section 1 - Helper functions
import turtle, time, random
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")
def create_sprite(image_filename, x=0, y=0):
	image_file = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
	screen = turtle.Screen()
	screen.register_shape(image_file)
	sprite = turtle.Turtle()
	sprite.shape(image_file)
	sprite.penup()
	sprite.goto(x,y)
	return sprite


# Section 2 - Variables
# TODO - add starting values for all the variables
x1 =0
y1 =100
x2 =0
y2 =80
x3 =0
y3 =60
x4 =0
y4 =40
# Section 3 - Setup
# TODO - use your own background, and set your four turtles to images of your choice
set_background("castle")
t1 = create_sprite("baseball",x1,y1)
t2 = create_sprite("basketball",x2,y2)
t3 = create_sprite("fish",x3,y3)
t4 = create_sprite("flower",x4,y4)


# Section 4 - Racing
# TODO - set how much each variable changes by and increase the number of repeats to at least 30
# TODO - explain here which sprites are faster or slower

# Let's assume the speeds of each player are different.
speed1 = 5  # Player 1's speed
speed2 = 4  # Player 2's speed
speed3 = 3  # Player 3's speed
speed4 = 2  # Player 4's speed

# We will use these initial positions for the players
x1, x2, x3, x4 = 0, 0, 0, 0
y1, y2, y3, y4 = 100, 90, 80, 70  # y-coordinates for each player

# Assuming t1, t2, t3, t4 are the turtle objects representing the players
# Example: t1 = turtle.Turtle(), and similar for t2, t3, t4

# Run the race for at least 30 iterations
for i in range(30):  # Increased the number of repeats to 30
    x1 += speed1
    x2 += speed2
    x3 += speed3
    x4 += speed4
    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)
    time.sleep(0.1)  # Sleep to slow down the movement for visual effect

# Section 5 - Winner
# TODO - complete the elif for player 2 winning
# TODO - write another elif for player 3 and player 4

if x1 >= 1000:  # Assuming 1000 is the finish line position
    print("Player 1 wins!")
elif x2 >= 1000:
    print("Player 2 wins!")
elif x3 >= 1000:
    print("Player 3 wins!")
elif x4 >= 1000:
    print("Player 4 wins!")
else:
    print("No winner yet.")