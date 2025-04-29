#Curves Recursion project

##Introduction
 using only basic operators and simple functions learned in class. 

##description of the code 
This Python code utilises the Turtle module to draw fractal curves known as "dragon curves." Here's a breakdown of the code:
Importing Libraries: The code imports the turtle module as t and the random module. It also imports the sqrt function from the math module.
Defining the tri_curve Functions: Two functions are defined:
The first tri_curve function appears to draw a specific pattern of lines without recursion. It is followed by another tri_curve function that actually implements recursion to draw the dragon curve.
The tri_curve function with recursion takes two parameters: depth and dist. It draws the dragon curve recursively based on the specified depth and initial distance.
Defining tri_curve_reverse Function: This function is similar to the tri_curve function but draws the dragon curve in reverse, from right to left.
Setting Up Initial Drawing Position: The turtle is positioned at the initial drawing position to start drawing the fractal curves.
Drawing the Dragon Curve with Recursion: The tri_curve function with recursion is called to draw the dragon curve. The depth parameter determines the level of recursion, and the dist parameter determines the initial distance of the line segments.
Drawing the Dragon Curve Backwards: After drawing the dragon curve forwards, the turtle's position is reset, and the tri_curve_reverse function is called to draw the dragon curve in reverse.
Overall, the code demonstrates how to use recursion to draw fractal curves and provides an example of drawing a dragon curve and its reverse using Turtle graphics.

##challenges
One key challenge was debugging Recursive Functions; Debugging recursive functions can be challenging because they can involve multiple levels of recursion. Understanding how to trace the execution of recursive calls and identify potential issues, such as infinite recursion or incorrect base cases, is essential for debugging.Another possible challenge may be visualising the Fractal Curve; visualising the fractal curve as it is being drawn can be challenging, especially for complex shapes or when debugging recursive functions. Using visualisation tools or techniques to help understand the recursive process and the resulting curve can be beneficial.

##improvement
One possible improvement that could be made in the code is to enhance its flexibility by introducing parameters for angle and scale. By allowing the user to customise these parameters, the code becomes more versatile and can generate a wider range of fractal curves with different shapes and sizes. Additionally, incorporating error handling mechanisms to handle invalid input values can make the code more robust and user-friendly. This would ensure that the program gracefully handles unexpected input and provides informative error messages to the user, enhancing the overall user experience.