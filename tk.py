from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk

GUI = Tk()
GUI.title('มาเขียนโปราแกรมกันเถอะ')
GUI.geometry('500x500')
img = Image.open('ส้มcartoon.jpg')
img2 = ImageTk.PhotoImage(img)
lbl = Label(image=img2).pack()


L1 = Label(GUI,text='ทานผลไม้กัน',font=('Angsana new',20),fg='green').pack()
L2 = Label(GUI,text='ต้องการผลไม้กี่ กิโลกรัม',font=('Angsana new',20),fg='blue').pack()

V = StringVar()
E = ttk.Entry(GUI,textvariable=V).pack(ipadx=10,ipady=10,pady=10)

def C():
	Q = V.get()
	price = 100
	print('จำนวน',float(Q)*price)
	cal = float(Q)*price
	messagebox.showinfo('ราคาที่ต้องจ่ายทั้งหมด','จำนวน {} กิโลกรัม ราคาทั้งหมด :{:,.2f}บาท'.format(Q,cal))

B = Button(GUI,text='เก็บข้อมูล',font=('Angsana new',20),fg='green',command=C).pack()

GUI.mainloop()