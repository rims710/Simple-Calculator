from tkinter import *

# Basic Functions
def click(val):
    entry.insert(END, str(val))

def clear():
    entry.delete(0, END)

def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, result)
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")

# Main Window
root = Tk()
root.title("Calculator")
root.config(bg="darkblue")   # dark background

# Entry box
entry = Entry(root, width=25, font=("Arial", 16), borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=15)

# Button style
btn_color = "violet"   # violet button color
btn_fg = "black"        # black text

def create_btn(text, r, c, cmd=None):
    return Button(root, text=text, width=8, height=2,
                  bg=btn_color, fg=btn_fg,
                  command=cmd if cmd else lambda: click(text)
                 ).grid(row=r, column=c, padx=5, pady=5)

# Creating buttons 
create_btn("1", 1, 0)
create_btn("2", 1, 1)
create_btn("3", 1, 2)

create_btn("4", 2, 0)
create_btn("5", 2, 1)
create_btn("6", 2, 2)

create_btn("7", 3, 0)
create_btn("8", 3, 1)
create_btn("9", 3, 2)

create_btn("0", 4, 1)

# Operators
create_btn("+", 5, 0)
create_btn("-", 5, 1)
create_btn("*", 5, 2)

create_btn("/", 6, 0)
create_btn("=", 6, 1, equal)
create_btn("Clear", 6, 2, clear)

root.mainloop()
