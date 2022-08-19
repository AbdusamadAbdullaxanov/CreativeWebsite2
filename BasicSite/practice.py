"""
to make it more realistic

file_action = ttk.Menubutton(task_frame, text=tab + "File", width=10)
file_action.menu = Menu()
file_action.menu.insert_cascade(index=0)
file_action.pack(side=LEFT)
edit_action = ttk.Menubutton(task_frame, text=tab + "Edit", width=10)
edit_action.pack(side=LEFT)
view_action = ttk.Menubutton(task_frame, text=tab + "View", width=10)
view_action.pack(side=LEFT)
"""

import os
from tkinter import *
from tkinter import (
    ttk,
    messagebox,
    filedialog
)

window_name: str = "unnamed file"
tab = chr(32) * 8
LIGHT_COLORS = ["#9C9C9C"]  # index 0 for menu, 1  for textbox
DARK_COLORS = ["#141431", "white"]  # index 0 for menu, 1 for foreground color, 2 textbox color


def run_script():
    with open("file.py", "w") as file:
        file.write(main_textbox.get("1.0", END))
    os.system('cmd /c "python -m file.py"')


def themes(textbox: str, foreground: str = "black"):
    main_textbox.config(bg=textbox, fg=foreground)


window = Tk()
window.title(window_name)
window.geometry("1000x600")
window.minsize(700, 400)

task_frame = Frame(window)
task_frame.pack(fill=X)
radio1 = ttk.Radiobutton(task_frame, text="Light theme", command=lambda: themes(LIGHT_COLORS[0]))
radio1.pack(side=RIGHT)
radio1 = ttk.Radiobutton(
    task_frame, text="Dark theme", command=lambda: themes(DARK_COLORS[0], DARK_COLORS[1])
)
radio1.pack(side=RIGHT)
run_button = ttk.Button(task_frame, text="▶", command=run_script)
run_button.pack(side=RIGHT)
main_textbox = Text(height=726)
main_textbox.bind(")", lambda event: main_textbox.insert(END, "("))
main_textbox.pack(fill=BOTH)

window.mainloop()
