import tkinter as tk

buttons = [
    ["x", "AC", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["+/-", "0", ".", "="],
]

top_buttons = ["x", "AC", "%"]
right_buttons = ["/", "*", "-", "+", "="]

button_rows = len(buttons)
button_columns = len(buttons[0])

black_colour = "#1C1C1C"
white_colour = "#FFFFFF"
light_grey_colour = "#D4D4D2"
dark_grey_colour = "#505050"

window = tk.Tk()
window.title("Calculator")
window.resizable(False, False)
window.configure(background=black_colour)

window_width = 300
display_height = 130
buttons_height = 300

frame = tk.Frame(
    window,
    background=black_colour,
    width=window_width,
    height=display_height + buttons_height
)

frame.grid_propagate(False)
frame.pack_propagate(False)

display_frame = tk.Frame(
    frame,
    background=black_colour,
    width=window_width,
    height=display_height
)

display_frame.pack(
    side="top",
    fill="x"
)

display_frame.pack_propagate(False)

label = tk.Label(
    display_frame,
    text="0",
    font=("Arial", 44),
    background=black_colour,
    foreground=white_colour,
    anchor="e",
)

label.pack(
    fill="both",
    expand=True,
    padx=(0, 14)
)

buttons_frame = tk.Frame(
    frame,
    background=black_colour,
    width=window_width,
    height=buttons_height
)

buttons_frame.pack(
    side="top",
    fill="both",
    expand=True
)

buttons_frame.pack_propagate(False)

for row in range(button_rows):
    buttons_frame.grid_rowconfigure(
        row,
        weight=1
    )

for column in range(button_columns):
    buttons_frame.grid_columnconfigure(
        column,
        weight=1
    )

def set_display(text):
    text = str(text)
    length = len(text)

    if length <= 7:
        size = 40
    elif length <= 10:
        size = 30
    elif length <= 13:
        size = 20
    else:
        size = 20

    label.config(
        text=text,
        font=("Arial", size)
    )

A = "0"
operator = None
B = None

def clear_all():
    global A, B, operator

    A = "0"
    operator = None
    B = None

def remove_zero_decimal(num):
    if num % 1 == 0:
        return str(int(num))

    return f"{num:.10g}"

def backspace(event=None):
    text = label["text"]

    if len(text) > 1:
        set_display(text[:-1])
    else:
        set_display("0")

def button_clicked(number):
    global A, B, operator

    if number == "=":
        if A is not None and operator is not None:
            B = label["text"]

            numA = float(A)
            numB = float(B)

            if operator == "+":
                set_display(
                    remove_zero_decimal(numA + numB)
                )

            elif operator == "-":
                set_display(
                    remove_zero_decimal(numA - numB)
                )

            elif operator == "*":
                set_display(
                    remove_zero_decimal(numA * numB)
                )

            elif operator == "/":
                set_display(
                    remove_zero_decimal(numA / numB)
                )

            clear_all()

    elif number in "+-*/":
        A = label["text"]
        set_display("0")
        operator = number

    elif number == "AC":
        clear_all()
        set_display("0")

    elif number == "+/-":
        result = float(label["text"]) * -1

        set_display(
            remove_zero_decimal(result)
        )

    elif number == "%":
        result = float(label["text"]) / 100

        set_display(
            remove_zero_decimal(result)
        )

    elif number == "x":
        backspace()

    else:
        if number == ".":
            if number not in label["text"]:
                set_display(
                    label["text"] + number
                )

        elif number in "0123456789":
            if label["text"] == "0":
                set_display(number)
            else:
                set_display(
                    label["text"] + number
                )

for row in range(button_rows):
    for column in range(button_columns):
        value = buttons[row][column]

        if value in top_buttons:
            fg, bg = white_colour, light_grey_colour

        elif value in right_buttons:
            fg, bg = white_colour, light_grey_colour

        else:
            fg, bg = white_colour, dark_grey_colour

        button = tk.Label(
            buttons_frame,
            text=value,
            font=("Arial", 20),
            foreground=fg,
            background=bg,
            cursor="arrow"
        )

        button.grid(
            row=row,
            column=column,
            sticky="nsew",
            padx=1,
            pady=1
        )

        button.bind(
            "<Button-1>",
            lambda event, value=value:
                button_clicked(value)
        )

frame.pack(
    fill="both",
    expand=True
)

window.mainloop()