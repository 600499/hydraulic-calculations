import tkinter as tk

def load_calculation2(frame):
    """Load widgets for Calculation 2 in the given frame."""
    label = tk.Label(frame, text="Calculation 2", font=("Arial", 16))
    label.pack(pady=10)

    entry1 = tk.Entry(frame, width=15)
    entry1.pack(pady=5, side=tk.LEFT)

    entry2 = tk.Entry(frame, width=15)
    entry2.pack(pady=5, side=tk.RIGHT)

    result_label = tk.Label(frame, text="Sum: ")
    result_label.pack(pady=5)

    def calculate_sum():
        try:
            num1 = float(entry1.get())
            num2 = float(entry2.get())
            result_label.config(text=f"Sum: {num1 + num2}")
        except ValueError:
            result_label.config(text="Error: Enter numbers")

    btn = tk.Button(frame, text="Add", command=calculate_sum)
    btn.pack(pady=10)
