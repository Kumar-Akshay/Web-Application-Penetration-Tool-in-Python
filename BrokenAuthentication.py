from urllib.parse import urlsplit, parse_qs
from urllib  import request
from bs4 import BeautifulSoup
import re
import urllib.error
import requests
from webbrowser import open_new_tab
from tkinter import messagebox


def Broken_Authentication (url):
    user_payload = "' or 1=1 --"
    pass_payload = "' or 1=1 --"
    open_new_tab(url)
    
    
    