import tkinter as tk

# Function to create a rounded rectangle on the Canvas
def create_rounded_box(canvas, x1, y1, x2, y2, radius, **kwargs):
    # Draw the rounded box by creating a combination of arcs and rectangles
    canvas.create_oval(x1, y1, x1 + radius, y1 + radius, **kwargs)  # Top-left arc
    canvas.create_oval(x2 - radius, y1, x2, y1 + radius, **kwargs)  # Top-right arc
    canvas.create_oval(x1, y2 - radius, x1 + radius, y2, **kwargs)  # Bottom-left arc
    canvas.create_oval(x2 - radius, y2 - radius, x2, y2, **kwargs)  # Bottom-right arc
    canvas.create_rectangle(x1 + radius, y1, x2 - radius, y2, **kwargs)  # Middle rectangle
    canvas.create_rectangle(x1, y1 + radius, x2, y2 - radius, **kwargs)  # Middle rectangle

# Initialize the Tkinter window
app = tk.Tk()
app.title("Smooth Edged Box Example")

# Box settings
box_background_color = "skyblue"
box_width = 300
box_height = 100
box_radius = 20  # Radius for smooth edges

# Canvas setup
canvas = tk.Canvas(app, width=box_width, height=box_height)
canvas.pack(pady=20)

# Create a rounded box (smooth edges)
create_rounded_box(canvas, 10, 10, box_width - 10, box_height - 10, radius=box_radius, fill=box_background_color, outline="blue")

# Add text on top of the rounded box
canvas.create_text(box_width / 2, box_height / 2, text="Smooth Box", font=("Arial", 14, "bold"), fill="white")

# Run the Tkinter event loop
app.mainloop()
