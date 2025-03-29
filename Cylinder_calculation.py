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
    text= " \u2699 Hydraulic Cylinder Calculation", 
    height=680, 
    width=1200,
    background="#002b36",highlightbackground="white",font=custom_font_1,foreground="white"
    )
    Frame1.place(x=10,y=2)
    Frame2=tk.Frame(Frame1,height=640, width=400, background="gainsboro")
    Frame2.place(x=790, y=10)
    Frame3=tk.Frame(Frame1,height=430, width=775, background="gainsboro")
    Frame3.place(x=10, y=220)
    Frame4 = tk.LabelFrame(
    Frame3, 
    text= " \u2699 Normal Extension", 
    height=350, 
    width=300,
    background="gainsboro",highlightbackground="black",font=custom_font_1,foreground="black"
    )
    Frame4.place(x=20, y=50)
    Frame5 = tk.LabelFrame(
    Frame3, 
    text= " \u2699 Regenerative Extension", 
    height=350, 
    width=300,
    background="gainsboro",highlightbackground="black",font=custom_font_1,foreground="black"
    )
    Frame5.place(x=400, y=50)

    label_inside_frame(Frame1,"INPUT PARAMETERS FOR CYLINDER CALCULATION", custom_font_2, "#002b36","white" ).place(x=250, y=10)
    label_inside_frame(Frame1,"Cap Side Diameter [mm]", custom_font_3, "#002b36","white" ).place(x=50, y=50)
    label_inside_frame(Frame1,"Rod Side Diameter [mm]", custom_font_3, "#002b36","white" ).place(x=50, y=100)
    label_inside_frame(Frame1,"Stroke Length [mm]", custom_font_3, "#002b36","white" ).place(x=50, y=150)
    label_inside_frame(Frame1,"Flow Rate [LPM]", custom_font_3, "#002b36","white").place(x=250, y=150)
    label_inside_frame(Frame1,"No of Cylinders", custom_font_3, "#002b36","white").place(x=250, y=50)
    label_inside_frame(Frame1,"Operating Pressure [bar]", custom_font_3, "#002b36","white").place(x=250, y=100)
    label_inside_frame(Frame1,"Inlet Port Size [BSP Port]", custom_font_3, "#002b36","white").place(x=450, y=50)
    label_inside_frame(Frame1,"Outlet Port Size [BSP Port]", custom_font_3, "#002b36","white").place(x=450, y=100)
    
    label_inside_frame(Frame3, "CALCULATION RESULTS", custom_font_2,"gainsboro", "black" ).place(x=250, y=10)
    #++++++++Normal extension+++++++++
    label_inside_frame(Frame4, "Cap Side Area [mm\u00b2]", custom_font_3,"gainsboro", "black" ).place(x=10, y=10)
    spinbox_inside_Frame(Frame4, "spinbox_for_cap_Area","white", "black").place(x=200, y=10)
    label_inside_frame(Frame4, "Rod Side Area [mm\u00b2]", custom_font_3,"gainsboro", "black" ).place(x=10, y=35)
    spinbox_inside_Frame(Frame4, "spinbox_for_rod_Area","white", "black").place(x=200, y=35)
    label_inside_frame(Frame4, "Area Ratio", custom_font_3,"gainsboro", "black" ).place(x=10, y=60)
    spinbox_inside_Frame(Frame4, "spinbox_for_Area_ratio","white", "black").place(x=200, y=60)
    label_inside_frame(Frame4, "Extension velocity [mm/s]", custom_font_3,"gainsboro", "black" ).place(x=10, y=85)
    spinbox_inside_Frame(Frame4, "spinbox_for_Extension_velocity","white", "black").place(x=200, y=85)
    label_inside_frame(Frame4, "Retraction Velocity [mm/s]", custom_font_3,"gainsboro", "black" ).place(x=10, y=110)
    spinbox_inside_Frame(Frame4, "spinbox_for_Retraction_velocity","white", "black").place(x=200, y=110)
    label_inside_frame(Frame4, "Extension Time [sec]", custom_font_3,"gainsboro", "black" ).place(x=10, y=135)
    spinbox_inside_Frame(Frame4, "spinbox_for_extension_time","white", "black").place(x=200, y=135)
    label_inside_frame(Frame4, "Retraction Time [sec]", custom_font_3,"gainsboro", "black" ).place(x=10, y=160)
    spinbox_inside_Frame(Frame4, "spinbox_for_retraction_time","white", "black").place(x=200, y=160)
    label_inside_frame(Frame4, "Cap Side Force [KN]", custom_font_3,"gainsboro", "black" ).place(x=10, y=185)
    spinbox_inside_Frame(Frame4, "spinbox_for_capside_force","white", "black").place(x=200, y=185)
    label_inside_frame(Frame4, "Rod Side Force [KN]", custom_font_3,"gainsboro", "black" ).place(x=10, y=210)
    spinbox_inside_Frame(Frame4, "spinbox_for_rodside_force","white", "black").place(x=200, y=210)   
    label_inside_frame(Frame4, "Velocity at cap port [m/s]", custom_font_3,"gainsboro", "black" ).place(x=10, y=235)
    spinbox_inside_Frame(Frame4, "spinbox_for_cap_velocity","white", "black").place(x=200, y=235)
    label_inside_frame(Frame4, "Velocity at Rod port [m/s]", custom_font_3,"gainsboro", "black" ).place(x=10, y=260)
    spinbox_inside_Frame(Frame4, "spinbox_for_rod_velocity","white", "black").place(x=200, y=260)
    #++++++++Regenerative extension+++++++++
    label_inside_frame(Frame5, "Cap Side Area [mm\u00b2]", custom_font_3,"gainsboro", "black" ).place(x=10, y=10)
    spinbox_inside_Frame(Frame5, "spinbox_for_cap_Area_1","white", "black").place(x=200, y=10)
    label_inside_frame(Frame5, "Rod Side Area [mm\u00b2]", custom_font_3,"gainsboro", "black" ).place(x=10, y=35)
    spinbox_inside_Frame(Frame5, "spinbox_for_rod_Area_1","white", "black").place(x=200, y=35)
    label_inside_frame(Frame5, "Area Ratio", custom_font_3,"gainsboro", "black" ).place(x=10, y=60)
    spinbox_inside_Frame(Frame5, "spinbox_for_Area_ratio_1","white", "black").place(x=200, y=60)
    label_inside_frame(Frame5, "Extension velocity [mm/s]", custom_font_3,"gainsboro", "black" ).place(x=10, y=85)
    spinbox_inside_Frame(Frame5, "spinbox_for_Extension_velocity_1","white", "black").place(x=200, y=85)
    label_inside_frame(Frame5, "Retraction Velocity [mm/s]", custom_font_3,"gainsboro", "black" ).place(x=10, y=110)
    spinbox_inside_Frame(Frame5, "spinbox_for_Retraction_velocity_1","white", "black").place(x=200, y=110)
    label_inside_frame(Frame5, "Extension Time [sec]", custom_font_3,"gainsboro", "black" ).place(x=10, y=135)
    spinbox_inside_Frame(Frame5, "spinbox_for_extension_time_1","white", "black").place(x=200, y=135)
    label_inside_frame(Frame5, "Retraction Time [sec]", custom_font_3,"gainsboro", "black" ).place(x=10, y=160)
    spinbox_inside_Frame(Frame5, "spinbox_for_retraction_time_1","white", "black").place(x=200, y=160)
    label_inside_frame(Frame5, "Cap Side Force [KN]", custom_font_3,"gainsboro", "black" ).place(x=10, y=185)
    spinbox_inside_Frame(Frame5, "spinbox_for_capside_force_1","white", "black").place(x=200, y=185)
    label_inside_frame(Frame5, "Rod Side Force [KN]", custom_font_3,"gainsboro", "black" ).place(x=10, y=210)
    spinbox_inside_Frame(Frame5, "spinbox_for_rodside_force_1","white", "black").place(x=200, y=210)   
    label_inside_frame(Frame5, "Velocity at cap port [m/s]", custom_font_3,"gainsboro", "black" ).place(x=10, y=235)
    spinbox_inside_Frame(Frame5, "spinbox_for_cap_velocity_1","white", "black").place(x=200, y=235)
    label_inside_frame(Frame5, "Velocity at Rod port [m/s]", custom_font_3,"gainsboro", "black" ).place(x=10, y=260)
    spinbox_inside_Frame(Frame5, "spinbox_for_rod_velocity_1","white", "black").place(x=200, y=260)

    spinbox_inside_Frame(Frame1,"spinbox_for_capside_diameter","white","black").place(x=50,y=75)
    spinbox_inside_Frame(Frame1,"spinbox_for_rodside_diameter","white","black").place(x=50,y=125)
    spinbox_inside_Frame(Frame1,"spinbox_stroke_length","white","black").place(x=50,y=175)
    spinbox_inside_Frame(Frame1,"spinbox_FlowRate","white","black").place(x=250,y=175)
    spinbox_inside_Frame(Frame1,"spinbox_no_of_cylinders","white","black").place(x=250,y=75)
    spinbox_inside_Frame(Frame1,"spinbox_operating_pressure","white","black").place(x=250,y=125)
    Port_size = [ "G-1/8", "G-1/4", "G-3/8","G-1/2","G-3/4", "G-1", "G-1 1/4", "G-1 1/2","G-2"]
    combobox_for_inletPort_size = ttk.Combobox(Frame1, values=Port_size,width=11)
    combobox_for_inletPort_size.place(x=450, y=75)
    combobox_for_inletPort_size.current(6)
    combobox_for_outletPort_size = ttk.Combobox(Frame1, values=Port_size,width=11)
    combobox_for_outletPort_size.place(x=450, y=125)
    combobox_for_outletPort_size.current(5)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Function Call for labels+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    label_inside_frame(Frame2,"SPECIFICATION OF THE OIL", custom_font_2,"gainsboro", "black").place(x=100, y=10)  
    label_inside_frame(Frame2,"\U0001F44D Hints", custom_font_2,"gainsboro", "black").place(x=150, y=300) 
    label_inside_frame(Frame2,"Oil Code                      = Shell Tellus S2 MX 46", custom_font_1,"gainsboro", "black").place(x=40, y=50)
    label_inside_frame(Frame2,"API Group                   = GroupII", custom_font_1,"gainsboro", "black").place(x=40, y=70)
    label_inside_frame(Frame2,"Base Oil                       = Mineral based oil", custom_font_1,"gainsboro", "black").place(x=40,y=90)
    label_inside_frame(Frame2,"Density                        = 846 kg/m\u00b3", custom_font_1,"gainsboro", "black").place(x=40,y=110)
    label_inside_frame(Frame2,"kinematic viscosity = 46 cSt\n @40 deg ", custom_font_1,"gainsboro", "black").place(x=40,y=130)
    label_inside_frame(Frame2,"kinematic viscosity = 6.9 cSt\n @100 deg ", custom_font_1,"gainsboro", "black").place(x=40,y=170)
    label_inside_frame(Frame2,"Viscosity index         = 105",custom_font_1,"gainsboro", "black").place(x=40,y=210)
    label_inside_frame(Frame2,"Flash point                 = 230 deg", custom_font_1,"gainsboro", "black").place(x=40,y=230)
    label_inside_frame(Frame2,"Pour point                  = -30 deg",custom_font_1,"gainsboro", "black").place(x=40,y=250)
    label_inside_frame(Frame2,"Specific gravity         = 0.846  ",custom_font_1,"gainsboro", "black").place(x=40,y=270)
    label_inside_frame(Frame2,"1 st = 10\u2074 m\u00b2/sec",custom_font_1,"gainsboro", "black").place(x=40, y=340)
    label_inside_frame(Frame2,"1 ct = 10\u2076 m\u00b2/sec",custom_font_1,"gainsboro", "black").place(x=40, y=360)
    label_inside_frame(Frame2,"1 pascal = 10\u2075 bar",custom_font_1,"gainsboro", "black").place(x=40, y=380)
    label_inside_frame(Frame2,"1 Mega pascal = 10 bar",custom_font_1,"gainsboro", "black").place(x=40, y=400)
 #+++ Calculation Part +++++++
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
    def Calculate ():
        cap_diameter=float(spinboxes["spinbox_for_capside_diameter"].get())
        no_of_cylinder=float(spinboxes["spinbox_no_of_cylinders"].get())
        capside_area=float(((math.pi / 4) * (cap_diameter** 2))*no_of_cylinder)
        spinboxes["spinbox_for_cap_Area"].delete(0, tk.END)
        spinboxes["spinbox_for_cap_Area"].insert(0, round(capside_area, 2))
        spinboxes["spinbox_for_cap_Area_1"].delete(0, tk.END)
        spinboxes["spinbox_for_cap_Area_1"].insert(0, round(capside_area, 2))       
        rod_diameter=float(spinboxes["spinbox_for_rodside_diameter"].get())
        rodside_area=float((math.pi / 4) * ((cap_diameter**2)-(rod_diameter** 2))*no_of_cylinder)
        spinboxes["spinbox_for_rod_Area"].delete(0, tk.END)
        spinboxes["spinbox_for_rod_Area"].insert(0, round(rodside_area, 2))
        spinboxes["spinbox_for_rod_Area_1"].delete(0, tk.END)
        spinboxes["spinbox_for_rod_Area_1"].insert(0, round(rodside_area, 2))    
        Area_ratio=float(capside_area/rodside_area)
        spinboxes["spinbox_for_Area_ratio"].delete(0, tk.END)
        spinboxes["spinbox_for_Area_ratio"].insert(0, round(Area_ratio, 2))
        spinboxes["spinbox_for_Area_ratio_1"].delete(0, tk.END)
        spinboxes["spinbox_for_Area_ratio_1"].insert(0, round(Area_ratio, 2))
        Flowrate=float(spinboxes["spinbox_FlowRate"].get())
        Flowrate_in_mm3per_sec=float(Flowrate*10**6)/60
        rodside_flowrate=Flowrate_in_mm3per_sec*Area_ratio
        Regeneration_flow=Flowrate_in_mm3per_sec+rodside_flowrate
        Extension_velocity=float(Flowrate_in_mm3per_sec/capside_area)
        spinboxes["spinbox_for_Extension_velocity"].delete(0, tk.END)
        spinboxes["spinbox_for_Extension_velocity"].insert(0, round(Extension_velocity, 2))
        Regenerative_Extensionvelocity=float(Flowrate_in_mm3per_sec/(capside_area-rodside_area))
        spinboxes["spinbox_for_Extension_velocity_1"].delete(0, tk.END)
        spinboxes["spinbox_for_Extension_velocity_1"].insert(0, round(Regenerative_Extensionvelocity, 2))
        Retraction_velocity=float(Flowrate_in_mm3per_sec/rodside_area)
        spinboxes["spinbox_for_Retraction_velocity"].delete(0, tk.END)
        spinboxes["spinbox_for_Retraction_velocity"].insert(0, round(Retraction_velocity, 2))
        spinboxes["spinbox_for_Retraction_velocity_1"].delete(0, tk.END)
        spinboxes["spinbox_for_Retraction_velocity_1"].insert(0, round(Retraction_velocity, 2))
        Cylinder_stroke=float(spinboxes["spinbox_stroke_length"].get())
        extension_time=float(Cylinder_stroke/Extension_velocity)
        spinboxes["spinbox_for_extension_time"].delete(0, tk.END)
        spinboxes["spinbox_for_extension_time"].insert(0, round(extension_time, 2)) 
        Renerative_extensiontime=float(Cylinder_stroke/Regenerative_Extensionvelocity)
        spinboxes["spinbox_for_extension_time_1"].delete(0, tk.END)
        spinboxes["spinbox_for_extension_time_1"].insert(0, round(Renerative_extensiontime, 2))      
        retraction_time=float(Cylinder_stroke/Retraction_velocity)
        spinboxes["spinbox_for_retraction_time"].delete(0, tk.END)
        spinboxes["spinbox_for_retraction_time"].insert(0, round(retraction_time, 2)) 
        spinboxes["spinbox_for_retraction_time_1"].delete(0, tk.END)
        spinboxes["spinbox_for_retraction_time_1"].insert(0, round(retraction_time, 2)) 
        pressure=float(spinboxes["spinbox_operating_pressure"].get())
        Pressure_mpa=float(pressure/10)
        cap_Force=Pressure_mpa*capside_area/1000
        spinboxes["spinbox_for_capside_force"].delete(0, tk.END)
        spinboxes["spinbox_for_capside_force"].insert(0, round(cap_Force, 2))     
        spinboxes["spinbox_for_capside_force_1"].delete(0, tk.END)
        spinboxes["spinbox_for_capside_force_1"].insert(0, round(cap_Force, 2)) 
        rod_Force=Pressure_mpa*rodside_area/1000
        spinboxes["spinbox_for_rodside_force"].delete(0, tk.END)
        spinboxes["spinbox_for_rodside_force"].insert(0, round(rod_Force, 2))   
        spinboxes["spinbox_for_rodside_force_1"].delete(0, tk.END)
        spinboxes["spinbox_for_rodside_force_1"].insert(0, round(rod_Force, 2)) 
        Port_size_inlet = combobox_for_inletPort_size.get()
        Port_size_outlet = combobox_for_outletPort_size.get()
        Port_Diameter_inlet = port_diameter_map.get(Port_size_inlet, 0)
        Port_Diameter_outlet = port_diameter_map.get(Port_size_outlet, 0)
        Port_Area_inlet = (math.pi / 4) * (Port_Diameter_inlet ** 2)
        Port_Area_outlet = (math.pi / 4) * (Port_Diameter_outlet ** 2)
        port_inlet_veloicty=Flowrate_in_mm3per_sec/Port_Area_inlet
        Port_inlet_Velocity_m_per_s=port_inlet_veloicty/1000
        spinboxes["spinbox_for_cap_velocity"].delete(0, tk.END)
        spinboxes["spinbox_for_cap_velocity"].insert(0, round(Port_inlet_Velocity_m_per_s, 2))
        port_inlet_veloicty_Reg=Regeneration_flow/Port_Area_inlet
        Port_inlet_Velocity_m_per_s_Reg=port_inlet_veloicty_Reg/1000
        spinboxes["spinbox_for_cap_velocity_1"].delete(0, tk.END)
        spinboxes["spinbox_for_cap_velocity_1"].insert(0, round(Port_inlet_Velocity_m_per_s_Reg, 2))
        Port_outlet_velocity=float(rodside_flowrate/Port_Area_outlet)
        Port_outlet_Velocity_m_per_s=Port_outlet_velocity/1000
        spinboxes["spinbox_for_rod_velocity"].delete(0, tk.END)
        spinboxes["spinbox_for_rod_velocity"].insert(0, round(Port_outlet_Velocity_m_per_s, 2))
        spinboxes["spinbox_for_rod_velocity_1"].delete(0, tk.END)
        spinboxes["spinbox_for_rod_velocity_1"].insert(0, round(Port_outlet_Velocity_m_per_s, 2))
        if Port_inlet_Velocity_m_per_s >= 8:
            spinboxes["spinbox_for_cap_velocity"].config(background = "red")
            messagebox.showinfo("Error","Inlet port velocity should be <8 m/s")
        else:
            spinboxes["spinbox_for_cap_velocity"].config(background = "white")
        if Port_inlet_Velocity_m_per_s_Reg >= 8:
            spinboxes["spinbox_for_cap_velocity_1"].config(background = "red")
            messagebox.showinfo("Error","Inlet port velocity should be <8 m/s")
        else:
            spinboxes["spinbox_for_cap_velocity_1"].config(background = "white")
        if Port_outlet_Velocity_m_per_s >= 8:
            spinboxes["spinbox_for_rod_velocity"].config(background = "red")
            spinboxes["spinbox_for_rod_velocity_1"].config(background = "red")
            messagebox.showinfo("Error","Outlet port velocity should be <8 m/s")
        else:
            spinboxes["spinbox_for_rod_velocity"].config(background = "white")
            spinboxes["spinbox_for_rod_velocity_1"].config(background = "white")
    
        
    Calculate_B1=tk.Button(Frame1, text="CALCULATE", width=15, height=1, background="yellow4", foreground="Black",font=custom_font_1,command= Calculate)
    Calculate_B1.place(x=370,y=170)









    
    

    

   
    return (Frame)

    
    



