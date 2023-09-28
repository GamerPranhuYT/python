#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 20:15:23 2023

@author: Pranshu
"""

from tkinter import *
root = Tk()
root.title("Fibonacci")
root.geometry("400x400")

input_box = Entry(root)

label = Label(root, text = "Fibonacci series")
label2 = Label(root, text= "Fibonacci sum: ")
    

def Fibonacci():
    num = int(input_box.get())
    first_no = 0
    second_no = 1
    sum = 0
    sum2 = 0
    counter = 1
    while(counter <= num):
      label["text"]+=str(sum)
      label2["text"]="Fibonacci sum: "+str(sum2)
      counter = counter + 1
      first_no = second_no
      second_no = sum
      sum = first_no + second_no
      sum2 = sum2 +sum
      
btn = Button(root,text = "show fibonacci", command = Fibonacci, fg="white", bg="dark blue")

input_box.pack()
btn.pack()
label.pack()
label2.pack()

root.mainloop()