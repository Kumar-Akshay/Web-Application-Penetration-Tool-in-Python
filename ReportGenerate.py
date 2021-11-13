import time
import datetime
import validators
from webbrowser import open_new_tab
import urllib.error
from urllib  import request




VulStatus = []


def GenerateReport(self):
                url=text1 = self.value.get()
                parsed = request.urlparse(url)
                Filename=parsed.netloc
                print(Filename)

                
                for link in self.VulUrls:
                        print(link)
                        
                VulCause="Not Found"
                Solution="Not Found"
                Description="Not Found"
                print(self.count)
                if(self.count):
                        VulCause = "CVE-20: Improper Input Validation"
                        Solution ="What you should do, to avoid problems, is quite simple: whenever you embed a string within foreign code, you must escape it, according to the rules of that language. For example, if you embed a string in some SQL targeting MySQL, you must escape the string with MySQL's function for this purpose (mysqli_real_escape_string). (Or, in case of databases, using prepared statements are a better approach, when possible.)"
                        Description="When Website does not validate input properly, an attacker is able to craft the input in a form that is not expected by the rest of the application. This will lead to parts of the system receiving unintended input, which may result in altered control flow, arbitrary control of a resource, or arbitrary code execution."
                else:
                        VulCause="Not Found"
                        Solution="Not Found"
                        Description="Not Found"
                        link="Not Found"
                        
                
                
                Time= datetime.datetime.today().strftime("%B %d %Y %H:%M:%S")
                index = open("C:/Users/Akshay Kumar/Desktop/FYP/fYP/Report.html").read().format(
                        Target_url=Filename,Time=Time,Vulnerability_Name='Sql Injection',Count_Vulnerablity=self.count ,VulnerabilityCause=VulCause,      
                        VulnerabilityDescription=Description,VulnerableSol=Solution, VulnerableUrl=link
                        )

                file=Filename+".html"
                Path="C:/Users/Akshay Kumar/Desktop/FYP/fYP/"+file
                f=open(Path,"w")
                f.write(index)
                f.close()

                open_new_tab(Path)        
                
                return