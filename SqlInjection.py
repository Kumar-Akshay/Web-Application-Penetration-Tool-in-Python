import requests
# import re # uncomment this for DVWA
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
from pprint import pprint

s = requests.Session()
s.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"

def is_vulnerable(response):
    """A simple boolean function that determines whether a page 
    is SQL Injection vulnerable from its `response`"""
    errors = {
        # MySQL
        "You have an error in your SQL syntax",
        "Warning: mysql_fetch_array()",
        "warning: mysql_fetch_array()",
        "already has more than 'max_user_connections",
        "supplied argument is not a valid MySQL MySQL Injection",
        "you have an error in your SQL syntax",
        "you have an error in your sql syntax",
        "expects parameter 1 to be resource, boolean given in",
        "unclosed quotation mark after the character string",
        "you have an error in your sql syntax;",
        "select pagemap, parent, image, redir, template_id from pages where id='2'' and is_published='1'",
        "select pagemap, parent, image, redir, template_id from pages where id='2\' and is_published='1'"
        "warning: mysql",
        # SQL Server
        "unclosed quotation mark after the character string",
        # Oracle
        "quoted string not properly terminated",
    }
    for error in errors:
        # if you find one of these errors, return True
        if error in response.content.decode('iso-8859-1').lower():
            return True
    # no error detected
    return False


def scan_sql_injection(url):
    # test on URL
    parameter = {"'","\\",}
    for c in parameter:
        # add quote/double quote character to the URL
        new_url = f"{url}{c}"
        print("[!] Trying", new_url)
        # make the HTTP request
        res = s.get(new_url)
        if is_vulnerable(res):
            # SQL Injection detected on the URL itself, 
            # no need to preceed for extracting forms and submitting them
            print("[+] SQL Injection vulnerability detected, link:", new_url)
            return True,c,new_url
        else:
            return False,c,url