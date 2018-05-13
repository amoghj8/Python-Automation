import os

#Run in shell
#Access the cuurent working directory
file_path = os.getcwd()
#Convert to uppercase
for file_name in file_path:
	os.rename(file_name,file_name.upper())


