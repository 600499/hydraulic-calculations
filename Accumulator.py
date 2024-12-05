import tkinter as tk
from tkinter import ttk
from functools import partial
from PIL import Image, ImageTk  # Importing from Pillown
import os
from time import strftime

# Create the main application window
app = tk.Tk () 
app.title("Hydraulic calculations Application Prepared by...............................ASK")
app.geometry("1500x900+200+50")
app.resizable(False, False) 
app.configure(background="#002b36")
# custom font
cutom_font1=("arial", 11)
custom_font2=("callibre",12,"bold")
custom_font3=("callibre",14,"bold")
#frames
Frame1 = tk.LabelFrame(
    app, 
    text= " \u2630 list of contents", 
    height=730, 
    width=280,
    background="grey23",highlightbackground="white",font=cutom_font1,foreground="white"
)
Frame1.place(x=1215,y=165)
Fram2=tk.Frame(app,height=160, width=1500, highlightbackground="white", background="gainsboro")
Fram2.pack(side="top", fill="x", padx=1, pady=1)
Fram3=tk.Frame(app,height=685, width=1210, background="#002b36")
Fram3.place(x=1,y=210)
# user defined functions
def label_animation(label1, color1):
    labels = [L1, L2, L3, L4, L5, L6]
    for la in labels:
        la.configure(background="grey23")
    label1.configure(background=color1) 
def Theory_of_hyd ():
    B11.destroy()
    L11.destroy ()
    L7=tk.Label(Frame1,text="\U0001F4D6", height=2,width=0, background="grey23",font=("Segoe UI Emoji", 10),
    foreground="white")
    L7.place(x=15,y=345)
    B7=tk.Button(Frame1, text="Bernoullis Theory", width=20, height=1, background="steelblue", foreground="white",font=cutom_font1)
    B7.place(x=45,y=350)
    L8=tk.Label(Frame1,text="\U0001F4D6", height=2,width=0, background="grey23",font=("Segoe UI Emoji", 10),
    foreground="white")
    L8.place(x=15,y=395)
    B8=tk.Button(Frame1, text="Pascal Law", width=20, height=1, background="steelblue", foreground="white",font=cutom_font1)
    B8.place(x=45,y=400)
    L9=tk.Label(Frame1,text="\U0001F4D6", height=2,width=0, background="grey23",font=("Segoe UI Emoji", 10),
    foreground="white")
    L9.place(x=15,y=445)
    B9=tk.Button(Frame1, text="Theories of Accumulators", width=20, height=1, background="steelblue", foreground="white",font=cutom_font1)
    B9.place(x=45,y=450)
    L10=tk.Label(Frame1,text="\U0001F4D6", height=2,width=0, background="grey23",font=("Segoe UI Emoji", 10),
    foreground="white")
    L10.place(x=15,y=495)
    B10=tk.Button(Frame1, text="Darcy weisback Equations", width=20, height=1, background="steelblue", foreground="white",font=cutom_font1)
    B10.place(x=45,y=500)
    L12=tk.Label(Frame1,text="", height=2,width=0, background="grey23")
    L12.place(x=260,y=545)
    B12=tk.Button(Frame1, text="\u2699Service page", width=25, height=1, background="yellow4", foreground="white",font=cutom_font1,command=partial(label_animation, L12, "yellow4"))
    B12.place(x=20,y=550)
def lable_inside_frame2 (text):
    lable_inside_frame = ttk.Label(text=text,foreground="black", background="gainsboro",font=custom_font2)
    return lable_inside_frame
def display_image(image_path, x, y, width, height):
    image = Image.open(image_path)
    image = image.resize((width, height), Image.LANCZOS)  # Resize the image
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(app, image=photo)
    label.image = photo  # Keep a reference to avoid garbage collection
    label.place(x=x, y=y)
# function to update date and time
time_entry=tk.Entry(Fram2,background="yellow4",foreground="white", width=18, font=cutom_font1)
time_entry.place(x=1050,y=55,height=25, width=150)
def update_time ():
    current_time=strftime('%H : %M : %S')
    time_entry.delete(0,tk.END)
    time_entry.insert(0, f"  Time : {current_time}")
    #Time_lable.configure(text=f"Time : {current_time}")
    app.after(1000, update_time)
update_time ()  
Date=strftime("%d : %m : %Y")
date_entry=tk.Entry(Fram2,background="yellow4",foreground="white", width=18, font=cutom_font1)
date_entry.place(x=1050,y=15,height=25, width=150)
date_entry.delete(0, tk.END)
date_entry.insert(0,f"  Date : {Date}")
display_image(os.path.join(os.path.dirname(__file__), 'shibaura_new.png'), 30, 40, 180, 70)
display_image(os.path.join(os.path.dirname(__file__), 'hyd.jpg'), 1250, 15, 200, 130)
# Image animation for screen
image_list = [
    os.path.join(os.path.dirname(__file__), 'cloud3.jpg'),
    os.path.join(os.path.dirname(__file__), 'cloud.jpg'),
    os.path.join(os.path.dirname(__file__), 'cloud2.jpg'), 
    os.path.join(os.path.dirname(__file__), 'unit2.jpg'),
    os.path.join(os.path.dirname(__file__), 'team.jpg')
]
# Function to load and resize images
def load_images(image_list, width, height):
    images = []
    for file in image_list:
        img = Image.open(file).resize((width, height), Image.LANCZOS)
        images.append(ImageTk.PhotoImage(img))
    return images
images = load_images(image_list, 1210, 685)
# Add the first image to the frame as a label
current_image_index = 0
label_for_images = tk.Label(Fram3, image=images[current_image_index])
label_for_images.place(x=0, y=0, relwidth=1, relheight=1)
# Function to update the image
def update_image():
    global current_image_index
    current_image_index = (current_image_index + 1) % len(images)  # Loop through images
    label_for_images.configure(image=images[current_image_index])
    label_for_images.image = images[current_image_index]  # Keep reference
    app.after(3000, update_image)  # Call this function again after 3 seconds
# Start the animation
app.after(3000, update_image)
lable_inside_frame2("Research and Developement of Shibaura Machine").place(x=20,y=10)
lable_inside_frame2("Prepared by : ASK").place(x=1050, y=130)
lable_inside_frame2("Approved by : SVK").place(x=20, y=130)
#Heading_lable=tk.Label(Fram2,text="Hydraulic Calculation Application",font=custom_font3,background="lightslategrey",
                        #foreground= "black", height=2, width=30, relief= "ridge")
#Heading_lable.place(x=520,y=10)
#Buttons inside frame1
L1=tk.Label(Frame1,text="", height=2,width=0, background="grey23")
L1.place(x=260,y=45)
B1=tk.Button(Frame1, text=" \U0001F6E0 Throttle Calculations", width=25, height=1, background="yellow4", foreground="white",font=cutom_font1, command=partial(label_animation, L1, "yellow4") )
B1.place(x=20,y=50)
L2=tk.Label(Frame1,text="", height=2,width=0, background="grey23")
L2.place(x=260,y=95)
B2=tk.Button(Frame1, text="\U0001F527 Hydraulic cylinder calculations", width=25, height=1, background="yellow4", foreground="white",font=cutom_font1,command=partial(label_animation, L2, "yellow4"))
B2.place(x=20,y=100)
L3=tk.Label(Frame1,text="", height=2,width=0, background="grey23")
L3.place(x=260,y=145)
B3=tk.Button(Frame1, text="\U0001F4D5 Pipe Flow Calculations", width=25, height=1, background="yellow4", foreground="white",font=cutom_font1,command=partial(label_animation, L3, "yellow4"))
B3.place(x=20,y=150)
L4=tk.Label(Frame1,text="", height=2,width=0, background="grey23")
L4.place(x=260,y=195)
B4=tk.Button(Frame1, text="\U0001F529 Pressure Drop Calculations", width=25, height=1, background="yellow4", foreground="white",font=cutom_font1,command=partial(label_animation, L4, "yellow4"))
B4.place(x=20,y=200)
L5=tk.Label(Frame1,text="", height=2,width=0, background="grey23")
L5.place(x=260,y=245)
B5=tk.Button(Frame1, text="\u2702 Accumulator Calculations", width=25, height=1, background="yellow4", foreground="white",font=cutom_font1,command=partial(label_animation, L5, "yellow4"))
B5.place(x=20,y=250)
L6=tk.Label(Frame1,text="", height=2,width=0, background="grey23")
L6.place(x=260,y=295)
def combined_function ():
    label_animation (L6,"yellow4")
    Theory_of_hyd ()
B6=tk.Button(Frame1, text="\U0001F6E2 Theory of hydraulics", width=25, height=1, background="yellow4", foreground="white",font=cutom_font1,command=combined_function)
B6.place(x=20,y=300)
L11=tk.Label(Frame1,text="", height=2,width=0, background="grey23")
L11.place(x=260,y=345)
B11=tk.Button(Frame1, text=" \u2699 Service page", width=25, height=1, background="yellow4", foreground="white",font=cutom_font1,command=partial(label_animation, L11, "yellow4"))
B11.place(x=20,y=350)
B13=tk.Button(app, text=" \u2630 Service page", width=20, height=1, background="yellow4", foreground="white",font=cutom_font1,command=partial(label_animation, L11, "yellow4"))
B13.place(x=1,y=170)
B14=tk.Button(app, text=" \u2630 Service page", width=20, height=1, background="yellow4", foreground="white",font=cutom_font1,command=partial(label_animation, L11, "yellow4"))
B14.place(x=195,y=170)
B15=tk.Button(app, text=" \u2630 Service page", width=20, height=1, background="yellow4", foreground="white",font=cutom_font1,command=partial(label_animation, L11, "yellow4"))
B15.place(x=389,y=170)
B16=tk.Button(app, text=" \u2630 Service page", width=20, height=1, background="yellow4", foreground="white",font=cutom_font1,command=partial(label_animation, L11, "yellow4"))
B16.place(x=583,y=170)

# Run the application
app.mainloop()
