from tkinter import Tk, Label, Button, Entry, Toplevel
import requests 

class Prozor: 
    def __init__(self,master): 
        self.master = master
        self.text_label = Label(master, text= "Enter site URL: ")
        self.text_label.pack() 
        self.url_entry = Entry(master)
        self.url_entry.pack()
        self.convert_btn = Button(master, text= "Convert", command= self.url_enter)
        self.convert_btn.pack(side="left") 
        self.quit_btn = Button(master, text = "Quit", command= self.master.destroy)
        self.quit_btn.pack(side= "right")
        self.master.title("URL to HTML converter")
        self.master.geometry("600x400")

    def url_enter(self): 
        url = self.url_entry.get()
        response = requests.get(url).text
        with open("index.html", "w", encoding="utf-8") as fajl:
            fajl.write(response)

master = Tk() 
prozor = Prozor(master)
master.mainloop() 