from tkinter import*
root=Tk()


frame=LabelFrame(root,text="This is my frame",padx=10,pady=10)
frame.pack(padx=50,pady=50)
b=Button(frame,text="login")
b.grid(row=0,column=0)
b2=Button(frame,text="register")
b2.grid(row=1,column=1)


root.mainloop()
