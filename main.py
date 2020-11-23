#Name:- Karthik D
from tkinter import*
import wikipedia
import sys
import requests
import datetime
###################


#########################
root=Tk()
y='#ffc13b'
b='#1e3d59'
o='#ff6e40'
w='#f5f5f5'
fg='courier 12'
######################
global text, st,link
tet =StringVar()#to get city name using tkinter

tet.set('Enter Name to Search')#setting value


#######################################################
def ex():
    sys.exit()
def check():
    global l11, st,tet,link
    try:
        st = wikipedia.summary(tet.get().strip()).split('.')
        sm = ''
        for i in st:
            sm += i.strip() + '.\n'
        l11.delete('1.0', END)
        l11.insert(END, sm)

    except:
        l11.delete('1.0', END)
        l11.insert(END,'Error in Name')





root.config(bg=w)
root.geometry('700x700')
l1=Label(root,text='Wikipedia Using Python',fg=o,relief='flat',font='courier 15',justify='center')
l1.pack(pady=5)
l1=Label(root,bg=b,text=' ',fg=b, width =200,relief='flat',font=fg,justify='center')
l1.pack(pady=5)

l1=Entry(root,bg=y,text=tet,fg=b,relief=FLAT,font=fg,justify='center')
l1.pack(pady=5)
l1=Button(root,bg=y,text='search',activebackground=o,fg=b,relief='ridge',font=fg,justify='center',command=check)
l1.pack(pady=5)
l1=Button(root,bg=y,text='Quit',activebackground=o,fg=b,relief=FLAT,font=fg,justify='center',command=ex)
l1.pack(pady=5)
frame=Frame(root)
frame.pack()
l11 = Text(frame, bg=w, fg=b, relief='flat', font='courier 12')
l11.pack(pady=5)

l1=Label(root,bg=b,text=' ',fg=y, width =200,relief=FLAT,font=fg,justify='center')
l1.pack(pady=5)





root.mainloop()
