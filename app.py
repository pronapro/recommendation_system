import os
import json
import random
from PyPDF2 import PdfFileReader
import subprocess, sys
def read_files(type):
	file_type = type
	if type.lower()  == "pdf":
		extension =".pdf"
	elif type.lower() =="video":
		extension = ".mkv"
	else:
		extension =".htm"

	arr = os.listdir()
	#print(arr)
	#geting there path
	#files_path = [os.path.abspath(x) for x in arr]
	#print(files_path)
	#getting type
# Getting the current work directory (cwd)
	thisdir = "/Users/napro/"
	files =[]
	files_path =[]

	# r=root, d=directories, f = files
	for r, d, f in os.walk(thisdir):
	    for file in f:
	        if file.endswith(extension):
	            files_path.append(os.path.join(r, file))
	            files.append(file)
	file_paths =list(zip(files, files_path))
	data = dict(file_paths)
	#print(data)
	#print("number of " + file_type+ " files in '" + thisdir + " : " + str(len(files)))  
	file_name ="{}.json".format(file_type)
	with open(file_name, 'w') as fp:
		json.dump(data,fp)
def extract_information(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

    txt = f"""
    Information about {pdf_path}: 

    Author: {information.author}
    Creator: {information.creator}
    Producer: {information.producer}
    Subject: {information.subject}
    Title: {information.title}
    Number of pages: {number_of_pages}
    """

    print(txt)
    return information
def recommend_file(file_type):
	if file_type == "pdf":
		file_name ="{}.json".format(file_type)
		with open(file_name) as json_file:
			data =json.load(json_file)
		key_files =list(data.keys())
		file_choice = random.choice(key_files)
		print(file_choice)
		extract_information(data[file_choice])
		#os.startfile(data[file_choice], 'open')
		subprocess.run(['open', data[file_choice]], check=True)
	elif file_type =="video":
		file_name ="{}.json".format(file_type)
		with open(file_name) as json_file:
			data =json.load(json_file)
		key_files =list(data.keys())
		file_choice = random.choice(key_files)
		print(file_choice)

		subprocess.run(['open', data[file_choice]], check=True)

	elif file_type == "websites":
		file_name ="{}.json".format(file_type)
		with open(file_name) as json_file:
			data =json.load(json_file)
		key_files =list(data.keys())
		file_choice = random.choice(key_files)
		print(random.choice(key_files))
		subprocess.run(['open', data[file_choice]], check=True)

def write_files():
	pass
def recommend(mood ="normal", filetype= None, duration =None):
	pass
def rate_file(name, rate):
	pass
def delete_file(name):
	pass
def viewed_files():
	pass

def update_database():
	pass
def connect_to_dabase():
	pass
def update_database():
	pass
def delete_value():
	pass


#read_files("video")
recommend_file("video")
#recommend_file("websites")
#recommend_file("pdf")

""" 
import subprocess, os, platform
if platform.system() == 'Darwin':       # macOS
    subprocess.call(('open', filepath))
elif platform.system() == 'Windows':    # Windows
    os.startfile(filepath)
else:                                   # linux variants
    subprocess.call(('xdg-open', filepath))
"""

