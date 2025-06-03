#Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, math, time, random
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")
def set_image(sprite, image_filename):
	image_file = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
	screen = turtle.Screen()
	screen.register_shape(image_file)
	sprite.shape(image_file)
def create_sprite(image_filename, x=0, y=0):
	sprite = turtle.Turtle()
	set_image(sprite, image_filename)
	sprite.penup()
	sprite.goto(x,y)
	return sprite
def get_distance(s1, s2):
	dx = s1.xcor() - s2.xcor()
	dy = s1.ycor() - s2.ycor()
	return math.sqrt(dx*dx + dy*dy)
window = turtle.Screen()
window.tracer(0)

# Section 2: Setup
s1 = create_sprite ("corgi", -100,0)
set_background ("pond")
lives = 3  # Setting the starting value for the variable 'lives' 

# Section 3: Controls

def move_up():
    s1.setheading(90)
    s1.forward(10)
    
def move_down():
    s1.setheading(270)
    s1.forward(10)
    
def move_left():
    s1.setheading(180)
    s1.forward(10)
    
def move_right():
    s1.setheading(0)
    s1.forward(10)

window.onkeypress(move_up, "w") #shows that when the player presses w the character will move up
window.onkeypress(move_down, "s") #shows that when the player presses s the character will move down
window.onkeypress(move_left, "a") #shows that when the player presses a the character will move left
window.onkeypress(move_right, "d") #shows that when the player presses d the character will move right
s2 = create_sprite ("fox" ,-250, 0) 

# Section 4: Game Loop
window.listen()
timer = 0
while True:
	time.sleep(0.1)
	timer += 1  
	 
    
 
	movement = random.randint (-3, 4)
	s2.forward (movement)

	if get_distance (s1,s2) < 50:
		live -= 1




	window.update()

	if lives == 0:
		break
	

print("game over")
	