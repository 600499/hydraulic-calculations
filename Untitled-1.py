import math
import tkinter as tk
from tkinter import ttk

# Example dictionary to hold spinbox references (update based on your actual structure)
spinboxes = {
    "Spinbox_for_InletArea": None,  # Assign actual Spinbox widget
    "Spinbox_for_OutletArea": None  # Assign actual Spinbox widget
}

# Dictionary to store port sizes and their diameters
port_diameter_map = {
    "G-1/8": 10,
    "G-1/4": 20,
    "G-3/8": 30,
    "G-3/4": 40,
    "G-1": 50,
    "G-1 1/4": 60,
    "G-1 1/2": 70
}

def Port_size_selection(event):
    # Get selected inlet and outlet port sizes
    Port_size_inlet = combobox_for_inletPort_size.get()
    Port_size_outlet = combobox_for_outletPort_size.get()

    # Get diameters from dictionary
    Port_Diameter_inlet = port_diameter_map.get(Port_size_inlet, 0)
    Port_Diameter_outlet = port_diameter_map.get(Port_size_outlet, 0)

    # Calculate areas
    Port_Area_inlet = (math.pi / 4) * (Port_Diameter_inlet ** 2)
    Port_Area_outlet = (math.pi / 4) * (Port_Diameter_outlet ** 2)

    # Update spinboxes with calculated areas
    if spinboxes["Spinbox_for_InletArea"]:
        spinboxes["Spinbox_for_InletArea"].delete(0, tk.END)
        spinboxes["Spinbox_for_InletArea"].insert(0, round(Port_Area_inlet, 2))

    if spinboxes["Spinbox_for_OutletArea"]:
        spinboxes["Spinbox_for_OutletArea"].delete(0, tk.END)
        spinboxes["Spinbox_for_OutletArea"].insert(0, round(Port_Area_outlet, 2))

# Example: Create your comboboxes (ensure they exist in your UI)
root = tk.Tk()

combobox_for_inletPort_size = ttk.Combobox(root, values=list(port_diameter_map.keys()))
combobox_for_inletPort_size.bind("<<ComboboxSelected>>", Port_size_selection)
combobox_for_inletPort_size.grid(row=0, column=1)

combobox_for_outletPort_size = ttk.Combobox(root, values=list(port_diameter_map.keys()))
combobox_for_outletPort_size.bind("<<ComboboxSelected>>", Port_size_selection)
combobox_for_outletPort_size.grid(row=1, column=1)

# Create spinboxes and add them to the dictionary
spinboxes["Spinbox_for_InletArea"] = ttk.Spinbox(root)
spinboxes["Spinbox_for_InletArea"].grid(row=0, column=2)

spinboxes["Spinbox_for_OutletArea"] = ttk.Spinbox(root)
spinboxes["Spinbox_for_OutletArea"].grid(row=1, column=2)

root.mainloop()
