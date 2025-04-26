import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Importing from Pillown
import os
from tkinter import messagebox
service_page_open = False
service_page_frame = None
custom_font_1 = ("Calibri", 11, "bold")
custom_font_2 = ("Calibri", 14, "bold", "underline")
custom_font_3 = ("Arial", 10, "bold")

def Service_page_1 (frame):
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ User Defined functions+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def label_inside_frame1 (parameter):
        lable=ttk.Label(Frame1,text=parameter, font=custom_font_3,background=Frame1.cget("bg"), foreground="white")
        return lable
    def label_inside_frame2 (Parent_frame,parameter,customfont):
        lable=tk.Label(Parent_frame,text=parameter, font=customfont,background=Frame2.cget("bg"), foreground="black")
        return lable    
    #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Frame Inside Pressure drop Calculations+++++++++++++++++++++++++++++++++++++++++++++++++++++
    Frame1 = tk.Frame(
    frame,
    height=250, 
    width=220,
    background="gainsboro",highlightbackground="white")
    Frame1.place(x=20,y=200)
    
 
    return(Service_page_1)

