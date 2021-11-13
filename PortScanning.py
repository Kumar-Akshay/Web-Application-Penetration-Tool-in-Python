from queue import Queue
import socket
import threading
import urllib.parse


target = "127.0.0.1"
queue = Queue()
open_ports = []


def portscan(port,url):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #s.settimeout(2)
        sock.connect((url, port))
        return True
    except:
        return False

def get_ports():
    for port in range(1, 512):
        queue.put(port)
     
def worker(url):
    while not queue.empty():
        port = queue.get()
        if portscan(port,url):
            #print("Port {} is open!".format(port))
            open_ports.append(port)

def run_scanner(urls):
    try:
        url = socket.gethostbyname(urls)
        print(url)
        threads=200
        get_ports()

        thread_list = []

        for t in range(threads):
            thread = threading.Thread(target=worker,args=(url,))
            thread_list.append(thread)

        for thread in thread_list:
            thread.start()

        for thread in thread_list:
            thread.join()
        if len(open_ports)!=0:
            return True, open_ports
        else:
            return False, open_ports


    except:
        print("failed to get the host name, use www.example.com")
