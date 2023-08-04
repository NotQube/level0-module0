import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    chicken = turtle.Turtle()

    # Make your turtle's shape 'turtle', .shape('turtle')
    chicken.shape('turtle')

    # Set your turtle's speed using .speed(2)
    chicken.speed(2)

    # Set your turtle's color using .color('green') and .pencolor('blue')
    chicken.color('green')
    chicken.pencolor('blue')

    # Move your turtle forward using .forward(100)
    chicken.forward(100)
    # TEST    Did your turtle move forward?

    # Move your turtle left or right using .left(90) or .right(90)
    chicken.right(90)

    # Now put the forward and left/right code into a for loop to repeat 4 times.
    for i in range (4):
        chicken.forward(100)
        chicken.right(90)
    # TEST    Did your turtle draw a square?


    # Move your turtle to a new place on the screen using .goto(x, y)
    chicken.goto(100, 200)
    # x=0 and y=0 is the center of the screen



    # Have your turtle draw a circle using .circle(radius, steps=30)
    chicken.begin_fill()
    # TEST    Did your turtle draw a circle?
    chicken.circle(radius=30, steps=30)

    # Add color to your shape by adding .begin_fill() before drawing the circle
    chicken.end_fill()

    # and .end_fill() below
    chicken.goto(-100, 50)
    chicken.color('red')
    chicken.begin_fill()
    for i in range (4):
        chicken.forward(150)
        chicken.right(90)
    chicken.end_fill()

    chicken.goto(-25, 75)
    chicken.color('orange')
    chicken.begin_fill()
    for i in range (4):
        chicken.forward(30)
        chicken.right(90)
    chicken.end_fill()

    chicken.goto(175, 80)
    chicken.color('purple')
    chicken.begin_fill()
    chicken.circle(radius=30, steps=30)
    chicken.end_fill()







    # Draw 3 more shapes with different fill colors!

    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
