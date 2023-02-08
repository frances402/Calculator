import tkinter as tk


def evaluateExpression(expression):
    try:
        result = eval(expression)
        return result
    except:
        return "Error"


def buttonClick(numbers):
    global expression
    expression = expression + str(numbers)
    input_text.set(expression)


def buttonClearDisplay():
    global expression
    expression = ""
    input_text.set("")


def buttonEqualsInput():
    global expression
    result = evaluateExpression(expression)
    input_text.set(result)
    expression = ""


expression = ""

root = tk.Tk()
root.geometry("350x300")
root.title("Calculator")

input_text = tk.StringVar()

tk.Entry(root, font=('Helvetica', 14), textvariable=input_text, width=25, bd=5, bg="powder blue").pack()

row1 = tk.Frame(root)
row1.pack(side=tk.TOP, padx=5, pady=5)
# button 7
tk.Button(row1, text="7", fg="black", bg="red", font=('Helvetica', 14), height=2, width=7,
          command=lambda: buttonClick(7)).pack(side=tk.LEFT)
# button 8
tk.Button(row1, text="8", fg="black", bg="red", font=('Helvetica', 14), height=2, width=7,
          command=lambda: buttonClick(8)).pack(side=tk.LEFT)
# button 9
tk.Button(row1, text="9", fg="black", bg="red", font=('Helvetica', 14), height=2, width=7,
          command=lambda: buttonClick(9)).pack(side=tk.LEFT)
# button + (addition)
tk.Button(row1, text="+", fg="black", bg="red", font=('Helvetica', 14), height=2, width=7,
          command=lambda: buttonClick("+")).pack(side=tk.LEFT)

row2 = tk.Frame(root)
row2.pack(side=tk.TOP, padx=5, pady=5)
# button 4
tk.Button(row2, text="4", fg="black", bg="red", font=('Helvetica', 14), height=2, width=7,
          command=lambda: buttonClick(4)).pack(side=tk.LEFT)
# button 5
tk.Button(row2, text="5", fg="black", bg="red", font=('Helvetica', 14), height=2, width=7,
          command=lambda: buttonClick(5)).pack(side=tk.LEFT)
# button 6
tk.Button(row2, text="6", fg="black", bg="red", font=('Helvetica', 14), height=2, width=7,
          command=lambda: buttonClick(6)).pack(side=tk.LEFT)
# button - (subtraction)
tk.Button(row2, text="-", fg="black", bg="red", font=('Helvetica', 14), height=2, width=7,
          command=lambda: buttonClick("-")).pack(side=tk.LEFT)

row3 = tk.Frame(root)
row3.pack(side=tk.TOP, padx=5, pady=5)
# button 1
tk.Button(row3, text="1", fg="black", bg="red", font=('Helvetica', 14), height=2, width=7,
          command=lambda: buttonClick(1)).pack(side=tk.LEFT)
# button 2
tk.Button(row3, text="2", fg="black", bg="red", font=('Helvetica', 14), height=2, width=7,
          command=lambda: buttonClick(2)).pack(side=tk.LEFT)
# button 3
tk.Button(row3, text="3", fg="black", bg="red", font=('Helvetica', 14), height=2, width=7,
          command=lambda: buttonClick(3)).pack(side=tk.LEFT)
# button x (multiplication)
tk.Button(row3, text="x", fg="black", bg="red", font=('Helvetica', 14), height=2, width=7,
          command=lambda: buttonClick("*")).pack(side=tk.LEFT)

row4 = tk.Frame(root)
row4.pack(side=tk.TOP, padx=5, pady=5)
# button C (clear)
tk.Button(row4, text="C", fg="black", bg="red", font=('Helvetica', 14), height=2, width=7,
          command=buttonClearDisplay).pack(side=tk.LEFT)
# button 0
tk.Button(row4, text="0", fg="black", bg="red", font=('Helvetica', 14), height=2, width=7,
          command=lambda: buttonClick(0)).pack(side=tk.LEFT)
# button = (equal)
tk.Button(row4, text="=", fg="black", bg="red", font=('Helvetica', 14), height=2, width=7,
          command=buttonEqualsInput).pack(
    side=tk.LEFT)
# button / (division)
tk.Button(row4, text="/", fg="black", bg="red", font=('Helvetica', 14), height=2, width=7,
          command=lambda: buttonClick("/")).pack(side=tk.LEFT)

root.mainloop()
