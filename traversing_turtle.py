import turtle as trtl

class TurtleSpiral:
    def __init__(self, shapes, colors):
        # Data structure to store turtles and colors
        self.my_turtles = []
        self.turtle_shapes = shapes
        self.turtle_colors = colors
        
        # Initialize the turtles with shapes and colors
        for shape in self.turtle_shapes:
            t = trtl.Turtle(shape=shape)
            
            # Pop the last color from the list and apply it to the turtle
            new_color = self.turtle_colors.pop()
            t.fillcolor(new_color)
            t.pencolor(new_color)

            # Add the turtle to the list
            t.penup()  # Pen up initially
            self.my_turtles.append(t)
    
    def draw_spiral(self, angle_increment=45, step_increment=10):
        """ Public method to iterate through turtles and draw the expanding spiral """
        startx = 0
        starty = 0
        direction = 90  # Initial direction
        step = 50  # Initial step length
        
        # Loop through each turtle and make it draw part of the expanding spiral
        for t in self.my_turtles:
            t.goto(startx, starty)
            t.setheading(direction)
            t.pendown()
            t.forward(step)
            
            # Update starting position and direction
            startx = t.xcor()
            starty = t.ycor()
            direction += angle_increment

            # Increase the step size for the next turtle to make the spiral expand
            step += step_increment

    

# Example usage:
if __name__ == "__main__":
    # Define the shapes and colors for the turtles, duplicating them to create more turtles
    turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"] * 2  # Double the shapes
    turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"] * 2  # Double the colors

    # Create an instance of TurtleSpiral
    turtle_spiral = TurtleSpiral(turtle_shapes, turtle_colors)

    # Draw the expanding spiral
    turtle_spiral.draw_spiral(angle_increment=45, step_increment=10)

    # Print information about the turtles
    print(turtle_spiral)

    # Keep the window open
    wn = trtl.Screen()
    wn.mainloop()
