import os, re, shutil, glob

#List of companies(abbreviated)
companies =['ACC','AIR','AKA','ALLGO','AM','APPLIED','ALLSTATE','ARI','BOSCH','CONTI','DELL','DELO','ERN']
companies+=['FCS','FIDELITY','HP','IBM','INFOR','MANTRI','MERCE','MOTO','MU','NETAPP','NOVELL','ORACLE','SAP']
companies+=['TCS','WIPRO','YOKOGAWA','MINDTREE','COMMVAULT','EVIVE','NATIONAL','UTC','Y MEDIA','DELPHI','AIG']
companies+=['E AND Y','AMETEK','BOSCH','GM','IMS','INFOSYS','L & T','SCHNEIDER','ONMOBILE','TATA']
companies+=['TE CONNECTIVITY','ATKINS','IBM','NI','SOC GEN','ODESSA','TCS']
       
#Function to Create a folder for each company 
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

#Call the function
for i in range(len(companies)):
	createFolder('./'+companies[i])

#Get current woking directory
my_dir = os.getcwd()

#Obtain only files (not folders)
files_only = glob.glob(my_dir+'/*.*')

#Loop
for j in range(len(files_only)):
	for i in range(len(companies)):
		pattern = re.compile(companies[i])
		x = pattern.search(files_only[j])
	        if(x):
			shutil.move(files_only[j],companies[i])

