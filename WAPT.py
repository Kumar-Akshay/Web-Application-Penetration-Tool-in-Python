from tkinter import *
from Register import Register
from Login import Login

def register():
    screen.destroy()
    root=Tk()
    obj=Register(root)
    root.mainloop()    

def login():
    screen.destroy()
    root2=Tk()
    obj=Login(root2)
    root2.mainloop()

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("900x500+0+0")
    screen.configure(bg='#324857')
    screen.title("Web Application Penetration Testing Tool")

    Label(text = "WELLCOME TO WEB APPLICATION PENETRATION TESTING TOOL",bg="#86d2d9", width="400",height="3",font = ("Calibri",20,"bold")).pack()
    btn=Button(text= "Login Here", height = "3", width ="30", font = ("Calibri",15,"bold") ,bg="green",fg="white", command = login)
    btn.place(x=80, y=200)
    btn1=Button(text= "Register Here", height = "3", width ="30", font = ("Calibri",15,"bold"),bg="green",fg="white", command = register)
    btn1.place(x=460, y=200)
    label = Label(text="What is WAPT?" ,bg="#c0d67c",font = ("Calibri",15,"bold"))
    label.place(x=100,y=350)
    label1 = Label(text="Web Applicaiton Peneration Tools which different Vulnerability to Test Website," ,bg="#324857",fg="white",font = ("Calibri",15))
    label1.place(x=100,y=400)
    label1 = Label(text="Like Sql Injection,Blind Injection, Cross-Site Scripting and Port Scanning," ,bg="#324857",fg="white",font = ("Calibri",15))
    label1.place(x=100,y=430)

    screen.mainloop()

main_screen()