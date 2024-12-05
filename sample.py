import os
import tkinter as tk
from PIL import Image, ImageTk

# Create the main application window
root = tk.Tk()
root.title("Animated Background Example")
root.geometry("800x600")  # Set the window size

# Create a frame
Fram3 = tk.Frame(root, width=800, height=600)
Fram3.place(x=0, y=0)

# List of image file paths (replace with your own image paths)
image_files = [
    os.path.join(os.path.dirname(__file__), 'cloud.jpg'),
    os.path.join(os.path.dirname(__file__), 'cloud2.jpg'),
    os.path.join(os.path.dirname(__file__), 'cloud3.jpg')
]

# Function to load and resize images
def load_images(image_files, width, height):
    images = []
    for file in image_files:
        img = Image.open(file).resize((width, height), Image.LANCZOS)
        images.append(ImageTk.PhotoImage(img))
    return images

# Load all images and store them in a list
frame_width = 800
frame_height = 600
images = load_images(image_files, frame_width, frame_height)

# Add the first image to the frame as a label
current_image_index = 0
label_for_shibauralogo = tk.Label(Fram3, image=images[current_image_index])
label_for_shibauralogo.place(x=0, y=0, relwidth=1, relheight=1)

# Function to update the image
def update_image():
    global current_image_index
    current_image_index = (current_image_index + 1) % len(images)  # Loop through images
    label_for_shibauralogo.configure(image=images[current_image_index])
    label_for_shibauralogo.image = images[current_image_index]  # Keep reference
    root.after(3000, update_image)  # Call this function again after 3 seconds

# Start the animation
root.after(3000, update_image)

# Add other widgets on top of the frame (optional)
label = tk.Label(Fram3, text="Welcome to the Animated Background!", font=("Calibri", 20), bg="white")
label.place(x=50, y=50)

# Start the main event loop
root.mainloop()
