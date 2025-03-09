import tkinter as tk
from tkinter import ttk
import os
import math
from tkinter import messagebox
from PIL import Image
custom_font_1 = ("Calibri", 11, "bold")
custom_font_2 = ("Calibri", 14, "bold", "underline")
custom_font_3 = ("Arial", 10, "bold")
def cylinder_calculation (Frame):
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ User Defined functions+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def label_inside_frame (Parent_frame,parameter,customfont, bground, fground):
        lable=tk.Label(Parent_frame,text=parameter, font=customfont,background=bground, foreground= fground)
        return lable     
    spinboxes = {}
    def spinbox_inside_Frame (Parent_Frame,Name,bground,fground):
        spinbox_inside_farame=tk.Spinbox(Parent_Frame, from_=0, to=10000, background=bground, foreground=fground,font=("callibre", 10), width=10)
        spinboxes[Name]=spinbox_inside_farame
        return spinbox_inside_farame
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Widgets+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    Frame1 = tk.LabelFrame(
    Frame, 
    text= " \u2699 Hydraulic Cylinder Calculations", 
    height=680, 
    width=1200,
    background="#002b36",highlightbackground="white",font=custom_font_1,foreground="white"
    )
    Frame1.place(x=10,y=2)
    Frame2=tk.Frame(Frame1,height=650, width=400, background="gainsboro")
    Frame2.place(x=790, y=10)
    
    label_inside_frame(Frame1,"INPUT PARAMETERS FOR CYLINDER CALCULATION", custom_font_2, "#002b36","white" ).place(x=250, y=10)
    label_inside_frame(Frame1,"Cap Side Diameter [mm]", custom_font_3, "#002b36","white" ).place(x=50, y=50)
    label_inside_frame(Frame1,"Rod Side Diameter [mm]", custom_font_3, "#002b36","white" ).place(x=50, y=100)
    label_inside_frame(Frame1,"Stroke Length [mm]", custom_font_3, "#002b36","white" ).place(x=50, y=150)
    label_inside_frame(Frame1,"Flow Rate [LPM]", custom_font_3, "#002b36","white").place(x=50, y=200)
    label_inside_frame(Frame1,"No of Cylinders", custom_font_3, "#002b36","white").place(x=250, y=50)
    label_inside_frame(Frame1,"Operating Pressure [bar]", custom_font_3, "#002b36","white").place(x=250, y=100)
    label_inside_frame(Frame1,"Inlet_Port_Size [mm]", custom_font_3, "#002b36","white").place(x=250, y=150)
    label_inside_frame(Frame1,"Outlet_Port_Size [mm]", custom_font_3, "#002b36","white").place(x=250, y=200)
    
    spinbox_inside_Frame(Frame1,"spinbox_for_capside_diameter","white","black").place(x=50,y=75)
    spinbox_inside_Frame(Frame1,"spinbox_for_rodside_diameter","white","black").place(x=50,y=125)
    spinbox_inside_Frame(Frame1,"spinbox_stroke_length","white","black").place(x=50,y=175)
    spinbox_inside_Frame(Frame1,"spinbox_FlowRate","white","black").place(x=50,y=225)
    spinbox_inside_Frame(Frame1,"spinbox_no_of_cylinders","white","black").place(x=250,y=75)
    spinbox_inside_Frame(Frame1,"spinbox_operating_pressure","white","black").place(x=250,y=125)
    Port_size = [ "G-1/8", "G-1/4", "G-3/8","G-1/2","G-3/4", "G-1", "G-1 1/4", "G-1 1/2","G-2"]
    combobox_for_inletPort_size = ttk.Combobox(Frame1, values=Port_size,width=11)
    combobox_for_inletPort_size.place(x=250, y=175)
    combobox_for_inletPort_size.current(6)
    combobox_for_outletPort_size = ttk.Combobox(Frame1, values=Port_size,width=11)
    combobox_for_outletPort_size.place(x=250, y=225)
    combobox_for_outletPort_size.current(5)
    
    

   
    return (Frame)

    
    



