import tkinter as tk
from sample3 import load_calculation1
from sample4 import load_calculation2

def clear_frame(frame):
    """Clear all widgets in the frame."""
    for widget in frame.winfo_children():
        widget.destroy()

def switch_to_calculation1():
    clear_frame(main_frame)
    load_calculation1(main_frame)

def switch_to_calculation2():
    clear_frame(main_frame)
    load_calculation2(main_frame)

# Main application
app = tk.Tk()
app.geometry("600x400")

# Create a reusable frame
main_frame = tk.Frame(app, height=300, width=500, bg="lightgrey")
main_frame.pack(pady=20)

# Buttons to switch between functionalities
btn1 = tk.Button(app, text="Calculation 1", command=switch_to_calculation1)
btn1.pack(side=tk.LEFT, padx=10)

btn2 = tk.Button(app, text="Calculation 2", command=switch_to_calculation2)
btn2.pack(side=tk.RIGHT, padx=10)

app.mainloop()
