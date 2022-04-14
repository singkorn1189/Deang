from tkinter import *
from tkinter import ttk,messagebox

GUI = Tk()
GUI.geometry('500x500')
GUI.title('แดงเก่งที่สุด')

L1 = Label(GUI,text='มาเขียนโปรแกรมกันเถอะ',font=('Angsana new',20,'bold'),fg='green').pack()
L2 = Label(GUI,text='กรุณาใส่จำนวนที่ต้องการสั่ง',font=('Angsana new',20),fg='orange').pack()

V = StringVar()
E = ttk.Entry(GUI,textvariable=V,font=('impact',15,)).pack()

def Calcurate():
	C1 = V.get()
	price = 100 
	print('จำนวน',float(C1)*price)
	cal = float(C1)*price
	messagebox.showinfo('ยอดที่ต้องจ่าย','จำนวน กิโลกรับ {} ราคาทั้งหมด:{:,.2f}'.format(C1,cal))

B1 = ttk.Button(GUI,text='ราคาที่ต้องจ่าย',command=Calcurate).pack(ipadx=20,ipady=15,pady=10)
	
GUI.mainloop()