import turtle

# COLORS:
# Here are the colors you have available to you:
# "red", "blue", "green"
# "yellow", "cyan", "magenta"
# "black", "white", "gray"
# "pink", "purple", "orange", "brown", "violet", "lightgreen", "lightblue", "gold"


# Setup the turtle screen
# Don't touch this setup
screen = turtle.Screen()
screen.title("Emoticon Maker")
screen.setup(width=600, height=600)

# x = 0, y = 0 is the center of the screen, 
# so the left is x = -300, the right is y = 300, 
# the top is y = 300, the bottom is y = -300
# Rectangles, Circles, and Triangles all have different ways they are drawn

def main():

    # ------------------------------------------ #
    # Your code will go here to draw your emoticon

    # set the background color
    set_background_color("darkviolet")

    # Body
    draw_circle(0, 0, 200, "orange")  # Pumpkin orange

    # Left Eye
    draw_triangle(-70, 60, -40, 110, -100, 110, "black")

    # Right Eye
    draw_triangle(70, 60, 40, 110, 100, 110, "black")

    # Nose
    draw_triangle(0, 30, -15, 10, 15, 10, "black")

    # Mouth
    draw_rectangle(-100, -100, 200, 30, "black")
    draw_triangle(-70, -120, -60, -100, -80, -100, "orange")  # Left tooth
    draw_triangle(70, -110, 80, -130, 60, -130, "orange")    # Right tooth

    # Stem
    draw_rectangle(-20, 240, 40, 60, "forestgreen")  # Forest green

    # ------------------------------------------ #

    # Keep the window open until clicked
    screen.exitonclick()


def set_background_color(color):
    """Set the background color of the canvas."""
    screen.bgcolor(color)

def draw_circle(x, y, radius, color):
    """Draw a circle with the given center, radius, and color."""
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.goto(x, y - radius)  # Adjust to draw from center
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

def draw_rectangle(x, y, width, height, color):
    """Draw a rectangle with the given top-left corner, width, height, and color."""
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(width)
        pen.right(90)
        pen.forward(height)
        pen.right(90)
    pen.end_fill()

def draw_triangle(x1, y1, x2, y2, x3, y3, color):
    """Draw a triangle using three vertices."""
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.goto(x1, y1)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    pen.goto(x2, y2)
    pen.goto(x3, y3)
    pen.goto(x1, y1)
    pen.end_fill()

if __name__ == "__main__":
    main()