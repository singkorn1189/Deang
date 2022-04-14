from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.option_add('*font','consolas 20')
img=Image.open('ส้มcartoon.jpg')#ดึงรูปภาพที่อยู่ในโฟเดอร์เดียวกันออกมา
#img=img.resize((int(img.width * .5),int(img.height * .5)))
photo=ImageTk.PhotoImage(img)
lbl=Label(image=photo)
lbl.pack()
#Label(root,text='มาพิมพ์ดีดกันเถอะ').pack()

root.mainloop()
