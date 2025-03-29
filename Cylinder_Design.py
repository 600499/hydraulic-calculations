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
    label_inside_frame(Frame3,"Cap Side Diameter [mm]", custom_font_3, "#002b36","white" ).place(x=20, y=10)
    spinbox_inside_Frame(Frame3, "spinbox_for_cap_Dia","white", "black").place(x=20, y=35)
    label_inside_frame(Frame3,"Rod Side Diameter [mm]", custom_font_3, "#002b36","white" ).place(x=20, y=60)
    spinbox_inside_Frame(Frame3, "spinbox_for_rod_Dia","white", "black").place(x=20, y=85)
    label_inside_frame(Frame3,"Stroke Length [mm]", custom_font_3, "#002b36","white" ).place(x=20, y=110)
    spinbox_inside_Frame(Frame3, "spinbox_for_stroke_Length","white", "black").place(x=20, y=135)
    label_inside_frame(Frame3,"Operating Pressure [bar]", custom_font_3, "#002b36","white").place(x=20, y=160)
    spinbox_inside_Frame(Frame3, "operating_Pressure","white", "black").place(x=20, y=185)
    label_inside_frame(Frame3,"young's Modulus for Piston [N/mm\u00b2]", custom_font_3, "#002b36","white").place(x=300, y=10)
    spinbox_inside_Frame(Frame3, "spinbox_for_piston_young's_Modulus","white", "black").place(x=300, y=35)
    label_inside_frame(Frame3,"Mounting Type", custom_font_3, "#002b36","white").place(x=300, y=60)
    Port_size = [ "Case 1", "Case 2", "Case 3"]
    combobox_for_mounting_type = ttk.Combobox(Frame3, values=Port_size,width=11)
    combobox_for_mounting_type.place(x=300, y=85)   
    label_inside_frame(Frame3,"Tube Thickness [mm]", custom_font_3, "#002b36","white").place(x=300, y=110)
    spinbox_inside_Frame(Frame3, "spinbox_for_Tube_Thickness","white", "black").place(x=300, y=135)


 #++++++++++++++++++ Widgets inside Frame4+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    label_inside_frame(Frame4,"Moment of Inertia [mm\u00b4]", custom_font_3, "gainsboro","black" ).place(x=20, y=10)
    spinbox_inside_Frame(Frame4, "spinbox_for_moment_of_inertia","white", "black").place(x=20, y=35)
    label_inside_frame(Frame4,"slenderness Ratio [\u03BB]", custom_font_3, "gainsboro","black" ).place(x=20, y=60)
    spinbox_inside_Frame(Frame4, "spinbox_for_slenderness_ratio","white", "black").place(x=20, y=85)
    label_inside_frame(Frame4,"slenderness Ratio 2 [\u03BB g]", custom_font_3, "gainsboro","black" ).place(x=20, y=105)
    spinbox_inside_Frame(Frame4, "spinbox_for_slenderness_ratio_2","white", "black").place(x=20, y=130)
    label_inside_frame(Frame4,"Buckling load [N]", custom_font_3, "gainsboro","black" ).place(x=20, y=155)
    spinbox_inside_Frame(Frame4, "spinbox_for_buckling_load","white", "black").place(x=20, y=180)
    label_inside_frame(Frame4,"Working load [N]", custom_font_3, "gainsboro","black" ).place(x=300, y=10)
    spinbox_inside_Frame(Frame4, "spinbox_for_Working_load","white", "black").place(x=300, y=35)
    label_inside_frame(Frame4,"Factor of safety", custom_font_3, "gainsboro","black" ).place(x=300, y=60)
    spinbox_inside_Frame(Frame4, "spinbox_for_Factor_of_safety","white", "black").place(x=300, y=85)








    image_path = os.path.join(os.path.dirname(__file__), 'hoop_stress.png')
    Picture1 = Image.open(image_path)
    Picture1 = Picture1.resize((180, 155), Image.LANCZOS) 
    photo = ImageTk.PhotoImage(Picture1)
    label_for_case1 = tk.Label(Frame3, image=photo)
    label_for_case1.image = photo  # Keep a reference to avoid garbage collection
    label_for_case1.place(x=570,y=10)
    


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

    Calculate_B1=tk.Button(Frame3, text="CALCULATE", width=15, height=1, background="yellow4", foreground="Black",font=custom_font_1,command= ())
    Calculate_B1.place(x=600,y=180)




    return ()

