from urllib.parse import  urlsplit, parse_qs
from urllib  import request
from bs4 import BeautifulSoup
import re
import urllib.error
import requests
from tkinter import *
import socket 
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time
import datetime
import validators
import ReportGenerate 
import SqlInjection
import BlindSqlInjection
import BrokenAuthentication
from webbrowser import open_new_tab
import StoreXssModule
import PortScanning
from pprint import pprint
from urllib.parse import urlparse


class Main():

        def __init__(self,root):
                self.root=root
                self.root.geometry("800x480+0+0")
                self.root.title("Web Application Testing ")
                self.root.configure(bg='#324857')
                self.check = False
                
                title=Label(self.root, text="WEB APPLICATION PENETRATION TESTING",width="400",height="3", font=("times new roman", 20,"bold"),bg="#86d2d9").pack()


                name=Label(self.root, text="Enter the Website URL Here", font=("times new roman", 15,"bold"),bg="#c0d67c").place(x=270,y=150)
                self.txt_name=Entry(self.root,font=("times new roman", 15),bg="white")
                self.txt_name.place(x=200,y=190,width=400)

                select_name=Label(self.root, text="Select the Vulnerablity to Test the URL", font=("times new roman", 15,"bold"),bg="#c0d67c").place(x=230,y=240)
                self.cmb_vulnerablity=ttk.Combobox(self.root,font=("times new roman", 15), state="readonly",justify="center")
                self.cmb_vulnerablity['values']=("Select","Sql Injection","Blind Sql Injection","Port Scanning","Cross Site Scripting","Broken Authentication")
                self.cmb_vulnerablity.place(x=200,y=280,width=400)
                self.cmb_vulnerablity.current(0)
                
                btn=Button(self.root, text="Scan it", font=("times new roman", 15,"bold"),cursor="hand2", fg="black", command = self.scan)
                btn.place(x=100,y=350,width=280)
                btn1=Button(self.root, text="Generate Report", font=("times new roman", 15,"bold"),cursor="hand2", fg="black", command=self.Report )
                btn1.place(x=420,y=350,width=280)        

        
        def scan(self):
                self.check=False
                if self.txt_name.get() ==  "":
                        messagebox.showerror("Erorr","Enter the Website to Scan it, try again")

                elif self.cmb_vulnerablity.get() == "Select":
                        messagebox.showerror("Erorr","Select the Vulnerability, try again")

                elif self.cmb_vulnerablity.get() == "Sql Injection":
                        url=self.txt_name.get()
                        print(url)
                        if "http" in url or "https" in url:
                                self.check=True
                                self.sqlflag,self.vul,self.sqllink=SqlInjection.scan_sql_injection(url)
                                if(self.sqlflag):
                                        messagebox.showinfo("Success","Vulnerability Found Generate the Report")
                                else:
                                        messagebox.showerror("Error", "Vulnerability Not Found,Not Generate the Report")
                                print(self.sqlflag)
                                print(self.vul)
                                print(self.sqllink)
                        else:
                                messagebox.showerror("Erorr","Enter Valid Url with Http/Https")
                        
                elif self.cmb_vulnerablity.get() == "Blind Sql Injection":
                        url=self.txt_name.get()
                        print(url)
                        if "http" in url or "https" in url:
                                self.check=True
                                self.bsqlflag,self.bsqllink,self.responsetime=BlindSqlInjection.check_url(url)
                                if(self.bsqlflag):
                                        messagebox.showinfo("Success","Vulnerability Found Generate the Report")
                                else:
                                        messagebox.showerror("Error", "Vulnerability Not Found,Not Generate the Report")
                                print(self.bsqlflag)
                                print(self.bsqllink)
                                print(self.responsetime)
                        else:
                                messagebox.showerror("Erorr","Enter Valid Url with Http/Https")
                        
                elif self.cmb_vulnerablity.get() == "Port Scanning":
                        input = self.txt_name.get()
                        parsed = request.urlparse(input)
                        if ("www." in parsed.netloc):
                                url = parsed.netloc
                        else:
                                url = "www." + parsed.netloc
                        if url != None:
                                self.check=True
                                self.portlist =[]
                                self.portflag, self.portlist=PortScanning.run_scanner(input)
                                if (self.portflag):
                                        messagebox.showinfo("Success", "Vulnerability Found Generate the Report")
                                else:
                                        messagebox.showerror("Error", "Vulnerability Not Found,Not Generate the Report")
                                print(self.portlist)
                        else:
                                messagebox.showerror("Erorr","Failed to get the host name, Enter url in this way www.example.com")

                elif self.cmb_vulnerablity.get() == "Cross Site Scripting":
                        url = self.txt_name.get()
                        if ("https" in url or "http" in url):
                                parsed = request.urlparse(url)
                                if ("https" in parsed.scheme or "http" in parsed.scheme):
                                        print(parsed.scheme + "://" + parsed.netloc)
                                        input = parsed.scheme + "://" + parsed.netloc
                                else:
                                        print("http://" + parsed.netloc)
                                        input = "http://" + parsed.netloc
                        else:
                                parsed = request.urlparse("http://" + url)
                                if ("https" in parsed.scheme or "http" in parsed.scheme):
                                        print(parsed.scheme + "://" + parsed.netloc)
                                        input = parsed.scheme + "://" + parsed.netloc
                                else:
                                        print("http://" + parsed.netloc)
                                        input = "http://" + parsed.netloc
                        if input != None:
                                self.check=True
                                self.xssflag,self.xssform,self.script = StoreXssModule.scan_xss(input)
                                if(self.xssflag):
                                        messagebox.showinfo("Success","Vulnerability Found Generate the Report")
                                else:
                                        messagebox.showerror("Error", "Vulnerability Not Found,Not Generate the Report")
                                print(self.xssflag,self.xssform,self.script)
                        else:
                                messagebox.showerror("Erorr","Enter Valid Url with Http/Https")

                elif self.cmb_vulnerablity.get() == "Broken Authentication":
                        url=self.txt_name.get()
                        print(url)
                        if "http" in url or "https" in url:        
                                self.check=True
                                BrokenAuthentication.Broken_Authentication(url)
                                messagebox.showinfo("Title", "To check Your Vulnerable to Broken Authetication use this payload to Bypass it ' or 1=1 --  this on Login page of Website.")
                        else:
                                messagebox.showerror("Erorr","Enter Valid Url with Http/Https")
        
        
        def Report(self):
                self.Reportpaths = "C:/Users/adnan/Downloads/WAPT/Report.html"
                self.Filepaths ="C:/Users/adnan/Downloads/WAPT"
                if self.check and self.txt_name != "":
                        if(self.check and self.cmb_vulnerablity.get() == "Sql Injection"):
                                print(self.sqlflag,self.vul,self.sqllink)
                                if(self.check):
                                        VulCause = "CVE-20: Improper Input Validation"
                                        Solution ="What you should do, to avoid problems, is quite simple: whenever you embed a string within foreign code, you must escape it, according to the rules of that language. For example, if you embed a string in some SQL targeting MySQL, you must escape the string with MySQL's function for this purpose (mysqli_real_escape_string). (Or, in case of databases, using prepared statements are a better approach, when possible.)"
                                        Description="When Website does not validate input properly, an attacker is able to craft the input in a form that is not expected by the rest of the application. This will lead to parts of the system receiving unintended input, which may result in altered control flow, arbitrary control of a resource, or arbitrary code execution."
                                else:
                                        VulCause="Not Found"
                                        Solution="Not Found"
                                        Description="Not Found"

                                parsed = request.urlparse(self.sqllink)
                                Filename=parsed.netloc
                                Time= datetime.datetime.today().strftime("%B %d %Y %H:%M:%S")
                                index = open(self.Reportpaths).read().format(
                                        Target_url=Filename,Time=Time,Vulnerability_Name=self.cmb_vulnerablity.get(),Status=self.sqlflag ,VulnerabilityCause=VulCause,      
                                        VulnerabilityDescription=Description,VulnerableSol=Solution, VulnerableUrl=self.sqllink)
                                file=Filename+".html"
                                Path=self.Filepaths+file
                                f=open(Path,"w")
                                f.write(index)
                                f.close()
                                open_new_tab(Path)

                        elif(self.check and self.cmb_vulnerablity.get() == "Blind Sql Injection"):
                                print(self.bsqlflag,self.bsqllink,self.responsetime)
                                if(self.check):
                                        VulCause = "CVE-2019-10763 Time based or Error based sql injection"
                                        Solution ="Use secure coding practices, independent on the language. All common web development platforms (including of course PHP, Java, and ASP.NET but also Ruby or Python) have mechanisms that you can use to avoid SQL Injection vulnerabilities including Blind SQL Injections. Avoid dynamic SQL at all costs.The best choice is to use prepared statements also known as parameterized queries.You can also use stored procedures if your SQL database supports them (most databases do, for example, MySQL, Oracle, MS SQL Server, PostgreSQL)."
                                        Description="Time-based SQL Injection is an inferential SQL Injection technique that relies on sending an SQL query to the database which forces the database to wait for a specified amount of time (in seconds) before responding. The response time will indicate to the attacker whether the result of the query is TRUE or FALSE, In the case of Time-based Blind SQLi, the attacker injects an SQL command that caused a delay (for example, SLEEP) and sees if the page is displayed with the delay."  
                                else:
                                        VulCause="Not Found"
                                        Solution="Not Found"
                                        Description="Not Found"

                                parsed = request.urlparse(self.bsqllink)
                                Filename=parsed.netloc
                                Time= datetime.datetime.today().strftime("%B %d %Y %H:%M:%S")
                                index = open(self.Reportpaths).read().format(
                                        Target_url=Filename,Time=Time,Vulnerability_Name=self.cmb_vulnerablity.get(),Status=self.bsqlflag ,VulnerabilityCause=VulCause,      
                                        VulnerabilityDescription=Description,VulnerableSol=Solution, VulnerableUrl=self.bsqllink)
                                file=Filename+".html"
                                Path=self.Filepaths+file
                                f=open(Path,"w")
                                f.write(index)
                                f.close()
                                open_new_tab(Path)


                        elif(self.check and self.cmb_vulnerablity.get() == "Port Scanning"):
                                if(len(self.portlist)!=0):
                                        if(self.check):
                                                VulCause = "CVE-2020-4062 installation of the Conjur Postgres database with an open port"
                                                Solution ="Attackers use open ports to find potential exploits. To run an exploit, the attacker needs to find a vulnerability To find a vulnerability, the attacker needs to fingerprint all services that run on a machine, including what protocols it uses, which programs implement them, and ideally the versions of those programs. "
                                                Description="In security parlance, the term open port is used to mean a TCP or UDP port number that is configured to accept packets. In contrast, a port which rejects connections or ignores all packets directed at it is called a closed port."
                                        else:
                                                VulCause="Not Found"
                                                Solution="Not Found"
                                                Description="Not Found"


                                        Filename=self.txt_name.get()
                                        Time= datetime.datetime.today().strftime("%B %d %Y %H:%M:%S")
                                        index = open(self.Reportpaths).read().format(
                                                Target_url=Filename,Time=Time,Vulnerability_Name=self.cmb_vulnerablity.get(),Status=self.portlist ,VulnerabilityCause=VulCause,      
                                                VulnerabilityDescription=Description,VulnerableSol=Solution, VulnerableUrl=self.txt_name.get())
                                        file=Filename+".html"
                                        Path=self.Filepaths+file
                                        f=open(Path,"w")
                                        f.write(index)
                                        f.close()
                                        open_new_tab(Path)
                                        
                                else:
                                        messagebox.showerror("Error","Vulnerability Not Found try again")         
                        elif(self.check and self.cmb_vulnerablity.get() == "Broken Authentication"):
                                messagebox.showerror("Scuccess","No need to Generate the Broken Authentication")
                        
                        elif(self.check and self.cmb_vulnerablity.get() == "Cross Site Scripting"):
                                if(self.check):
                                        VulCause = "CVE-2020-5842 Stored XSS Vulnerability"
                                        Solution ="XSS attack is a type of code injection: user input is mistakenly interpreted as malicious program code. In order to prevent this type of code injection, secure input handling is needed. For a web developer, there are two fundamentally different ways of performing secure input handling:  Encoding, which escapes the user input so that the browser interprets it only as data, not as code.   Validation, which filters the user input so that the browser interprets it as code without malicious commands."
                                        Description="In most modern web applications, user input is handled by both server-side code and client-side code. In order to protect against all types of XSS, secure input handling must be performed in both the server-side code and the client-side code.In order to protect against traditional XSS, secure input handling must be performed in server-side code. This is done using any language supported by the server."
                                else:
                                        VulCause="Not Found"
                                        Solution="Not Found"
                                        Description="Not Found"

                                parsed = request.urlparse(self.txt_name.get())
                                Filename=parsed.netloc
                                Time= datetime.datetime.today().strftime("%B %d %Y %H:%M:%S")
                                index = open(self.Reportpaths).read().format(
                                        Target_url=Filename,Time=Time,Vulnerability_Name=self.cmb_vulnerablity.get(),Status=self.xssflag ,VulnerabilityCause=VulCause,      
                                        VulnerabilityDescription=Description,VulnerableSol=Solution, VulnerableUrl=self.xssform)
                                file=Filename+".html"
                                Path=self.Filepaths+file
                                f=open(Path,"w")
                                f.write(index)
                                f.close()
                                open_new_tab(Path)
                        else:
                                messagebox.showerror("Error","No Match Found")
                else:
                        messagebox.showerror("Error","You can't Generate the Report Before the Scan it")



                        

                

                

                        

