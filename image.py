# from tkinter import*
# from pil import Image, ImageTK
# root =Tk()
# def open():
#     global my_img
#     top = Toplevel()
#     my_img=ImageTK.photoimage(Image.open("eaglee.png"))
#     my_label=Label(top,image=my_img)
from tkinter import*
root =Tk()

def show():
    Label(root,text= clicked.get()).pack()

clicked=StringVar()
clicked.set("Sunday")
OptionMenu(root,clicked,"Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday").pack()

btn=Button(root,text="show selection",command=show)
btn.pack()
root.mainloop()
