from tkinter import *

root = Tk()
root.title('Peer Engagement')
root.geometry("600x200")

frame = Frame(root)
frame.pack(pady=32, padx=32)

def c1_selected():
    if var1.get() == 1: c1["fg"] = 'gray'
    else: c1["fg"] = 'black'

def c2_selected():
    if var2.get() == 1: c2["fg"] = 'gray'
    else: c2["fg"] = 'black'

def c3_selected():
    if var3.get() == 1: c3["fg"] = 'gray'
    else: c3["fg"] = 'black'

def c4_selected():
    if var4.get() == 1: c4["fg"] = 'gray'
    else: c4["fg"] = 'black'


var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()

c1 = Checkbutton(frame, text='Reply to all comments on last tweet', variable=var1, onvalue=1, offvalue=0, command=c1_selected)
c1.pack(anchor="w")
c2 = Checkbutton(frame, text='Give 1 comment + 1 share to all who commented me', variable=var2, onvalue=1, offvalue=0, command=c2_selected)
c2.pack(anchor="w")
c3 = Checkbutton(frame, text='Give 3 likes + 1 comment to peers for 20 mins', variable=var3, onvalue=1, offvalue=0, command=c3_selected)
c3.pack(anchor="w")
c4 = Checkbutton(frame, text='Give 1 like + 1 reply to comments in notifications for 20 minutes', variable=var4, onvalue=1, offvalue=0, command=c4_selected)
c4.pack(anchor="w")

btn = Button(frame, text="Victory")
btn.pack()

root.mainloop()