# readjon.py

import json
def readjson():
	with open('data.json',encoding='utf-8') as file:
		data = json.load(file)
		print(type(data))
		print(data[0])
	return data

def writejson(data):
	jsonobject = json.dumps(data,ensure_ascii=False,indent=4)
	with open('data.json','w',encoding='utf-8')as file:
		file.write(jsonobject)

data = {'112341234':['Banana',100,5],
		'112341235':['Durian',150,99],
		'112341237':['แก้วมังกร',500,20]}

writejson(data)