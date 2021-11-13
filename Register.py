from tkinter import *
from tkinter import messagebox
import pymysql
from Login import Login

class Register:
    def __init__(self,root):
        self.root=root
        self.root.geometry("750x400+0+0")
        self.root.title("Registration Here")
        self.root.configure(bg='#324857')
        #Registration ===============
        title=Label(self.root,text = "WELLCOME TO REGISTRATION",bg="#c0d67c", width="400",height="2",font = ("Calibri",20,"bold")).pack()
    
        f_name=Label(self.root, text="First Name", font=("times new roman", 15,"bold"),bg="#c0d67c").place(x=100,y=100)
        self.txt_fname=Entry(self.root,font=("times new roman", 15),bg="white")
        self.txt_fname.place(x=100,y=130,width=250)

        l_name=Label(self.root, text="Last Name", font=("times new roman", 15,"bold"),bg="#c0d67c").place(x=400,y=100)
        self.txt_lname=Entry(self.root,font=("times new roman", 15),bg="white")
        self.txt_lname.place(x=400,y=130,width=250)

        email=Label(self.root, text="Email", font=("times new roman", 15,"bold"),bg="#c0d67c").place(x=100,y=200)
        self.txt_email=Entry(self.root,font=("times new roman", 15),bg="white")
        self.txt_email.place(x=100,y=230,width=250)

        password=Label(self.root, text="Password", font=("times new roman", 15,"bold"),bg="#c0d67c").place(x=400,y=200)
        self.txt_password=Entry(self.root,show="*",font=("times new roman", 15),bg="white")
        self.txt_password.place(x=400,y=230,width=250)

        btn=Button(self.root, text="Register", font=("times new roman", 15,"bold"),cursor="hand2",command=self.Register_data, fg="black").place(x=200,y=300,width=350)


    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_password.delete(0,END)
        

    def Register_data(self):
        if self.txt_fname.get() =="" or self.txt_lname.get()=="" or self.txt_email.get()=="" or self.txt_password.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                conn=pymysql.connect(host="localhost",user="root",password="",database="wapt")
                cur=conn.cursor()
                cur.execute("select * from user where Email=%s",self.txt_email.get())
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already Exist, Please try with another email",parent=self.root)                
                else:
                    cur.execute("insert into user (F_Name,L_Name,Email,Password) values(%s,%s,%s,%s)",
                                (
                                    self.txt_fname.get(),
                                    self.txt_lname.get(),
                                    self.txt_email.get(),
                                    self.txt_password.get()
                                ))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success","Register Successfull",parent=self.root)
                    self.clear()
                    self.root.destroy()
                    root2 = Tk()
                    obj = Login(root2)
                    root2.mainloop()
            except Exception as e:
                    messagebox.showerror("Erorr",f"Error due to:{str(e)}",parent=self.root)
