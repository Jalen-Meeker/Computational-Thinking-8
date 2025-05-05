import turtle, time, random

# Section 1 - Helper functions
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
x1 = -200
y1 = 200
X2 = 200
y2 = -200
# Section 3 - Setup
set_background("castle")
t1 = create_sprite("baseball",x1,y1)
t2 = create_sprite("bat",x2,y2)
# Section 4 - movement
for i in range(30):
	y1 -= 10
	y2 -= 10

   
   t1.goto(x1, y1)      
    time.sleep(0.5)
    t2.goto(x2, y2) 
    time.sleep(1.0)


turtle.exitonclick()
