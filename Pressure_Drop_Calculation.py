import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Importing from Pillown
import os
from tkinter import messagebox
custom_font_1 = ("Calibri", 11, "bold")
custom_font_2 = ("Calibri", 14, "bold", "underline")
custom_font_3 = ("Arial", 10, "bold")
def pressuer_drop_calculation(frame):
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ User Defined functions+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def label_inside_frame1 (parameter):
        lable=ttk.Label(Frame1,text=parameter, font=custom_font_3,background=Frame1.cget("bg"), foreground="white")
        return lable
    def label_inside_frame2 (Parent_frame,parameter,customfont):
        lable=tk.Label(Parent_frame,text=parameter, font=customfont,background=Frame2.cget("bg"), foreground="black")
        return lable    
    def lable_For_heading (parameter):
        lable=tk.Label(Frame2, text=parameter, font=custom_font_2, background=Frame2.cget("bg"), foreground="black")
        return lable  
    spinboxes = {}
    def spinbox_inside_Frame3 (Parent_Frame, Name):
        spinbox_inside_farame3=tk.Spinbox(Parent_Frame, from_=0, to=10000, background="white", foreground="black",font=("callibre", 10), width=10)
        spinboxes[Name]=spinbox_inside_farame3
        return spinbox_inside_farame3
    #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Frame Inside Pressure drop Calculations+++++++++++++++++++++++++++++++++++++++++++++++++++++
    Frame1 = tk.LabelFrame(
    frame, 
    text= " \u2699 Pressure Drop Calculation", 
    height=680, 
    width=1200,
    background="#002b36",highlightbackground="white",font=custom_font_1,foreground="white"
    )
    Frame1.place(x=10,y=2)
    Frame2=tk.Frame(frame,height=650, width=400, background="gainsboro")
    Frame2.place(x=800, y=20)
    Frame3=tk.Frame(Frame1,height=150, width=775, background="gainsboro" )
    Frame3.place(x=10, y=290)
    Frame4=tk.Frame(Frame1,height=198, width=775, background="gainsboro")
    Frame4.place(x=10,y=450)
    lable_For_heading("SPECIFICATION OF THE OIL").place(x=100, y=10)
    lable_For_heading("\U0001F44D Hints").place(x=150, y=300)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Function Call for labels+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    label_inside_frame2(Frame2,"Oil Code                      = Shell Tellus S2 MX 46", custom_font_1).place(x=40, y=50)
    label_inside_frame2(Frame2,"API Group                   = GroupII", custom_font_1).place(x=40, y=70)
    label_inside_frame2(Frame2,"Base Oil                       = Mineral based oil", custom_font_1).place(x=40,y=90)
    label_inside_frame2(Frame2,"Density                        = 846 kg/m\u00b3", custom_font_1).place(x=40,y=110)
    label_inside_frame2(Frame2,"kinematic viscosity = 46 cSt\n @40 deg ", custom_font_1).place(x=40,y=130)
    label_inside_frame2(Frame2,"kinematic viscosity = 6.9 cSt\n @100 deg ", custom_font_1).place(x=40,y=170)
    label_inside_frame2(Frame2,"Viscosity index         = 105",custom_font_1).place(x=40,y=210)
    label_inside_frame2(Frame2,"Flash point                 = 230 deg", custom_font_1).place(x=40,y=230)
    label_inside_frame2(Frame2,"Pour point                  = -30 deg",custom_font_1).place(x=40,y=250)
    label_inside_frame2(Frame2,"Specific gravity         = 0.846  ",custom_font_1).place(x=40,y=270)
    label_inside_frame2(Frame2,"1 st = 10\u2074 m\u00b2/sec",custom_font_1).place(x=40, y=340)
    label_inside_frame2(Frame2,"1 ct = 10\u2076 m\u00b2/sec",custom_font_1).place(x=40, y=360)
    label_inside_frame2(Frame2,"1 pascal = 10\u2075 bar",custom_font_1).place(x=40, y=380)
    label_inside_frame2(Frame2,"1 Mega pascal = 10 bar",custom_font_1).place(x=40, y=400)
    label_inside_frame2(Frame3,"Inlet Port Size [BSP Port]",custom_font_1).place(x=50,y=40)
    label_inside_frame2(Frame3,"Outlet Port Size [BSP Port]",custom_font_1).place(x=50, y=90)
    label_inside_frame2(Frame3,"Flow Rate [LPM]",custom_font_1).place(x=250, y=40)
    label_inside_frame2(Frame4," Calculation Results", custom_font_2 ).place(x=300, y=10)
    label_inside_frame2(Frame4,"Inlet Area [mm\u00b2]", custom_font_1 ).place(x=50, y=40)
    label_inside_frame2(Frame4,"Outlet Area [mm\u00b2]", custom_font_1 ).place(x=50, y=90)
    label_inside_frame2(Frame4,"Area Ratio", custom_font_1 ).place(x=50, y=140)
    label_inside_frame2(Frame4,"Inlet Velocity [m/sec]", custom_font_1 ).place(x=300, y=40)
    label_inside_frame2(Frame4,"outlet Velocit [m/sec]", custom_font_1 ).place(x=300, y=90)
    label_inside_frame2(Frame4,"Pressure Drop  [bar]", custom_font_1 ).place(x=300, y=140)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Function Call for Spinboxex+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    spinbox_inside_Frame3(Frame3, "Spinbox_for_Flowrate").place(x=250, y=65)
    spinbox_inside_Frame3(Frame4, "Spinbox_for_InletArea").place(x=50, y=65)
    spinbox_inside_Frame3(Frame4, "Spinbox_for_outletArea").place(x=50, y=115)
    spinbox_inside_Frame3(Frame4, "Spinbox_for_Area Ratio").place(x=50, y=165)
    spinbox_inside_Frame3(Frame4, "Spinbox_for_inletvelocity").place(x=300, y=65)
    spinbox_inside_Frame3(Frame4, "Spinbox_for_outletvelocity").place(x=300, y=115)
    spinbox_inside_Frame3(Frame4, "Spinbox_for_PressureDrop").place(x=300, y=165)
    label_inside_frame1("This Calculation is based on Bernoullis Theory, Bernoullis theory is based on the Law of conservation of energy,\
    \nthe sum of potential energy, kinetic energy and Flow energy at any point inside the flow domain will be equal, \
    \n \
    \nAssumptions:\
    \n\
    \n1.Flow should be incompressible\
    \n2.Energy is conserved\
    \n3.Steady flow\
    \n4.Inviscous fluids\
    \n(but real fluids has viscosity, need to include head losses\
    \n \
    \nApplications:\
    \n\
    \nTo Measure Pressure Drop").place(x=5, y=10)
    #-----------------------------------------------------------------Loading images------------------------------------------------------
    image_path = os.path.join(os.path.dirname(__file__), 'Picture1.png')
    Picture1 = Image.open(image_path)
    Picture1 = Picture1.resize((330, 220), Image.LANCZOS)  # Resize the image to 200x150 pixels
    photo = ImageTk.PhotoImage(Picture1)
    label_for_cross_section = tk.Label(Frame1, image=photo)
    label_for_cross_section.image = photo  # Keep a reference to avoid garbage collection
    label_for_cross_section.place(x=450,y=60)
    image_path = os.path.join(os.path.dirname(__file__), 'Picture2.png')
    Picture2 = Image.open(image_path)
    Picture2 = Picture2.resize((230, 110), Image.LANCZOS)  # Resize the image to 200x150 pixels
    photo = ImageTk.PhotoImage(Picture2)
    label_for_eqn = tk.Label(Frame3, image=photo)
    label_for_eqn.image = photo  # Keep a reference to avoid garbage collection
    label_for_eqn.place(x=500,y=30)
    outlet_port_size = [ "G-1/8", "G-1/4", "G-3/8","G-1/2","G-3/4", "G-1", "G-1 1/4", "G-1 1/2","G-2"]
    inlet_port_size = ["G-2","G-1 1/2","G-1 1/4","G-1","G-3/4","G-1/2","G-3/8","G-1/4","G-1/8"]
    combobox_for_inletPort_size = ttk.Combobox(Frame3, values=inlet_port_size,width=11)
    combobox_for_inletPort_size.place(x=50, y=65)
    combobox_for_inletPort_size.current(1)
    combobox_for_outletPort_size = ttk.Combobox(Frame3, values=outlet_port_size,width=11)
    combobox_for_outletPort_size.place(x=50, y=115)
    combobox_for_outletPort_size.current(1)
    Lable_for_input_Parameters= tk.Label(Frame3,text="Input Parameters For Pressure Drop Calculation",font=custom_font_2, background=Frame3.cget("bg"), foreground="black")
    Lable_for_input_Parameters.place(x=170, y=0)
#++++++++++++++ Calculation Part+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Event calling function for Port size
    import math  
    port_diameter_map = {
    "G-1/8": 8.5,
    "G-1/4": 11.5,
    "G-3/8": 15,
    "G-1/2" : 19,
    "G-3/4": 24,
    "G-1": 30,
    "G-1 1/4": 38,
    "G-1 1/2": 45,
    "G-2": 27
    }
    def Port_szie_selection (event):
        Port_size_inlet = combobox_for_inletPort_size.get()
        Port_size_outlet = combobox_for_outletPort_size.get()
        Port_Diameter_inlet = port_diameter_map.get(Port_size_inlet, 0)
        Port_Diameter_outlet = port_diameter_map.get(Port_size_outlet, 0)
        Port_Area_inlet = (math.pi / 4) * (Port_Diameter_inlet ** 2)
        Port_Area_outlet = (math.pi / 4) * (Port_Diameter_outlet ** 2)
        Area_ratio = Port_Area_inlet/Port_Area_outlet
        spinboxes["Spinbox_for_InletArea"].delete(0, tk.END)
        spinboxes["Spinbox_for_InletArea"].insert(0, round(Port_Area_inlet, 2))  
        spinboxes["Spinbox_for_outletArea"].delete(0, tk.END)
        spinboxes["Spinbox_for_outletArea"].insert(0, round(Port_Area_outlet, 2)) 
        spinboxes["Spinbox_for_Area Ratio"].delete(0, tk.END)
        spinboxes["Spinbox_for_Area Ratio"].insert(0, round(Area_ratio, 2))    
        if Port_Area_outlet >= Port_Area_inlet:
            messagebox.showinfo("Error","Inlet Port should be greater than outlet port ")      
    combobox_for_inletPort_size.bind("<<ComboboxSelected>>",Port_szie_selection)
    combobox_for_outletPort_size.bind("<<ComboboxSelected>>",Port_szie_selection)
#event calling for calculate button
    def Calculate():
        Flowrate=float(spinboxes["Spinbox_for_Flowrate"].get())
        Flowrate_in_mm3per_sec=float(Flowrate*10**6)/60
        Inlet_Area=float(spinboxes["Spinbox_for_InletArea"].get())
        inlet_velociy_mm_per_sec=  Flowrate_in_mm3per_sec/Inlet_Area
        inlet_velociy_m_per_sec= inlet_velociy_mm_per_sec/1000
        spinboxes["Spinbox_for_inletvelocity"].delete(0, tk.END)
        spinboxes["Spinbox_for_inletvelocity"].insert(0, round(inlet_velociy_m_per_sec, 2))
        Outlet_Area=float(spinboxes["Spinbox_for_outletArea"].get())
        outlet_velociy_mm_per_sec=Flowrate_in_mm3per_sec/Outlet_Area
        outlet_velociy_m_per_sec=outlet_velociy_mm_per_sec/1000
        spinboxes["Spinbox_for_outletvelocity"].delete(0, tk.END)
        spinboxes["Spinbox_for_outletvelocity"].insert(0, round(outlet_velociy_m_per_sec, 2))   
        Density=float(856)#kg/m3
        Part1=float((Density*inlet_velociy_m_per_sec**2)/2)
        Part2=float(((Inlet_Area/Outlet_Area)**2)-1)
        pressuer_drop=float(Part1*Part2)
        Pressure_drop_in_bar=pressuer_drop/100000
        spinboxes["Spinbox_for_PressureDrop"].delete(0, tk.END)
        spinboxes["Spinbox_for_PressureDrop"].insert(0, round(Pressure_drop_in_bar, 2))         
        if inlet_velociy_m_per_sec >= 6:
            spinboxes["Spinbox_for_inletvelocity"].config(background = "red")
            messagebox.showinfo("Error","Inlet velocity should be <6 m/s")
        else:
            spinboxes["Spinbox_for_inletvelocity"].config(background = "white")
        if outlet_velociy_m_per_sec >= 6:
            spinboxes["Spinbox_for_outletvelocity"].config(background = "red")
            messagebox.showinfo("Error","outlet velocity should be <6 m/s")
        else:
            spinboxes["Spinbox_for_outletvelocity"].config(background = "white")            


    Calculate_B1=tk.Button(Frame3, text="CALCULATE", width=15, height=1, background="yellow4", foreground="Black",font=custom_font_1,command= Calculate)
    Calculate_B1.place(x=250,y=110)
    
    return(lable)
