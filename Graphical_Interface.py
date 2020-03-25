# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 02:08:52 2020

@author: Saurabh
"""

import Face_Recognition as frec
import pandas as pd
from tkinter import *
import pickle
import numpy as np
import os
BASE_DIR=BASE_DIR = os.path.dirname(os.path.abspath("__file__"))
df=pd.read_csv('Attendances.csv')
file1 = open("Total_attendance.txt","r+")
Total_classes = int(file1.read())
file1.close()
password="S@123"
with open("pickles/face-labels.pickle", 'rb') as f:
	og_labels = pickle.load(f)
	labels = {v:k for k,v in og_labels.items()}
Roll_Count=len(labels.keys())
ar = []
for i in range(Roll_Count):
    ar.append(False)
window=Tk()
window.title('ATTENDANCE SYSTEM')
window.geometry("500x500+10+20")
window.resizable(0,0)
def open1():
    messagebox.showinfo("Information","Press 'q' once your face is identified ")
    a=int(frec.A())
    print("a="+str(a))
    ar[a]=True
def open2():
    b=False
    top = Toplevel()
    top.title("VERIFICATION")
    top.resizable(0,0)
    top.geometry("300x100")
    lbl=Label(top, text="Enter Admin Password", fg='red', font=("Helvetica", 9))
    lbl.place(x=80,y=0)
    txtfld=Entry(top, show='*',text="This is Entry Widget", bd=5)
    txtfld.place(x=80, y=25)
    passwd=""
    def close():
        passwd=txtfld.get()
        if(passwd==password):
            b=True
            for i in range(Roll_Count):
                if(ar[i] is True):
                    df.loc[df['Roll_No.'] == i+1 , 'Total_Classes_Attended'] +=1
                    ar[i]=False
            #Total_classes+=1
            global Total_classes
            Total_classes+=1
            file1=file1 = open("Total_attendance.txt","w")
            file1.write(str(Total_classes))
            file1.close()
            df.to_csv(r'Attendances.csv',index=False)
            
        print("CLOSE"+passwd)
        txtfld.delete(0,'end')
        top.destroy()
    btn=Button(top, text="OK", fg='blue',command=close)
    btn.place(x=100,y=50)
    if(b):
        print("SUCESSFUL")
    else:
        print("UNSUCESSFUL"+"  "+passwd)
def open3():
    top = Toplevel()
    top.title("VERIFICATION")
    top.geometry("300x100")
    top.resizable(0,0)
    lbl=Label(top, text="Enter Your Name", fg='blue', font=("Helvetica", 9))
    lbl.place(x=80,y=0)
    txtfld=Entry(top, text="This is Entry Widget", bd=5)
    txtfld.place(x=80, y=25)
    def close():
        name = txtfld.get()
        attended = -1
        try:
            attended=int(df.loc[df['Name']==name,'Total_Classes_Attended'])
        except:
            print("")
        if(attended == -1):
            messagebox.showinfo("Error","Name NOT Found")
        else:
            global Total_classes
            numerator= str(attended)
            denominator=str(Total_classes)
            string=name + " : " +numerator + " clases attended out of " +denominator + " classes."
            messagebox.showinfo("Information",string)
    btn=Button(top, text="OK", fg='blue',command=close)
    btn.place(x=100,y=50)
def open4():
    b=False
    top = Toplevel()
    top.title("VERIFICATION")
    top.geometry("300x100")
    lbl=Label(top, text="Enter Admin Password", fg='red', font=("Helvetica", 9))
    lbl.place(x=80,y=0)
    txtfld=Entry(top, show='*',text="This is Entry Widget", bd=5)
    txtfld.place(x=80, y=25)
    passwd=""
    def close():
        passwd=txtfld.get()
        if(passwd==password):
            b=True
            for i in range(Roll_Count):
                ar[i]=False
                df.loc[df['Roll_No.'] == i+1 , 'Total_Classes_Attended'] =0
            #Total_classes+=1
            global Total_classes
            Total_classes=0
            file1=file1 = open("Total_attendance.txt","w")
            file1.write(str(Total_classes))
            file1.close()
            df.to_csv(r'Attendances.csv',index=False)
            
        print("CLOSE"+passwd)
        txtfld.delete(0,'end')
        top.destroy()
    btn=Button(top, text="OK", fg='blue',command=close)
    btn.place(x=100,y=50)
        
btn1=Button(window, text="Give Attendance", fg='blue',command=open1)
btn1.place(x=300, y=200)
btn2=Button(window, text="See Your Attendance", fg='blue',command=open3)
btn2.place(x=100, y=200)
btn3=Button(window, text=" SaveData and Refresh ", fg='blue',command=open2)
btn3.place(x=300, y=250)
btn4=Button(window, text=" RESET ALL ", fg='blue',bg='red',command=open4)
btn4.place(x=100, y=250)
lbl=Label(window, text="Facial Attendance System", fg='red', font=("Helvetica", 16))
lbl.place(x=150, y=50)
window.mainloop()