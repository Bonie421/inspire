from tkinter import *
root = Tk()
def myClick():
    myLabel = Label(root,text = "Hey,did you just clicked me?!!!!")
    myLabel.pack()
myB = Button(root,text="Click Me!!!", command = myClick)
myB.pack()
root.mainloop()