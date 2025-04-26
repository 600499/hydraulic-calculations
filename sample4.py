import tkinter as tk

app = tk.Tk()
app.geometry("600x400")

# 1. Create the Frame (but don't place it yet)
service_page_frame = tk.Frame(app, width=300, height=200, bg="gainsboro")

# 2. Create a variable to track if frame is open or not
service_page_open = False

# 3. Function to open/close the frame
def toggle_service_page():
    global service_page_open

    if not service_page_open:
        service_page_frame.place(x=20, y=100)  # Show the frame
        service_page_open = True
    else:
        service_page_frame.place_forget()       # Hide the frame
        service_page_open = False

# 4. Button to toggle
B13 = tk.Button(app, text="☰ Service page", width=20, height=1,
                background="yellow4", foreground="white",
                command=toggle_service_page)
B13.place(x=20, y=20)

app.mainloop()
