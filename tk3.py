from tkinter import *
from tkinter import ttk,messagebox

GUI = Tk()
GUI.geometry('500x300')

L1 = Label(GUI,text='แดงสสุดยอดเลย',font=('Angsana new',20,'bold'),fg='red').pack()
L2 = Label(GUI,text='กรุณากรอกจำนวนทุเรียน',font=('Angsana new',20))

V = StringVar()
E1 = ttk.Entry(GUI,textvariable=V,font=('impact',30,)).pack()

def Calculate(event=None):
    Q = V.get()
    price = 100
    print('จำนวน',float(Q)*price)
    cal = float(Q)*price
    #EN DATE
    #stamp = datatime.now().strftime('%Y-%m-%H-%M-%S')

    #writetext(Q,cal)
    data = [timestamp(), Q,cal]
    writecsv(data)

    title = 'ยอดสรุปรวมทั้งหมด'
    text = 'ทุเรียนจำนวน {} กก. ราคาทั้งหมด: {:,.2f} บาท'.format(Q,cal)
    messagebox.showinfo(title,text)


    V.set('')#clear data
    E1.focus()
    
B1 = ttk.Button(GUI,text='คำนวน',command=Calculate)
B1.pack(ipadx=30,ipady=20,pady=20)

E1.bind('<Return>', Calculate)

def SummaryData(event):
    # pop up
    sm = sumdata()
    title = 'ยอดสรุปรวมทั้งหมด'
    text = 'จำนวนที่ขายได้ {} กก.\n ยอดขาย: {:,.2f} บาท'.format(sm[0],sm[1])
    messagebox.showinfo(title , text)

GUI.bind('<F1>',SummaryData)

E1.focus()#ให้ cursor ไปยังตำแหน่งของ E1
GUI.mainloop()
