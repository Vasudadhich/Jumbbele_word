
from tkinter import *
import random
from tkinter import messagebox
answers = [
    "python",
    "java",
    "swift",
    "canada",
    "india",
    "america",
    "london",
]

words = [
    "nptoyh",
    "avja",
    "wfsit",
    "cdanaa",
    "aidin",
    "aiearcm",
    "odnlon",
]
num=random.randrange(0,7,1)
def default():
    global words ,answers,num
    lbl.config(text=words[num])
def rest():
     global words ,answers,num
     num=random.randrange(0,7,1)
     lbl.config(text=words[num])
     e1.delete(0,END)
def checkans():
     global words ,answers,num
     var=e1.get()
     if var == answers[num]:
         messagebox.showinfo("Succes","This is Right Answer")
         rest()
     elif var == "":
        messagebox.showwarning("warning","Enter the String")
     else:
        messagebox.showerror("Wrong","This is wrong answer")
        e1.delete(0,END)
         
         
    
root=Tk()
root.title("Jumbble Word")
root.geometry("350x400+400+300")
root.config(bg="black")
lbl=Label(root,text="Your Here",font=("Verdana",18),bg="black",fg="white")
lbl.pack(pady=30,ipady=10,ipadx=10)
ans=StringVar()
e1=Entry(root,textvariable=ans,font=("Verdana",16))
e1.pack(ipady=5,ipadx=5)
btncheck=Button(root,text="check",font=("Comic sans ms",16),bg="#4C4B4B" ,fg="#6ab04c",command= checkans ,relief=GROOVE,)
btncheck.pack(pady=40)
btnreset=Button(root,text="reset",font=("Comic sans ms",16),bg="#4C4B4B" ,fg="#EA425C" ,command= rest ,relief=GROOVE,)
btnreset.pack()
default()

root.mainloop()
