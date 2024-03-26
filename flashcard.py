import json
import random
import os
from flashcardui import run as runui


def print_filelist(files):
	counter=1
	print("File_List::")
	while counter <= len(files):
		for item in files:
			if int(item) == counter:
				print(item+"."+files[item])
				counter+=1
	
	

def set_default_file():
	cwd = os.getcwd()
	files = json.load(open(cwd+"/Data/filenames.txt"))
	keys = list(files.keys())
	values = list(files.values())
	print_filelist(files)
	select = input("\nSet the default file (0 for new file):")
	if select=="0":
		add_file()
	elif int(select)!=-1 and int(select)<=len(files) and int(select)>=2:
		temp = files["1"]
		files["1"] = files[select]
		files[select] = temp
		print_filelist(files)
		json.dump(files,open(cwd+'/Data/filenames.txt','w'))
	if select=="-1":exit()
	


def delete_file():
	cwd = os.getcwd()
	files = json.load(open(cwd+"/Data/filenames.txt"))
	keys = list(files.keys())
	values = list(files.values())
	counter=1
	os.system("cls")
	print_filelist(files)
	select = input("\nEnter the number of the file to no longer load: ")
	if select!="-1":
		set_erase=0
		for i in range(1,len(files)):
			if files[str(i)] == files[select]:
				set_erase = 1
			if set_erase==1:
				files[str(i)]=files[str(i+1)]
		del files[str(len(files))]
		counter=1
		json.dump(files,open(cwd+"/Data/filenames.txt",'w'))
		
	
		
		
		
				
					


def add_file():
	cwd = os.getcwd()
	files = json.load(open(cwd+"/Data/filenames.txt"))
	keys = list(files.keys())
	values = list(files.values())
	new_file = input("Enter new file: ").replace(".txt","")+".txt"
	k = 1
	while (k==1 and new_file!="-1"):
		try:
			open(cwd+'/Files/'+new_file,"w")
			if (new_file in values or new_file=="filenames.txt" or new_file=="DefaultFile.txt"):
				new_file = input("Enter new file: ")
			else:
				k=0
				myfile = open(cwd+f'/Files/{new_file.replace(".txt","")}.txt', 'w')
				myfile.close()
		except FileNotFoundError:
			k=0
			open(cwd+'/Files/'+new_file,"w")

	number = len(keys)+1
	if new_file!="-1":
		files[number] = f'{new_file.replace(".txt","")}.txt'
		json.dump(files,open(cwd+"/Data/filenames.txt",'w'))
	os.system("cls")
	set_default_file()
		
	


def delete_key():
	cwd = os.getcwd()
	files = json.load(open(cwd+"/Data/filenames.txt"))
	File = files["1"]
	try:fc = json.load(open(cwd+'/Files/'+File))
	except ValueError: return
	keys = list(fc.keys())
	print(keys)
	topic = input("word/topic to delete: ")
	while topic not in keys and topic!="-1":
		topic = input("word/topic to delete: ")
	if topic=="-1":return
	del fc[topic]
	keys = list(fc.keys())
	json.dump(fc,open(cwd+'/Files/'+File,'w'))


def edit_definition():
	cwd = os.getcwd()
	files = json.load(open(cwd+"/Data/filenames.txt"))
	File = files["1"]
	try:fc = json.load(open(cwd+'/Files/'+File))
	except ValueError: exit()
	keys = list(fc.keys())
	print(keys)
	topic = input("word/topic to edit: ")
	while topic not in keys:
		topic = input("word/topic to edit: ")	
	fc[topic] = input("what is the definition: ")
	json.dump(fc,open(cwd+'/Files/'+File,'w'))
	os.system("cls")
	print("updated\n")
	
def add_card():
	cwd = os.getcwd()
	files = json.load(open(cwd+"/Data/filenames.txt"))
	File = files["1"]
	topic = input("what is your word/topic: ")
	definition = input("what is the definition: ")
	try:
		fc = json.load(open(cwd+'/Files/'+File))
	except:
		fc = {}
	fc[topic] = definition
	json.dump(fc,open(cwd+'/Files/'+File,'w'))

def study():
	runui()


		
	

os.system("cls")
set_default_file()
os.system("cls")
ask = 0
while ask !=-1:
	ask = (input("do you want to study(1) or add new cards(2) or exit(-1)\n or edit card(0) or delete card(3) or go back(4) or delete File(5): "))
	while ask not in ['0','1','-1','2','3',"4","5"]:
		os.system("cls")
		print("Incorrect Input")
		ask = input("do you want to study(1) or add new cards(2) or exit(-1)\n or edit card(0) or delete card(3) or go back(4) or delete File(5): ")
	os.system("cls")
	if ask == '1': study()
	if ask == '0': edit_definition()
	if ask == '2': add_card()
	if ask == '3': delete_key()
	if ask =='-1': exit()
	if ask == "4":set_default_file()
	if ask == "5":delete_file() & set_default_file()
	

		
	
	
	
	

