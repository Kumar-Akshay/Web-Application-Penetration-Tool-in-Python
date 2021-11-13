from urllib.parse import urlsplit, parse_qs
from urllib  import request
from bs4 import BeautifulSoup
import re
import urllib.error
import requests





class SqlInjection_Detect:
        Error = []
        
        def __init__(self):
                self.Error.append("You have an error in your SQL syntax")
                self.Error.append("Warning: mysql_fetch_array()")
                self.Error.append("warning: mysql_fetch_array()")
                self.Error.append("already has more than 'max_user_connections")
                self.Error.append("supplied argument is not a valid MySQL MySQL Injection")
                self.Error.append("you have an error in your SQL syntax")
                self.Error.append("you have an error in your sql syntax")
                self.Error.append("expects parameter 1 to be resource, boolean given in")
                self.Error.append("unclosed quotation mark after the character string")
        
################################################################################################################################
#Spider The Urls
################################################################################################################################
        def SpiderWebsiteParameter(self,url):
                links = []
                char1 = set('?=')
                parsed = request.urlparse(url)
                DomainName=parsed.netloc
                html_page = urllib.request.urlopen(url)
                soup = BeautifulSoup(html_page,'lxml')
                for link in soup.findAll('a', href=True):
                        str1=link.get('href')
                        if any((c in char1 ) for c in str1):
                                links.append(DomainName+"/"+str1)
                                print(str1)
                        
                Count= len(links) 
                print(Count)
                return links
        

################################################################################################################################
#apply Injection Payload
################################################################################################################################
        
        def SqlInjection (self,url):
            if "'" not in url:
                url = url +"'"
                Vul = self.Vulnerable(url)  
                #print(length)
                if not Vul:
                        if '"' not in url:
                                url = url +'"'
                                Vul1 = self.Vulnerable(url) 
                 #               print(length) 
                                if not Vul1:
                                        if "\\" not in url:
                                                url = url +"\\"
                                                Vul2 = self.Vulnerable(url)
                #                               print(length)
                                                if not Vul2:
                                                        print("It seems Not Vulnerable")       
                                else:
                                        print("It seems Not Vulnerable")
                else:
                        print("It seems Not Vulnerable")
                
                return Vul
        
################################################################################################################################
#       if Url is Vulnerable
################################################################################################################################
        def Vulnerable(self,url):    
                try:
                        count=2
                        VulUrls = []
                        checkstatus = urllib.request.urlopen(url).getcode()
                        if(checkstatus==200):
                                print(url)
                                Web =  urllib.request.urlopen(url)
                                data = Web.read().decode('iso-8859-1')                
                                if data != None:
                                        for e in self.Error:
                                                if e in data:
                                                        print ("[*] SQL  error in the original URL/website found.")
                                                        print ("[*] There might be problems exploiting this website  (if it is vulnerable).")
                                                        VulUrls.append(url)
                                                        break                 
                        else:
                                print("[*] Url Not Loaded")
                        
                        return VulUrls
                except:
                        urllib.error.URLError.reason; 
                        
################################################################################################################################
#Check Urls
################################################################################################################################

        def CheckUrl(self,urls):
                try:
                        url=urls.replace(" ","%20")
                        if url is None:
                                pass
                        elif url is not None:
                                parsed = request.urlparse(url)
                                protocol= parsed.scheme   #check site protocol http or https
                        if protocol == "":
                                url = "http://" + url
                                status1=urllib.request.urlopen(url).getcode()
                                if (status1 != 200):
                                        url.replace("http://","https://")
                                        status2=urllib.request.urlopen(url).getcode()
                                        if(status2==200):
                                             Vul=self.SqlInjection(url)     
                                if(status1==200):
                                        Vul=self.SqlInjection(url) 
                        else:
                                Vul=self.SqlInjection(url)                                    
                except:
                        print(url)
                        print("[*] Url Not Found Try Again")
        
        
        

################################################################################################################################
# Creating Instance and calling function
################################################################################################################################


#http://www.asfaa.org/members.php?id=2
#http://www.imagesystems.com.mt/index.php?id=10
#http://asfaa.org/publications.php?id=2


Obj = SqlInjection_Detect();
url = "http://www.asfaa.org/members.php"
links = Obj.SpiderWebsiteParameter(url)
for item in links:
        print(item)
        Obj.CheckUrl(item)
        break

        
         














































                        
                        



        











