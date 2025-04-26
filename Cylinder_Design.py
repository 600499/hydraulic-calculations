import tkinter as tk
from tkinter import ttk
import math
import os
from PIL import Image,ImageTk
from tkinter import messagebox
custom_font_1 = ("Calibri", 11, "bold")
custom_font_2 = ("Calibri", 14, "bold", "underline")
custom_font_3 = ("Arial", 10, "bold")
custom_font_4 = ("Arial", 12, "bold", "underline")
def cylinder_Design (Frame):
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ User Defined functions+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def label_inside_frame (Parent_frame,parameter,customfont, bground, fground):
        lable=ttk.Label(Parent_frame,text=parameter, font=customfont,background=bground, foreground= fground)
        return lable     
    spinboxes = {}
    def spinbox_inside_Frame (Parent_Frame,Name,bground,fground):
        spinbox_inside_farame=tk.Spinbox(Parent_Frame, from_=0, to=10000, background=bground, foreground=fground,font=("callibre", 10), width=10)
        spinboxes[Name]=spinbox_inside_farame
        return spinbox_inside_farame
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Widgets+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    Frame1 = tk.LabelFrame(
    Frame, 
    text= " \u2699 Cylinder Design Calculation", 
    height=680, 
    width=1200,
    background="#002b36",highlightbackground="white",font=custom_font_1,foreground="white"
    )
    Frame1.place(x=10,y=2)
    Frame2=tk.Frame(Frame1,height=640, width=400, background="gainsboro")
    Frame2.place(x=790, y=10)
    Frame3=tk.Frame(Frame1,height=220, width=775, background="#002b36", highlightbackground="white", highlightthickness=1)
    Frame3.place(x=10, y=200)
    Frame4=tk.Frame(Frame1,height=220, width=775, background="gainsboro", highlightbackground="white")
    Frame4.place(x=10, y=430)



   
   
 #++++++++++++++++++ Widgets inside Frame3+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    label_inside_frame(Frame1,"INPUT PARAMETERS FOR CYLINDER CALCULATION", custom_font_2, "#002b36","white" ).place(x=250, y=10)
    label_inside_frame(Frame1,"Piston Rod Design",custom_font_4,"#002b36","yellow4").place(x=20, y=30)
    label_inside_frame(Frame1,"The piston rod of the hudraulic cylinder is highly stressed and therefore it should be able to resist bending, tensile\
    \nand compressive forces that it may encounter during its operation without buckling \
    \nPiston rod diameter is related to the crital buckling load as per Euler's Formula.",custom_font_3,"#002b36","white").place(x=20, y=60)
    label_inside_frame(Frame1,"Cylinder Cap Design",custom_font_4,"#002b36","yellow4").place(x=20, y=110)
    label_inside_frame(Frame1,"The strength of the cylinder tube is proportional to its wall thickness, A cylinder that is tooo thick or too thin may pose\
    \nserious safety and operationl problems and hence the tube thickness of the cylinder has to be carefully chosen\
    \nThe cylinder material and wall thickness should resist the hoop stress produced by the hydraulic pressure.",custom_font_3,"#002b36","white").place(x=20, y=140)
    label_inside_frame(Frame3,"Outer Diameter - OD [mm]", custom_font_3, "#002b36","white").place(x=20, y=10)
    spinbox_inside_Frame(Frame3, "spinbox_for_Outer_Diameter","white", "black").place(x=20, y=35)  
    label_inside_frame(Frame3,"Inner Diameter - ID [mm]", custom_font_3, "#002b36","white" ).place(x=20, y=60)
    spinbox_inside_Frame(Frame3, "spinbox_for_cap_Dia","white", "black").place(x=20, y=85)
    label_inside_frame(Frame3,"Piston Diameter [mm]", custom_font_3, "#002b36","white" ).place(x=20, y=110)
    spinbox_inside_Frame(Frame3, "spinbox_for_rod_Dia","white", "black").place(x=20, y=135)
    label_inside_frame(Frame3,"Mounting Length [mm]", custom_font_3, "#002b36","white" ).place(x=20, y=160)
    spinbox_inside_Frame(Frame3, "spinbox_for_stroke_Length","white", "black").place(x=20, y=185)
    label_inside_frame(Frame3,"Operating Pressure [bar]", custom_font_3, "#002b36","white").place(x=300, y=10)
    spinbox_inside_Frame(Frame3, "spinbox_for_operating_Pressure","white", "black").place(x=300, y=35)
    Material=[ "42CrMo4", "C45", "FCD 450", "ST52-3"]
    label_inside_frame(Frame3,"Piston Material", custom_font_3, "#002b36","white").place(x=300, y=60)
    Combobox_for_piston_Material = ttk.Combobox(Frame3, values=Material,width=11)
    Combobox_for_piston_Material.place(x=300, y=85)  
    label_inside_frame(Frame3,"Tube Material", custom_font_3, "#002b36","white").place(x=300, y=110)    
    Combobox_for_tube_Material = ttk.Combobox(Frame3, values=Material,width=11)
    Combobox_for_tube_Material.place(x=300, y=135)       
    label_inside_frame(Frame3,"Mounting Type", custom_font_3, "#002b36","white").place(x=300, y=160)
    Port_size = [ "Case 1", "Case 2", "Case 3"]
    combobox_for_mounting_type = ttk.Combobox(Frame3, values=Port_size,width=11)
    combobox_for_mounting_type.place(x=300, y=185)   


 #++++++++++++++++++ Widgets inside Frame4+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    label_inside_frame(Frame4,"Moment of Inertia [mm\u2074]", custom_font_3, "gainsboro","black" ).place(x=20, y=10)
    spinbox_inside_Frame(Frame4, "spinbox_for_moment_of_inertia","white", "black").place(x=20, y=35)
    label_inside_frame(Frame4,"slenderness Ratio [\u03BB]", custom_font_3, "gainsboro","black" ).place(x=20, y=60)
    spinbox_inside_Frame(Frame4, "spinbox_for_slenderness_ratio","white", "black").place(x=20, y=85)
    label_inside_frame(Frame4,"slenderness Ratio 2 [\u03BB g]", custom_font_3, "gainsboro","black" ).place(x=20, y=110)
    spinbox_inside_Frame(Frame4, "spinbox_for_slenderness_ratio_2","white", "black").place(x=20, y=135)
    label_inside_frame(Frame4,"Effective buckling length [mm]", custom_font_3, "gainsboro","black" ).place(x=20, y=160)
    spinbox_inside_Frame(Frame4, "spinbox_for_Effective_buckling_length","white", "black").place(x=20, y=185)
    label_inside_frame(Frame4,"Buckling load [KN]", custom_font_3, "gainsboro","black" ).place(x=230, y=10)
    spinbox_inside_Frame(Frame4, "spinbox_for_buckling_load","white", "black").place(x=230, y=35)
    label_inside_frame(Frame4,"Working load [KN]", custom_font_3, "gainsboro","black" ).place(x=230, y=60)
    spinbox_inside_Frame(Frame4, "spinbox_for_Working_load","white", "black").place(x=230, y=85)
    label_inside_frame(Frame4,"FOS for Buckling", custom_font_3, "gainsboro","black" ).place(x=230, y=110)
    spinbox_inside_Frame(Frame4, "spinbox_for_Factor_of_safety_for_buckling","white", "black").place(x=230, y=135)
    label_inside_frame(Frame4,"Cylinder Thickness [mm]", custom_font_3, "gainsboro","black" ).place(x=230, y=160)
    spinbox_inside_Frame(Frame4, "spinbox_for_cylinder_thickness","white", "black").place(x=230, y=185)
    label_inside_frame(Frame4,"Hoop Stress [N/mm\u00b2]", custom_font_3, "gainsboro","black" ).place(x=400, y=10)
    spinbox_inside_Frame(Frame4, "spinbox_for_Hoop_Stress","white", "black").place(x=400, y=35)
    label_inside_frame(Frame4,"Longitudinal Stress [N/mm\u00b2]", custom_font_3, "gainsboro","black" ).place(x=400, y=60)
    spinbox_inside_Frame(Frame4, "spinbox_for_longitudinal_stress","white", "black").place(x=400, y=85)
    label_inside_frame(Frame4,"Radial Stress [N/mm\u00b2]", custom_font_3, "gainsboro","black" ).place(x=400, y=110)
    spinbox_inside_Frame(Frame4, "spinbox_for_radial_stress","white", "black").place(x=400, y=135)
    label_inside_frame(Frame4,"FOS for Tube Thickness", custom_font_3, "gainsboro","black" ).place(x=400, y=160)
    spinbox_inside_Frame(Frame4, "spinbox_for_FOS_Tube_thickness","white", "black").place(x=400, y=185)
    label_inside_frame(Frame4,"Yield Stress-Piston [N/mm\u00b2]", custom_font_3, "gainsboro","black" ).place(x=600, y=10)
    spinbox_inside_Frame(Frame4, "spinbox_for_yieldstress_piston","white", "black").place(x=600, y=35)
    label_inside_frame(Frame4,"Young's Modulus - Piston", custom_font_3, "gainsboro","black" ).place(x=600, y=60)
    spinbox_inside_Frame(Frame4, "spinbox_ofr_youngsModulus_piston","white", "black").place(x=600, y=85)
    label_inside_frame(Frame4,"Yield Stress - Tube [N/mm\u00b2]", custom_font_3, "gainsboro","black" ).place(x=600, y=110)
    spinbox_inside_Frame(Frame4, "spinbox_for_yieldstress_tube","white", "black").place(x=600, y=135)
    label_inside_frame(Frame4,"Young's Modulus - Tube", custom_font_3, "gainsboro","black" ).place(x=600, y=160)
    spinbox_inside_Frame(Frame4, "spinbox_ofr_youngsModulus_tube","white", "black").place(x=600, y=185)

    image_path = os.path.join(os.path.dirname(__file__), 'hoop_stress.png')
    Picture1 = Image.open(image_path)
    Picture1 = Picture1.resize((240, 160), Image.LANCZOS) 
    photo = ImageTk.PhotoImage(Picture1)
    label_for_case1 = tk.Label(Frame3, image=photo)
    label_for_case1.image = photo  # Keep a reference to avoid garbage collection
    label_for_case1.place(x=480,y=10)

    label_inside_frame(Frame2, "Characteristics of Effecive Buckling length", custom_font_4,"gainsboro", "black").place(x=40, y=10)
    label_inside_frame(Frame2, "case (i):Both Ends are fixed and Guided", custom_font_1,"gainsboro", "black").place(x=20, y=45)
    image_path = os.path.join(os.path.dirname(__file__), 'BothEndFixed_Guided.png')
    Picture1 = Image.open(image_path)
    Picture1 = Picture1.resize((160, 150), Image.LANCZOS) 
    photo = ImageTk.PhotoImage(Picture1)
    label_for_case1 = tk.Label(Frame2, image=photo)
    label_for_case1.image = photo  # Keep a reference to avoid garbage collection
    label_for_case1.place(x=100,y=70)
    label_inside_frame(Frame2, "Case (ii):One end Pivoted and another end guided or \
                       \nboth ends are pivoted and guided", custom_font_1,"gainsboro", "black").place(x=20, y=220)
    image_path = os.path.join(os.path.dirname(__file__), 'OneEndFixed_pivoted.png')
    Picture1 = Image.open(image_path)
    Picture1 = Picture1.resize((160, 150), Image.LANCZOS) 
    photo = ImageTk.PhotoImage(Picture1)
    label_for_case1 = tk.Label(Frame2, image=photo)
    label_for_case1.image = photo  # Keep a reference to avoid garbage collection
    label_for_case1.place(x=100,y=260)
    label_inside_frame(Frame2, "Case (iii):One end fixed and another end free", custom_font_1,"gainsboro", "black").place(x=20, y=410)
    image_path = os.path.join(os.path.dirname(__file__), 'One_End_Fixed_Free.png')
    Picture1 = Image.open(image_path)
    Picture1 = Picture1.resize((160, 150), Image.LANCZOS) 
    photo = ImageTk.PhotoImage(Picture1)
    label_for_case1 = tk.Label(Frame2, image=photo)
    label_for_case1.image = photo  # Keep a reference to avoid garbage collection
    label_for_case1.place(x=100,y=435)

    def Calculate ():
        Mounting_Type_Map={
            "Case 1" : 0.7, "Case 2" : 1, "Case 3" : 2
        }
        Youngs_Modulus_Map={
            "42CrMo4" : 210000, "C45" : 210000, "FCD 450" : 170000, "ST52-3" : 210000
        }
        Yield_Stress_Map={
            "42CrMo4" : 800, "C45" : 353, "FCD 450" : 280, "ST52-3" : 450
        }
        Cap_Diameter=float(spinboxes["spinbox_for_cap_Dia"].get())
        Rod_Diameter=float(spinboxes["spinbox_for_rod_Dia"].get())
        Stroke_Length=float(spinboxes["spinbox_for_stroke_Length"].get())
        Mouting_Type=combobox_for_mounting_type.get()
        Piston_Material=Combobox_for_piston_Material.get()
        youngs_Modulus_piston=float(Youngs_Modulus_Map.get(Piston_Material, 0))
        Yield_Strength_Piston=float(Yield_Stress_Map.get(Piston_Material, 0))
        Tube_Material=Combobox_for_tube_Material.get()
        Yield_Strenth_Tube=(Yield_Stress_Map.get(Tube_Material, 0))
        youngs_Modulus_tube=float(Youngs_Modulus_Map.get(Tube_Material, 0))        
        Effectiv_Buckling_Length=float((Mounting_Type_Map.get(Mouting_Type,0))*Stroke_Length)
        Hydrauic_Pressure=float(spinboxes["spinbox_for_operating_Pressure"].get())
        Caspide_Area=float(((math.pi / 4) * (Cap_Diameter** 2)))
        Rodside_Area=float((math.pi/4)*((Cap_Diameter)**2-(Rod_Diameter)**2))
        Capside_Force=float(((Hydrauic_Pressure/10)*Caspide_Area)/1000)
        Rodside_Force=float((Hydrauic_Pressure/10)*Rodside_Area)
        Area_Moment_of_Inertia=float((math.pi/64*(Rod_Diameter)**4))
        Slenderness_Ratio1=float(4*Effectiv_Buckling_Length/Rod_Diameter)
        Slenderness_Ratio2=float(math.pi*(math.sqrt((youngs_Modulus_piston)/(0.8*Yield_Strength_Piston))))
        Outer_Diameter=float(spinboxes["spinbox_for_Outer_Diameter"].get())
        Outer_Radius=float(Outer_Diameter/2)
        Inner_Diameter=float(spinboxes["spinbox_for_cap_Dia"].get())
        Inner_Radius=float(Inner_Diameter/2)
        Thickness=float((Outer_Diameter-Inner_Diameter)/2)
        if Thickness/Inner_Diameter <= 0.05:
            Lable1=ttk.Label(Frame4, text="Thin Cylinder", font=custom_font_3, background="gainsboro", foreground="Red")
            Lable1.place(x=300, y=185)
            Radial_Stress="NA"
            Longitudinal_Stress=float(((Hydrauic_Pressure/10)*Inner_Diameter)/(4*Thickness)) 
            Hoop_Stress=float(((Hydrauic_Pressure/10)*Inner_Diameter)/(2*Thickness))
            spinboxes["spinbox_for_radial_stress"].delete(0, tk.END)
            spinboxes["spinbox_for_radial_stress"].insert(0,Radial_Stress)
            Max_Stress=max(Hoop_Stress,Longitudinal_Stress)
            Factor_of_Safety_Tube=float(Yield_Strenth_Tube/Max_Stress)  
             
        else:
            Lable1=ttk.Label(Frame4, text="Thick Cylinder", font=custom_font_3, background="gainsboro", foreground="Red")
            Lable1.place(x=300, y=185)
            L1=float(((Hydrauic_Pressure/10)*(Inner_Radius**2))/(Outer_Radius**2-Inner_Radius**2))
            L2=float((1)-(Outer_Radius**2/Inner_Radius**2))
            L3=float((1)+(Outer_Radius**2/Inner_Radius**2))
            Radial_Stress=L1*L2*-1
            Longitudinal_Stress=float((Hydrauic_Pressure/10)*((Inner_Radius**2)/(Outer_Radius**2-Inner_Radius**2)))
            Hoop_Stress=L1*L3
            spinboxes["spinbox_for_radial_stress"].delete(0, tk.END)
            spinboxes["spinbox_for_radial_stress"].insert(0, round(Radial_Stress,2))
            Max_Stress=max(Radial_Stress,Hoop_Stress,Longitudinal_Stress)
            Factor_of_Safety_Tube=float(Yield_Strenth_Tube/Max_Stress)
   
        if Slenderness_Ratio1 >= Slenderness_Ratio2:
            Buckling_load=float((((math.pi**2)*youngs_Modulus_piston*Area_Moment_of_Inertia)/(3.5*Effectiv_Buckling_Length**2))/1000)
        else:
            Numerator1=float(math.pi*((335-(0.62*Slenderness_Ratio1))))
            Numerator2=float(Rod_Diameter**2)
            Buckling_load=float(((Numerator1*Numerator2)/(4*3.5))/1000)
        Factor_of_Safety_Rod=float(Buckling_load/Capside_Force)
        spinboxes["spinbox_for_moment_of_inertia"].delete(0, tk.END)
        spinboxes["spinbox_for_moment_of_inertia"].insert(0, round(Area_Moment_of_Inertia,2))
        spinboxes["spinbox_for_Effective_buckling_length"].delete(0, tk.END)
        spinboxes["spinbox_for_Effective_buckling_length"].insert(0, round(Effectiv_Buckling_Length,2))
        spinboxes["spinbox_for_Working_load"].delete(0, tk.END)
        spinboxes["spinbox_for_Working_load"].insert(0, round(Capside_Force,2))
        spinboxes["spinbox_for_slenderness_ratio"].delete(0, tk.END)
        spinboxes["spinbox_for_slenderness_ratio"].insert(0, round(Slenderness_Ratio1,2))
        spinboxes["spinbox_for_slenderness_ratio_2"].delete(0, tk.END)
        spinboxes["spinbox_for_slenderness_ratio_2"].insert(0, round(Slenderness_Ratio2,2))
        spinboxes["spinbox_for_buckling_load"].delete(0, tk.END)
        spinboxes["spinbox_for_buckling_load"].insert(0, round(Buckling_load,2))
        spinboxes["spinbox_for_Factor_of_safety_for_buckling"].delete(0, tk.END)
        spinboxes["spinbox_for_Factor_of_safety_for_buckling"].insert(0, round(Factor_of_Safety_Rod,2))
        spinboxes["spinbox_for_Hoop_Stress"].delete(0, tk.END)
        spinboxes["spinbox_for_Hoop_Stress"].insert(0, round(Hoop_Stress,2))
        spinboxes["spinbox_for_longitudinal_stress"].delete(0, tk.END)
        spinboxes["spinbox_for_longitudinal_stress"].insert(0, round(Longitudinal_Stress,2))               
        spinboxes["spinbox_for_cylinder_thickness"].delete(0, tk.END)
        spinboxes["spinbox_for_cylinder_thickness"].insert(0, round(Thickness,2))
        spinboxes["spinbox_for_FOS_Tube_thickness"].delete(0, tk.END)
        spinboxes["spinbox_for_FOS_Tube_thickness"].insert(0, round(Factor_of_Safety_Tube,2))
        spinboxes["spinbox_for_yieldstress_piston"].delete(0, tk.END)
        spinboxes["spinbox_for_yieldstress_piston"].insert(0, round(Yield_Strength_Piston,2))
        spinboxes["spinbox_ofr_youngsModulus_piston"].delete(0, tk.END)
        spinboxes["spinbox_ofr_youngsModulus_piston"].insert(0, round(youngs_Modulus_piston,2))
        spinboxes["spinbox_for_yieldstress_tube"].delete(0, tk.END)
        spinboxes["spinbox_for_yieldstress_tube"].insert(0, round(Yield_Strenth_Tube,2))
        spinboxes["spinbox_ofr_youngsModulus_tube"].delete(0, tk.END)
        spinboxes["spinbox_ofr_youngsModulus_tube"].insert(0, round(youngs_Modulus_tube,2))
        
        if (Capside_Force >= Buckling_load ):
            spinboxes["spinbox_for_Working_load"].config(background = "red")
            messagebox.showinfo("Error","working load should be < Buckling Load")   
        else:
            spinboxes["spinbox_for_Working_load"].config(background = "white")
        if (Longitudinal_Stress >= Yield_Strenth_Tube ):
            spinboxes["spinbox_for_longitudinal_stress"].config(background = "red")
            messagebox.showinfo("Error","Longitudinal stress should be < Yield Stress")   
        else:
            spinboxes["spinbox_for_longitudinal_stress"].config(background = "white")
        if (Hoop_Stress >= Yield_Strenth_Tube ):
            spinboxes["spinbox_for_Hoop_Stress"].config(background = "red")
            messagebox.showinfo("Error","Hoop stress should be < Yield Stress")   
        else:
            spinboxes["spinbox_for_Hoop_Stress"].config(background = "white")
        if (Radial_Stress >= Buckling_load ):
            spinboxes["spinbox_for_radial_stress"].config(background = "red")
            messagebox.showinfo("Error","Radial Stress should be < Buckling Load")   
        else:
            spinboxes["spinbox_for_radial_stress"].config(background = "white")
 
            

    
        return()










    Calculate_B1=tk.Button(Frame3, text="CALCULATE", width=15, height=1, background="yellow4", foreground="Black",font=custom_font_1,command=Calculate)
    Calculate_B1.place(x=550,y=180)




    return ()

