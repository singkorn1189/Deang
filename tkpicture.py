from tkinter import *
from PIL import Image, ImageTk

def basic():
	root = Tk()
	root.option_add('*font','consolas 20')
	img = Image.open('ส้ม1ลูก1ซีก.jpg')
	img = img.resize((int(img.width * .3),int(img.height *.3)))
	photo = ImageTk.PhotoImage(img)
	lbl = Label(image=photo).pack()
	Label(root,text='โชว์หน้าจอวินโดวส์').pack()

	root.mainloop()

def adv():
	image = ['ส้ม2ลูก1ซีก','ผลไม้รวม','ผักรวม']
	root = Tk()
	root.option_add('*font','consolas 20')
	img_list = []
	for i,img in enumerate(image):
		img_list.append(ImageTk.PhotoImage(Image.open(f'{img}.jpg')))
		lbl = Label(image=img_list[i]).grid(row=0,column=i)
		Label(root,text=f'{img}.jpg').grid(row=1,column=i)
		

	root.mainloop()

if __name__=='__main__':
	basic()
	#adv()
