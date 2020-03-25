# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 23:06:29 2020

@author: Saurabh
"""
import Face_Recognition as f
def reset():
    f.event1

import tkinter as tk
window=tk.Tk()
window.geometry("500x500")
btn = tk.Button(window,text='RESET',bg="orange", fg="red",command=reset)
btn.grid(column=1000, row=500)
btn.bind(reset)
window.mainloop()
