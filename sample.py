import tkinter as tk
from PIL import Image, ImageTk  # For handling images beyond .png

# Create main window
root = tk.Tk()
root.title("Picture with Matching Background")

# Define frame background color
frame_color = "#f0e68c"  # Khaki

# Set root background color
root.configure(bg=frame_color)

# Create a frame with the same background color
frame = tk.Frame(root, bg=frame_color, width=500, height=500)
frame.place(x=50, y=50)

# Load an image
image = Image.open("D:\Hydraulics\Python Programming\hydraulic-calculations\shibaura_new.png")
# Replace 'example.jpg' with your image path
image = image.resize((200, 200), Image.LANCZOS)  # Resize the image
photo = ImageTk.PhotoImage(image)

# Add the image to the frame
label = tk.Label(frame, image=photo, bg="red")  # Match background color
label.place(x=150, y=150)

# Run the application
root.geometry("600x600")  # Set window size
root.mainloop()
