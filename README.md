# Calculator

#Introduction
This is a simple calculator program that has been created using Python's GUI library, tkinter. The program includes a display area, where the user's input is displayed, and a set of buttons for performing various arithmetic operations. The buttons included in the calculator are numbers from 0 to 9, arithmetic operations such as addition, subtraction, multiplication, and division, a clear button for clearing the display, and an equal button for evaluating the input.

#Code Explanation
The program starts by importing the tkinter library and creating a tkinter window, also known as the root window. A StringVar object, called "input_text", is then created, which will store the user's input. A display area is created using the tkinter Entry widget, which is configured with a font, background color, and a width, among other properties.

For each button in the calculator, a tkinter button widget is created, configured with text, font, color, and size, among other properties. When a button is clicked, it calls a function "btnClick" with the button's value as a parameter. The "btnClick" function appends the value of the button to the input_text variable. The clear button, when clicked, calls the "btnClearDisplay" function, which sets the input_text variable to an empty string. The equal button, when clicked, calls the "btnEqualsInput" function, which evaluates the input stored in the input_text variable as a mathematical expression and displays the result in the display area.
