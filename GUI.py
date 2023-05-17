#!/usr/bin/env 
from tkinter import *
from tkinter import messagebox
from Tester import Tester
import sys
import io
import threading
import ping3
import re
import os


BACKGROUND_COLOR = '#DDDDDD'
ITEM_COLOR = 'white'

if os.geteuid() != 0:
    messagebox.showwarning("Warning", "You have to execute this script as administrator")
    exit()

class PingThread(threading.Thread):
    def __init__(self, url, count):
        threading.Thread.__init__(self)
        self.url = url
        self.count = count

    def run(self):
        t.configure(state='normal')
        t.insert(END, f"Pinging {self.url} -- {self.count} times\n")
        t.configure(state='disabled')
        success = 0
        failed  = 0
        for i in range(1, self.count+1):
            ping_time = ping3.ping(self.url)
            if ping_time is not None:
                message = f"Ping {i} : {ping_time:.2f} ms\n"
                success = success+1
            else:
                message = f"Ping {i} : Timeout\n"
                failed = failed+1
            t.configure(state='normal')
            t.insert(END, message)
            t.see(END)
            t.configure(state='disabled')
        t.configure(state='normal')
        t.insert(END,f"{self.count} packets transmitted, {success} received, ")
        t.insert(END, f"{(failed / self.count) * 100}% packet loss\n")
        t.configure(state='disabled')
        bouton.config(state='active')

def Submit(url):
    # Rediriger la sortie standard vers le buffer de texte
    text_buffer = io.StringIO()
    sys.stdout = text_buffer
    if len(url) == 0:
        my_entry.config(highlightthickness=2, highlightbackground="red")
    else:
        my_entry.config(highlightthickness=0, highlightbackground="red")
        method = var.get()
        if(method == 1):
            # Appeller la fonction "connectREQUEST" pour etablir une connexion au site de l'user en fesant des requetes
            connection = agent.connectREQUEST(url, 10)
            response_code, response_time = connection
            if(response_code == 200):
                t.configure(state='normal')
                t.insert(END, f"[ok][{'{:.2f}'.format(response_time)}s] {url} -- Working well -- Response code: {response_code}\n", "green")
                t.tag_config("green", foreground="green") # Configure le tag "red" pour la couleur vert
                t.configure(state="disabled")
            else:
                t.configure(state='normal') 
                t.insert(END, f"[!] -- Response code: {response_code}\n", "red")
                t.tag_config("red", foreground="red") # Configure le tag "red" pour la couleur rouge
                t.configure(state="disabled")
        elif(method == 2):
            url = str(url)
            # Verifier avec re, pour savoir s'il y a ecrit http, ou https, au debut du lien de l'user
            p = '(?:http.*://)?(?P<host>[^:/ ]+).?(?P<port>[0-9]*).*'
            # Rechercher s'il y a un http, ou https
            p = re.search(p,url)
            # Rechercher l'host
            p = p.group('host')
            bouton.config(state='disabled')
            ping_thread = PingThread(p, 4)
            ping_thread.start()

# Create the window
window = Tk()
agent = Tester()

# Custom the window 
window.title("WebTesterX")
window.geometry("1080x800")
window.resizable(0,0)
window.config(bg=BACKGROUND_COLOR)

# Title
Label_type = Label(window, text="Welcome to WebTesterX", bg=BACKGROUND_COLOR, font=("Arial", 20))
Label_type.pack()

# Text Credits
Label_type = Label(window, text="Created by Mael and Amaury, 2nd SN, ALL RIGHTS RESERVED.", bg=BACKGROUND_COLOR, font=("Arial", 10))
Label_type.pack(side='bottom')

# Left frame 
frame = Frame(window, bg=BACKGROUND_COLOR)
frame.pack(side=LEFT, padx=50)
frameresult = LabelFrame(window, bg=BACKGROUND_COLOR, text="Results: ")
frameresult.pack(side=RIGHT)
#resultat
t = Text(frameresult, height= 40, width= 80, state='disabled')
t.pack(side=RIGHT,padx=20)
t.configure(state='normal')
t.insert(END, """
__        __   _   _____         _             __  __
\ \      / /__| |_|_   _|__  ___| |_ ___ _ __  \ \/ /
 \ \ /\ / / _ \ '_ \| |/ _ \/ __| __/ _ \ '__|  \  / 
  \ V  V /  __/ |_) | |  __/\__ \ ||  __/ |     /  \ 
   \_/\_/ \___|_.__/|_|\___||___/\__\___|_|    /_/\_\ \n
""")
t.insert(END,"Developped by Hoag and Eagle_\n", 'green')
t.insert(END,"2nd Systèmes Numériques | Saint Aspais Melun(77)\n", 'green')
t.insert(END,"Version: Stable -- 1.0\n", "orange")
t.insert(END, "----------------------------------------------------------------\n")

t.tag_config("green", foreground="green")
t.tag_config("orange", foreground="orange")
t.configure(state='disabled')

Label(frame, text="URL: ", bg=BACKGROUND_COLOR).pack()
my_entry = Entry(frame, width=35, text="URL")
my_entry.pack()
my_entry.bind('<Return>',lambda event:Submit(my_entry.get()))

frame2 = LabelFrame(frame, bg = BACKGROUND_COLOR, text = 'method')
frame2.pack(fill=X)
var = IntVar()
var.set(1)

choix1 = Radiobutton(frame2, text = "Requests -- (Timeout: 10s)", value=1, variable = var, bg = BACKGROUND_COLOR).pack()
choix2 = Radiobutton(frame2, text = "Ping -- (Default: 4)", value=2, variable = var, bg = BACKGROUND_COLOR).pack()

bouton=Button(frame, text="submit", command=lambda: Submit(my_entry.get()), width=25)
bouton.pack(padx=0, pady=0, fill=X)
# afficher
window.mainloop()