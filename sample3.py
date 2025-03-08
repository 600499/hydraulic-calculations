import tkinter as tk

def load_calculation1(frame):
    """Load widgets for Calculation 1 in the given frame."""
    label = tk.Label(frame, text="Calculation 1", font=("Arial", 16))
    label.pack(pady=10)

    entry = tk.Entry(frame, width=30)
    entry.pack(pady=5)

    result_label = tk.Label(frame, text="Result: ")
    result_label.pack(pady=5)

    def calculate():
        value = entry.get()
        result_label.config(text=f"Result: {value}")

    btn = tk.Button(frame, text="Calculate", command=calculate)
    btn.pack(pady=10)
