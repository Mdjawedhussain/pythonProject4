from tkinter import *
win = Tk()
win.title("Ratio Calculator")
win.geometry("600x500")
win.resizable(0,0)
#Create text Label for Ratio Calculator
label= Label(win, text="Ratio Calculator", font=('Times New Roman', 25))
#Define the function to calculate the value
def ratio_cal():
   a1=int(a.get())
   b1= int(b.get())
   c1= int(c.get())
   val= (b1*c1)/a1
   x_val.config(text=val)
#Add another frame
frame= Frame(win)
frame.pack()
#Create Spin Boxes for A B and C
a= Spinbox(frame, from_=0, to= 100000, font=('Times New Roman', 14), width=10)
a.pack(side=LEFT,padx=10, pady=10)
b= Spinbox(frame,from_=0, to=100000, font=('Times New Roman', 14), width=10)
b.pack(side=LEFT, padx= 10, pady=10)
c= Spinbox(frame, from_=0, to=100000, font=('Times New Roman', 14), width= 10)
c.pack(side= LEFT, padx=10, pady=10)
x_val= Label(frame, text="",font=('Times New Roman', 18))
x_val.pack(side=LEFT)
#Create a Button to calculate the result
Button(win, text= "Calculate",command=ratio_cal, borderwidth=3, fg="white",
bg="black", width=15).pack(pady=20)
win.mainloop()
