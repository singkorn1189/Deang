from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk

root=Tk()
root.title('My GUI')
''
root.geometry('500x600')

img = Image.open('ผลไม้รวม.jpg')
img =img.resize((int(img.width *.7),int(img.height *.7)))
img2 = ImageTk.PhotoImage(img)
lbl = Label(image=img2).pack()


#ใส่ข้อความในหน้าจอ

myLabel1=Label(root,text='สั่งซื้อผลไม้กับเราได้',font=20,fg='red',bg='green').pack(ipadx=10,ipady=10,padx=10,pady=10)
myLabel2=Label(root,text='กรุณาใส่ปริมาณที่ต้องการซื้อ:กก.',font=20,fg='green').pack()

def showmessage():
    message=txt.get()
    print(message)
   
def Calculate(event=None):
    Q = txt.get()
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


def openwindow():
    #หน้าจอที่2
    mywindow=Tk()
    mywindow.title('รายงานแสดงผล')
    mywindow.geometry('300x300')

    L1=Label(mywindow,showmessage(),font=20,fg='green').pack(ipadx=5,ipady=5,padx=5,pady=5)
    L2=Label(mywindow,text='ตกลงสั่งซื้อทุเรียนหรือไม่',font=20,fg='red',bg='green').pack()

    bbn1=Button(mywindow,text='ตกลง',fg='red',bg='pink',command=Calculate).pack(ipadx=10,ipady=10,padx=10,pady=10)
  
#กล่อฃข้อความ
txt=StringVar()
myText=ttk.Entry(root,textvariable=txt).pack(ipadx=10,ipady=10,padx=10,pady=10)


#ใส่ปุ่ม
bbn2=Button(root,text='เปิดรายงาน',font=('Angsana new',20),fg='red',bg='pink',command=openwindow).pack(ipadx=10,ipady=2,padx=10,pady=10)

myText.bind('<Return>',Calculate)

def SummaryData(event):
    # pop up
    sm = sumdata()
    title = 'ยอดสรุปรวมทั้งหมด'
    text = 'จำนวนที่ขายได้: {} กก.\n ยอดขาย: {:,.2f} บาท'.format(sm[0],sm[1])
    messagebox.showinfo(title , text)

#root.bind('<F1>',SummaryData)


'''
def showmessage():
    print('Hello World')
#หน้าจอที่2
'''
root.mainloop()

