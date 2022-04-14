import json

def readjson():
	with open('json2.json')as file:
		data = json.load(file)
		print(data[1]['poit'])
	return data

def writejson(data):
	jsonobject = json.dumps(data,indent=4)
	with open('jj.json','w') as file:
		file.write(jsonobject)

data = {'112341234':['Banana',199,5],
		'112341235':['Durian',150,99],
		'112341236':['Apple',200,10],
		'112341237':['แก้วมังกร',300,20]}

writejson(data)