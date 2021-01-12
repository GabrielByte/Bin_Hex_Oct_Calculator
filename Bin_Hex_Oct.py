'''
    This is a Binary, Hexadecimal, and Octal calculator.
    And what it basically does is get a decimal number
    and convert it to Bin, Hex, or Oct.
'''

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title = ("Calculator")
root.geometry = (500, 500)
root.config(bg = "black")

# Font sizes
lange_font = ("Arial",15)
small_font = ("Arial",10)

# Frame
frame = tk.Frame(root, width = 500, height = 400)
frame.grid(row = 1, column = 0)
top_frame = tk.Frame(root, width = 500, height = 100)
top_frame.grid(row = 0, column = 0)

# Input box
result = tk.StringVar()
entry = tk.Entry(top_frame, textvariable = result, width = 30, bg = "black", fg = "white", font = lange_font) 
entry.grid(row = 0, column = 0, ipady = 15)

# Functions
def button_click(number):
    current_number = result.get()
    entry.delete(0, "end")
    entry.insert(0, current_number+number)


def button_clear():
    entry.delete(0, "end")


def button_bin():
    current_number = int(result.get())
    entry.delete(0, "end")
    entry.insert(0, bin(current_number)[2:])


def button_hex():
    current_number = int(result.get())
    entry.delete(0, "end")
    entry.insert(0, hex(current_number)[2:])

def button_oct():
    current_number = int(result.get())
    entry.delete(0, "end")
    entry.insert(0, oct(current_number)[2:])


# Define operations buttons
button_oct = tk.Button(frame, text = "Oct", padx = 40, pady = 20, command = button_oct, bg = "orange", font = small_font)
button_oct.grid(row = 2, column = 3)
button_bin = tk.Button(frame, text = "Bin", padx = 41, pady = 20, command = button_bin, bg = "orange", font = small_font)
button_bin.grid(row = 3, column = 3)
button_hex = tk.Button(frame, text = "Hex", padx = 40, pady = 20, command = button_hex, bg = "orange", font = small_font)
button_hex.grid(row = 4, column = 3)
button_clear = tk.Button(frame, text = "C", padx = 46, pady = 20, command = button_clear, bg = "orange", font = small_font)
button_clear.grid(row = 5, column = 3)

# Define numbers buttons
button_0 = tk.Button(frame, text = "0", padx = 40, pady = 20, command = lambda: button_click("0"))
button_0.grid(row = 5, column = 0, columnspan = 3)
button_1 = tk.Button(frame, text = "1", padx = 40, pady = 20, command = lambda: button_click("1"))
button_1.grid(row = 4, column = 0)
button_2 = tk.Button(frame, text = "2", padx = 40, pady = 20, command = lambda: button_click("2"))
button_2.grid(row = 4, column = 1)
button_3 = tk.Button(frame, text = "3", padx = 40, pady = 20, command = lambda: button_click("3"))
button_3.grid(row = 4, column = 2)
button_4 = tk.Button(frame, text = "4", padx = 40, pady = 20, command = lambda: button_click("4"))
button_4.grid(row = 3, column = 0)
button_5 = tk.Button(frame, text = "5", padx = 40, pady = 20, command = lambda: button_click("5"))
button_5.grid(row = 3, column = 1)
button_6 = tk.Button(frame, text = "6", padx = 40, pady = 20, command = lambda: button_click("6"))
button_6.grid(row = 3, column = 2)
button_7 = tk.Button(frame, text = "7", padx = 40, pady = 20, command = lambda: button_click("7"))
button_7.grid(row = 2, column = 0)
button_8 = tk.Button(frame, text = "8", padx = 40, pady = 20, command = lambda: button_click("8"))
button_8.grid(row = 2, column = 1)
button_9 = tk.Button(frame, text = "9", padx = 40, pady = 20, command = lambda: button_click("9"))
button_9.grid(row = 2, column = 2)

root.mainloop()
