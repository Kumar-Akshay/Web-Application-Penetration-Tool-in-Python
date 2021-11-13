from tkinter import *
from tkinter import messagebox
import pymysql
from MainScreen import Main

class Login:
    def __init__(self,root):
        self.root=root
        self.root.geometry("700x350+0+0")
        self.root.title("Login Here")
        self.root.configure(bg='#324857')

        #Login ===============

        title=Label(self.root,text = "WELLCOME TO LOGIN",bg="#c0d67c", width="400",height="2",font = ("Calibri",20,"bold")).pack()
    
        email=Label(self.root, text="Email", font=("times new roman", 15,"bold"),bg="#c0d67c").place(x=100,y=120)
        self.txt_email=Entry(self.root,font=("times new roman", 15),bg="white")
        self.txt_email.place(x=100,y=160,width=250)

        password=Label(self.root, text="Password", font=("times new roman", 15,"bold"),bg="#c0d67c").place(x=400,y=120)
        self.txt_password=Entry(self.root,font=("times new roman", 15),show="*",bg="white")
        self.txt_password.place(x=400,y=160,width=250)

        btn=Button(self.root, text="Sign in", font=("times new roman", 15,"bold"),command=self.check_user ,fg="black",bg="white").place(x=200,y=240,width=300)

    def WAPT(self):
        self.root.destroy()
        root2=Tk()
        obj=Main(root2)
        root2.mainloop()   

    def clear(self):
        self.txt_password.delete(0,END)
        self.txt_email.delete(0,END)

    def check_user(self):
        if self.txt_email.get()=="" or self.txt_password.get()=="":

            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                conn=pymysql.connect(host="localhost",user="root",password="",database="wapt")
                cur=conn.cursor()
                cur.execute("select * from user where Email=%s and Password=%s",(self.txt_email.get(),self.txt_password.get()))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showinfo("Success","Login Successfull",parent=self.root)
                    self.clear()
                    self.WAPT()
                else:
                    messagebox.showerror("Error","User Not Found, Try again ",parent=self.root)
                    self.clear()
                conn.close()
            except Exception as e:
                messagebox.showerror("Erorr",f"Error due to:{str(e)}",parent=self.root)


