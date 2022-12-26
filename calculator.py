import tkinter as tk

calculation = ""

lastEquals = False

def mark_equals():
    global lastEquals
    lastEquals = True


def add_to_calculation(symbol):
    global calculation
    global lastEquals

    if lastEquals:
        clear_field()

    # Add to the calculation the given symbol as a string 
    calculation += str(symbol)

    # Delete what's on the current display so it can display the next variable
    text_result.delete(1.0, "end")

    # Add to the display the selected variable
    text_result.insert(1.0, calculation)

    lastEquals = False

def add_to_calculation_op(symbol):
    global calculation
    global lastEquals

    # Add to the calculation the given symbol as a string 
    calculation += str(symbol)

    # Delete what's on the current display so it can display the next variable
    text_result.delete(1.0, "end")

    # Add to the display the selected variable
    text_result.insert(1.0, calculation)
    lastEquals = False

def evaluate_calculation():
    global calculation
    global lastEquals
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
    
    lastEquals = True
        

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


# Object creation
root = tk.Tk()

root.geometry("300x275")

# Result Page
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))

# Creating the grid since it will span 5 also to make sure result spans across all 5
text_result.grid(columnspan = 5)

# lambda will refer to function (do this if that rather than directly call)
btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 14))
btn_1.grid(row=2, column=1)

btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial", 14))
btn_2.grid(row=2, column=2)

btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial", 14))
btn_3.grid(row=2, column=3)

btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial", 14))
btn_4.grid(row=3, column=1)

btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial", 14))
btn_5.grid(row=3, column=2)

btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 14))
btn_6.grid(row=3, column=3)

btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial", 14))
btn_7.grid(row=4, column=1)

btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial", 14))
btn_8.grid(row=4, column=2)

btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial", 14))
btn_9.grid(row=4, column=3)

btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial", 14))
btn_0.grid(row=5, column=2)

btn_dec = tk.Button(root, text=".", command=lambda: add_to_calculation_op("."), width=5, font=("Arial", 14))
btn_dec.grid(row=5, column=1)

btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation_op("+"), width=5, font=("Arial", 14))
btn_plus.grid(row=5, column=3)

btn_div = tk.Button(root, text="/", command=lambda: add_to_calculation_op("/"), width=5, font=("Arial", 14))
btn_div.grid(row=2, column=4)

btn_mul = tk.Button(root, text="*", command=lambda: add_to_calculation_op("*"), width=5, font=("Arial", 14))
btn_mul.grid(row=3, column=4)

btn_sub = tk.Button(root, text="-", command=lambda: add_to_calculation_op("-"), width=5, font=("Arial", 14))
btn_sub.grid(row=4, column=4)

btn_eq = tk.Button(root, text="=", command=lambda: (evaluate_calculation(), mark_equals()), width=5, height=3, font=("Arial", 14))
btn_eq.grid(row=5, column=4, rowspan=2)

btn_left = tk.Button(root, text="(", command=lambda: add_to_calculation_op("("), width=5, font=("Arial", 14))
btn_left.grid(row=6, column=1)

btn_right = tk.Button(root, text=")", command=lambda: add_to_calculation_op(")"), width=5, font=("Arial", 14))
btn_right.grid(row=6, column=2)

btn_c = tk.Button(root, text="C", command=lambda: clear_field(), width=5, font=("Arial", 14))
btn_c.grid(row=6, column=3)

# Running the main loop
root.mainloop()