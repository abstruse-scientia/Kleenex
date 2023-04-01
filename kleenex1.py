import os
import shutil
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import sys


def get_path(filename):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, filename)
    else:
        return filename



root=Tk()
root.title("Kleenex")
root.geometry('350x500')
directory=os.path.dirname(__file__)
icon='icon1.ico'
path_icon=os.path.join(directory,icon)
root.wm_iconbitmap(get_path(path_icon))
root.resizable(0,0)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)


#Icon and Application Name
img=Image.open(get_path(path_icon))
resize_img=img.resize((60,60))
img2=ImageTk.PhotoImage(resize_img)
img_label=Label(image=img2)
img_label.grid(column=0,row=0,sticky=W)
name=Label(root,text="Kleenex")
name.grid(column=1,row=0,sticky=W)


top_frame=Frame(height=2, width=450, bd=1, relief=SUNKEN)
top_frame.grid(row=1, column=0, columnspan=2, padx=1, pady=1)

target_type=Label(root,text="Target type:")
target_type.grid(row=2,column=0,sticky=W)

text_for_targettype=Label(root,text="Junk Files")
text_for_targettype.grid(row=2,column=1,sticky=W,padx=3,pady=3)

target=Label(root,text="Target:")
target.grid(row=3,column=0,sticky=W)

text_for_target=Label(root,text="Files")
text_for_target.grid(row=3,column=1,sticky=W,padx=3,pady=3)

location=Label(root,text="Location:")
location.grid(row=4,column=0,sticky=W,padx=3,pady=3)

abpath=os.path.abspath(__file__)
e=Entry(root,width=35)
e.grid(row=4,column=1,sticky=W,padx=3,pady=3)
e.insert(0,abpath)

def show_msg(event):
    pathn=e.get()
    if pathn !=abpath:
        messagebox.showerror("Problem with Location","The name specified in Location box is not valid.Make sure the path and filename are correct.")

root.bind('<Return>', show_msg)
middle_frame=Frame(height=2, width=450, bd=1, relief=SUNKEN)
middle_frame.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

start_in=Label(root,text="Start in:")
start_in.grid(row=6,column=0,sticky=W,padx=3,pady=3)

f=Entry(root,width=35)
f.grid(row=6,column=1,sticky=W)
initial_target_path="C:\Windows\Temp"
f.insert(0,initial_target_path)

file_type=Label(root,text="File type:")
file_type.grid(row=7,column=0,sticky=W,padx=3,pady=3)

def combofunction(event):
    s=g.get()
    if s!='All':
        g.set(s)
    m=g.get()
    if m=="Temp":
        path="C:\Windows"
        for i in os.listdir(path):
            if "Temp"==i:
                path_of=os.path.join(path,i)
                f.delete(0,END)
                f.insert(0,path_of)
    elif m=="prefetch":
        path="C:\Windows"
        for i in os.listdir(path):
            if "prefetch"==i:
                path_of=os.path.join(path,i)
                f.delete(0,END)
                f.insert(0,path_of)
    elif m=="%temp%":
        path='C:\\Users'
        for i in os.listdir(path):
            if  i!='Default User'and i!='All Users' and i!='Public' and i!='Default' and i!='desktop.ini':
                path_line=os.path.join(path,i)
                for j in os.listdir(path_line):
                    if j=='AppData':
                        path_line2=os.path.join(path_line,j)
                        for k in os.listdir(path_line2):
                            if k=='Local':
                                path_line3=os.path.join(path_line2,k)
                                for l in os.listdir(path_line3):
                                    if l=='Temp':
                                        path_line4=os.path.join(path_line3,l)
                                        f.delete(0,END)
                                        f.insert(0,path_line4)
    elif m=="All":
        pass       
    else:
        messagebox.showerror("Problem with File type","Enter correct keyword! Keyword list: Temp,prefetch,%temp%,All.Keywords are case sensitive.")
options=['Temp','prefetch','%temp%','All']
g=ttk.Combobox(root,values=options,width=31)
g.grid(row=7,column=1,sticky=W,padx=3,pady=3)
g.current(3)
g.bind('<<ComboboxSelected>>',combofunction)
root.bind('<Return>',combofunction)


  
     


comment=Label(root,text="Comment:")
comment.grid(row=8,column=0,sticky=W,padx=3,pady=3)

h=Entry(root,width=35)
h.grid(row=8,column=1,sticky=W,padx=3,pady=3)
h.insert(0,"Deletes specified junk files")

bottom_frame=Frame(height=2, width=450, bd=1, relief=SUNKEN)
bottom_frame.grid(row=9, column=0, columnspan=2, padx=5, pady=5)


def file_location():
    loc=f.get()
    file_dia=filedialog.askopenfile(initialdir=loc)


def search():
    global path_of_prefetch
    global path_of_appdataTemp
    global path_of_temp
    global l1
    l1=[]
    path_of_temp='C:\Windows\Temp'
    path_of_prefetch='C:\Windows\prefetch'
    path_of='C:\\Users'
    for i in os.listdir(path_of):
        if  i!='Default User'and i!='All Users' and i!='Public' and i!='Default' and i!='desktop.ini':
            path_line=os.path.join(path_of,i)
            for j in os.listdir(path_line):
                if j=='AppData':
                    path_line2=os.path.join(path_line,j)
                    for k in os.listdir(path_line2):
                        if k=='Local':
                            path_line3=os.path.join(path_line2,k)
                            for l in os.listdir(path_line3):
                                if l=='Temp':
                                    path_of_appdataTemp=os.path.join(path_line3,l)
    l1=[path_of_temp,path_of_prefetch,path_of_appdataTemp]
                                    




def optimize():
    search()
    path=f.get()
    input_for_g=g.get()
    if input_for_g =="All":
        for j in l1:
            for thefile in os.listdir(j):
              file_path=os.path.join(j,thefile)
              try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
              except :
                pass
    for thefile in os.listdir(path):
       file_path=os.path.join(path,thefile)
       try:
         if os.path.isfile(file_path):
            os.unlink(file_path)
         elif os.path.isdir(file_path):
            shutil.rmtree(file_path) 
       except Exception as e:
        pass
        
        
        


button1=Button(root,text="File Location",command=file_location)
button1.grid(row=10,column=0,sticky=E,padx=10,pady=10)

button2=Button(root,text="Optimize",command=optimize)
button2.grid(row=10,column=1,padx=10,pady=10)







root.mainloop()