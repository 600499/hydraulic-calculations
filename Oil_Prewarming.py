import tkinter as tk
from tkinter import ttk
import os
import math
from tkinter import messagebox
from PIL import Image, ImageTk
custom_font_1 = ("Calibri", 11, "bold")
custom_font_2 = ("Calibri", 14, "bold", "underline")
custom_font_3 = ("Arial", 10, "bold")
def oil_prewarming_calculation (Frame):
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
    text= " \u2699 Oil Pewarming Calculation", 
    height=680, 
    width=1200,
    background="#002b36",highlightbackground="white",font=custom_font_1,foreground="white"
    )
    Frame1.place(x=10,y=2)
    Frame2=tk.Frame(Frame1,height=640, width=400, background="gainsboro")
    Frame2.place(x=790, y=10)
    Frame3=tk.Frame(Frame1,height=340, width=775, background="gainsboro")
    Frame3.place(x=10,y=310)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++images inside the applications+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    image_path = os.path.join(os.path.dirname(__file__), 'Pressure_Drop.png')
    Picture1 = Image.open(image_path)
    Picture1 = Picture1.resize((330, 220), Image.LANCZOS)  # Resize the image to 200x150 pixels
    photo = ImageTk.PhotoImage(Picture1)
    label_for_Pressuredrop = tk.Label(Frame1, image=photo)
    label_for_Pressuredrop.image = photo  # Keep a reference to avoid garbage collection
    label_for_Pressuredrop.place(x=450,y=80)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Function Call for labels+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    label_inside_frame(Frame1, "This calculation is based on the law of conservation of energy,i.e Energy can be converted into one form to another form\
    \nLosss in hydaulic energy due to the pressure drop across the throttle is converted into the heat energy." , custom_font_3, "#002b36", "white").place(x=5,y=10)
    label_inside_frame(Frame1, "INPUT PARAMETERS FOR CALCULATIONS", custom_font_2,"#002b36", "white" ).place(x=170,y=50)

    label_inside_frame(Frame1,"Pressure Drop [bar]",custom_font_3, "#002b36", "white" ).place(x=30, y=90)
    label_inside_frame(Frame1,"Oil Tank Capacity [Litres]",custom_font_3, "#002b36", "white" ).place(x=30, y=120)
    label_inside_frame(Frame1,"Flow Rate [LPM]",custom_font_3, "#002b36", "white" ).place(x=30, y=150)
    label_inside_frame(Frame1,"Starting Temperature [deg C]",custom_font_3, "#002b36", "white" ).place(x=30, y=180)
    label_inside_frame(Frame1,"End Temp [deg C]",custom_font_3, "#002b36", "white" ).place(x=30, y=210)

    spinbox_inside_Frame(Frame1, "spinbox_for_Pressure_drop","white", "black").place(x=250, y=90)
    spinbox_inside_Frame(Frame1, "spinbox_for_oilTank_Capacity","white", "black").place(x=250, y=120)
    spinbox_inside_Frame(Frame1, "spinbox_for_Flowrate","white", "black").place(x=250, y=150)
    spinbox_inside_Frame(Frame1, "spinbox_for_Starting_Temperature","white", "black").place(x=250, y=180)
    spinbox_inside_Frame(Frame1, "spinbox_for_End_Temperature","white", "black").place(x=250, y=210)

    label_inside_frame(Frame3,"Mass of the Oil [kg]",custom_font_3, "gainsboro", "black" ).place(x=30, y=50)
    label_inside_frame(Frame3,"Mass Flow Rate [kg/s]",custom_font_3, "gainsboro", "black" ).place(x=30, y=80)
    label_inside_frame(Frame3,"Energy Loss [KJ/s]",custom_font_3, "gainsboro", "black" ).place(x=30, y=110)
    label_inside_frame(Frame3,"Temperature Raise [deg C]",custom_font_3, "gainsboro", "black" ).place(x=30, y=140)
    label_inside_frame(Frame3,"Oil Prewarming Time [sec]",custom_font_3, "gainsboro", "black" ).place(x=30, y=170)
    label_inside_frame(Frame3,"Temperature Raise [deg C/min]",custom_font_3, "gainsboro", "black" ).place(x=30, y=200)

    spinbox_inside_Frame(Frame3, "spinbox_for_Mass","white", "black").place(x=250, y=50)
    spinbox_inside_Frame(Frame3, "spinbox_for_MassFlow_Rate","white", "black").place(x=250, y=80)
    spinbox_inside_Frame(Frame3, "spinbox_for_Energy_loss","white", "black").place(x=250, y=110)
    spinbox_inside_Frame(Frame3, "spinbox_for_DeltaT","white", "black").place(x=250, y=140)
    spinbox_inside_Frame(Frame3, "spinbox_for_oilprewarming_Time","white", "black").place(x=250, y=170)
    spinbox_inside_Frame(Frame3, "spinbox_for_TemperatureRaise","white", "black").place(x=250, y=200)

    Target_Entry=tk.Entry(Frame3,background="yellow4",foreground="black", width=18, font=custom_font_1)
    Target_Entry.place(x=520,y=20,height=25, width=150)
    Target_Entry.insert(0, "Target > 1 deg C/min")
    label_inside_frame(Frame3,"CALCULATION RESULTS",custom_font_2, "gainsboro","black").place(x=250, y=10)




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
    def calculate ():
        Density=float(856)
        CP_of_Oil=float(2.1)
        Tank_volume=float(spinboxes["spinbox_for_oilTank_Capacity"].get())
        Mass_of_Oil=float((Tank_volume/1000)*Density)
        spinboxes["spinbox_for_Mass"].delete(0, tk.END)
        spinboxes["spinbox_for_Mass"].insert(0, round(Mass_of_Oil,2))
        Flow_rate=float(spinboxes["spinbox_for_Flowrate"].get())    
        Mass_flow_rate=float(((Flow_rate)/(1000*60))*Density)
        spinboxes["spinbox_for_MassFlow_Rate"].delete(0, tk.END)
        spinboxes["spinbox_for_MassFlow_Rate"].insert(0, round(Mass_flow_rate,2))
        Pressure_drop=float(spinboxes["spinbox_for_Pressure_drop"].get())
        Energy_loss=float(Pressure_drop*Flow_rate/600)
        spinboxes["spinbox_for_Energy_loss"].delete(0, tk.END)       
        spinboxes["spinbox_for_Energy_loss"].insert(0, round(Energy_loss,2)) 
        DeltaT=((Energy_loss)/(CP_of_Oil*Mass_flow_rate))     
        spinboxes["spinbox_for_DeltaT"].delete(0, tk.END)       
        spinboxes["spinbox_for_DeltaT"].insert(0, round(DeltaT,2))
        Time_req_to_raise_DeltaT=float((Mass_of_Oil/Mass_flow_rate)/60)
        starting_Temp=float(spinboxes["spinbox_for_Starting_Temperature"].get())
        End_Temp=float(spinboxes["spinbox_for_End_Temperature"].get())       
        Temp_Difference=float(End_Temp-starting_Temp) 
        Oil_prewarming_Time=float(((Temp_Difference*Time_req_to_raise_DeltaT)/DeltaT)*1.3)
        spinboxes["spinbox_for_oilprewarming_Time"].delete(0, tk.END)       
        spinboxes["spinbox_for_oilprewarming_Time"].insert(0, round(Oil_prewarming_Time,2))   
        Temperature_Raise=float(Temp_Difference/Oil_prewarming_Time) 
        spinboxes["spinbox_for_TemperatureRaise"].delete(0, tk.END)       
        spinboxes["spinbox_for_TemperatureRaise"].insert(0, round(Temperature_Raise,2))  
        if Temperature_Raise < 1:
            spinboxes["spinbox_for_TemperatureRaise"].config(background = "red")
            messagebox.showinfo("Error","Temperature Raise should be > 1 deg C/min")
        else:
            spinboxes["spinbox_for_TemperatureRaise"].config(background = "white")

        return 



    Calculate_B1=tk.Button(Frame1, text="CALCULATE", width=15, height=1, background="yellow4", foreground="Black",font=custom_font_1,command= calculate)
    Calculate_B1.place(x=150,y=250)







    

   
    return (Frame)

    
    



