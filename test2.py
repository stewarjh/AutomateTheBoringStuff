import os, shutil

os.chdir('C:\\Users\\SNEAKY\\Desktop\\AutomateTheBoringStuff2')
print(os.getcwd())

for folderName, subfolders, filenames in os.walk('C:\\Users\\SNEAKY\\Desktop\\AutomateTheBoringStuff2'):
	for file in filenames:
		if file.endswith('.txt'):
			shutil.copy(file, 'C:\\Users\SNEAKY\\Desktop\\test2')
	for file in filenames:
		if file.endswith('.txt'):
			os.unlink(file)





